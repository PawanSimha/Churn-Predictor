from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pickle
import os
from functools import wraps

# Create Flask app instance
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'futuristic_secret_key')  # Secret key to secure sessions

# Dictionary holding multiple users and their passwords for login authentication
USERS = {
    "PawanSimha": "simha@123",
    "Prajwal": "raju@123",
    "Ankitha": "reddy@123"
}

# Load pre-trained churn prediction model from pickle file
model_path = os.path.join(os.path.dirname(__file__), 'churn_prediction_model.pkl')
model = None

if os.path.exists(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
else:
    print(f"Warning: Model file not found at {model_path}")

# --- New: Decorator to protect routes that require login ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# --- Security Headers ---
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response


# Route for login page (GET request)
@app.route('/')
def login():
    return render_template("login.html")  # Render login form

# Route to handle login form submission (POST request)
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']  # Extract username from form
    password = request.form['password']  # Extract password from form

    # Check if username exists and password matches
    if username in USERS and USERS[username] == password:
        session['user'] = username  # Store logged in user in session
        return redirect(url_for('index'))  # Redirect to main index page
    else:
        # On invalid credentials, reload login page with error message
        return render_template('login.html', error="Invalid username or password")

# Route for main index page - only accessible if user is logged in
@app.route('/index')
@login_required
def index():
    return render_template("index.html")  # Show main page if user is logged in

# Route to handle churn prediction form submission (POST request)
@app.route('/predict', methods=['POST'])
@login_required
def predict():
    try:
        if not model:
            return render_template("index.html", prediction_error="Error: Model file not loaded.")

        # Feature order must match the notebook model: X = data.drop(columns=['Churn'])
        # Form field names (some differ from notebook columns, e.g. Gender vs gender, Tenure vs tenure)
        feature_order = [
            'Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'Tenure', 'PhoneService',
            'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
            'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
        ]

        def to_float(val, default=0.0):
            try:
                return float(val) if val != '' else default
            except (ValueError, TypeError):
                return default

        # Gather data in the same order as training data, converting to float
        final_features = [to_float(request.form.get(f)) for f in feature_order]
        inputs = list(request.form.items())
        # Predict churn using the pre-loaded model
        prediction = model.predict(np.array([final_features]))[0]
        result = "Churn" if prediction == 1 else "No Churn"
        # Render result page with inputs and prediction outcome
        return render_template("result.html", inputs=inputs, prediction=result)
    except Exception as e:
        # Handle any error during prediction and show it on the index page
        return render_template("index.html", prediction_error=f"Prediction Error: {str(e)}")

# --- New logout route to clear user session and redirect to login ---
@app.route('/logout')
@login_required
def logout():
    session.pop('user', None)  # Remove user from session if exists
    return redirect(url_for('login'))  # Redirect to login page after logout

# Run the Flask app in debug mode when script is executed directly
if __name__ == '__main__':
    app.run(debug=True)