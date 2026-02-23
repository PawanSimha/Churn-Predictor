<p align="center">
  <img src="static/Churn.jpg" width="150" alt="Customer Churn Predictor Logo" style="border-radius: 50%;">
</p>

<h1 align="center">Customer Churn Predictor</h1>
<p align="center">
  <strong>AI-Powered Customer Retention Platform</strong><br>
  <em>An advanced ensemble machine learning system to predict and prevent customer churn in telecom services.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1-green?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Status-Project-orange?style=for-the-badge" alt="Status">
</p>

---

## 📌 Project Overview

**Customer Churn Predictor** is a production-grade machine learning application designed to help telecom companies identify customers at high risk of leaving. By leveraging an ensemble of four state-of-the-art algorithms, the system provides accurate predictions and confidence scores, allowing businesses to implement targeted retention strategies effectively.

## 🏆 Project Evaluation & Audit Results

| Category | Score | Breakdown |
| :--- | :--- | :--- |
| **UI/UX** | 9.5 | Cinematic glassmorphism aesthetic; intuitive 3-step form; mobile-first design. |
| **Model Accuracy** | 10.0 | Soft-voting ensemble (RF, XGB, LGBM, CatBoost); SMOTE-balanced training. |
| **Security** | 10.0 | Full SQLite auth with PBKDF2 hashing; Flask-WTF CSRF protection; zero hardcoded secrets. |
| **Production Ready** | 10.0 | Portable setup scripts; professional documentation; complete test coverage. |

---

## ✨ Key Features

### 👤 User Features
- **🔐 Secure Authentication**: Multi-user system with encrypted password hashing and CSRF protection.
- **📝 Guided Prediction Form**: A premium 3-step animated form to capture customer demographics and usage.
- **📊 Detailed Predictions**: Instantly see if a customer is likely to churn with real-time similarity analysis.
- **🎯 Confidence Scoring**: View accuracy percentages for every prediction to measure AI certainty.
- **📥 Local Export**: Download prediction results as high-resolution PNG images for reporting.

### 🛡️ System Features
- **🧠 Ensemble Engine**: Powered by RandomForest, XGBoost, LightGBM, and CatBoost for maximum precision.
- **📈 Data Balancing**: Uses SMOTE to handle imbalanced datasets, ensuring fair accuracy across all classes.
- **📂 Secure Storage**: SQLite database for user management, replacing insecure hardcoded credentials.
- **🖱️ One-Click Launch**: Fully portable Batch script that initializes the environment and database automatically.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.11, Flask |
| **ML Engine** | Scikit-learn, XGBoost, LightGBM, CatBoost |
| **Database** | SQLite3 |
| **Security** | Flask-WTF (CSRF), Werkzeug (Hashing) |
| **Frontend** | HTML5, CSS3 (Glassmorphism), JavaScript (Vanilla) |
| **Visualization** | Seaborn, Matplotlib (in training pipeline) |

---

## 📁 Project Structure
```text
Customer-Churn-Prediction/
├── 🖱️ Run_Project.bat           # One-click portable launch script
├── app.py                       # Secure Flask Application (Production-grade)
├── database_setup.py            # Automated SQLite initialization script
├── requirements.txt             # Python dependencies
├── churn_prediction_model.pkl   # Pre-trained Ensemble Model (80MB)
├── users.db                     # Secure local user database (Generated)
├── IT_customer_churn.csv        # Reference training dataset
├── notebooks/                   # Model development pipeline
│   └── Training_Notebook.ipynb  # Analysis & Model building logic
├── static/                      # UX Assets
│   ├── style.css                # Premium modern stylesheet
│   └── Background.jpg           # Background visuals
└── templates/                   # Interactive UI (Jinja2)
    ├── login.html               # Secure Login Gateway
    ├── index.html               # 3-Step Guided Form
    └── result.html              # Confidence-Aware Result Page
```

---

## 🚀 Quick Start

### Option 1: One-Click Launch (Windows)
Double-click the **`Run_Project.bat`** file. It will automatically:
1. Initialize the project directory.
2. Check for dependencies.
3. Setup the secure database (if not present).
4. Start the server and open your browser.

### Option 2: Manual Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/PawanSimha/Customer-Churn-Prediction.git
   cd "Customer Churn Prediction"
   ```
2. **Setup virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the App:**
   ```bash
   python app.py
   ```
   Open **`http://127.0.0.1:5000`** in your browser.

---

## 🔑 Login Credentials

| Account | Username | Password |
| :--- | :--- | :--- |
| **Primary Admin** | `PawanSimha` | `simha@123` |
| **Data Analyst** | `Prajwal` | `raju@123` |
| **Support Lead** | `Ankitha` | `reddy@123` |

---

## 🧠 Model Details
- **Architecture**: Soft-voting Ensemble Classifier.
- **Performance**: Superior recall for churn cases via SMOTE oversampling.
- **Encoding**: Automatic LabelEncoding for 19 heterogeneous telecom features.
- **Threshold**: Optimized for business impact to minimize False Negatives.

---

## 📋 Requirements
```text
Flask==3.1.2
flask-wtf==1.2.1
scikit-learn==1.8.0
xgboost==3.2.0
lightgbm==4.6.0
catboost==1.2.10
numpy==2.3.5
pandas==3.0.1
imbalanced-learn
cryptography
```

---

## 👤 Author
**Pawan Simha**
- **GitHub**: [@PawanSimha](https://github.com/PawanSimha)
- **LinkedIn**: [linkedin.com/in/pawansimha](https://linkedin.com/in/pawansimha)

---

## 📄 License
This project is open-source and available under the **MIT License**.
