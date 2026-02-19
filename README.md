<h1 align="center">
  <img src="static/Churn.jpg" alt="Logo" width="80" style="border-radius:50%"><br>
  Customer Churn Prediction
</h1>

<p align="center">
  <b>A full-stack ML web app that predicts telecom customer churn using an ensemble of RandomForest, XGBoost, LightGBM, and CatBoost.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.x-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/scikit--learn-1.8-orange?logo=scikit-learn" alt="sklearn">
  <img src="https://img.shields.io/badge/XGBoost-3.2-red" alt="XGBoost">
  <img src="https://img.shields.io/badge/LightGBM-4.6-green" alt="LightGBM">
  <img src="https://img.shields.io/badge/CatBoost-1.2-yellow" alt="CatBoost">
</p>

---

## 📌 Overview

This project predicts whether a telecom customer will **churn** (leave the service) based on 19 customer features. It uses a **VotingClassifier** ensemble model trained on the `IT_customer_churn.csv` dataset, balanced with SMOTE, and served via a Flask web application with a clean multi-step UI.

---

## ✨ Key Features

- 🔐 **Session-based login** with multiple user accounts
- 📋 **3-step guided form** for entering customer features
- 🤖 **Ensemble ML model** (RandomForest + XGBoost + LightGBM + CatBoost)
- 📊 **Result page** with colour-coded prediction and full input summary table
- 📥 **Download result as image** (html2canvas)
- 📱 **Fully responsive** — works on mobile, tablet, and desktop
- 🎨 **Glassmorphism UI** with smooth transitions and hover effects
- 🖱️ **One-click launch** via `Run_Project.bat`

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11, Flask |
| **ML Model** | scikit-learn VotingClassifier (RF + XGBoost + LightGBM + CatBoost) |
| **Data Balancing** | SMOTE (imbalanced-learn) |
| **Frontend** | HTML5, CSS3 (Poppins font, CSS variables), Vanilla JS |
| **Notebook** | Jupyter (data analysis + model training) |
| **Dataset** | IT Customer Churn CSV (telecom) |

---

## 📁 Project Structure

```
Customer Churn Prediction/
├── 🖱️ Run_Project.bat                          # Double-click to launch
├── app.py                                       # Flask application
├── churn_prediction_model.pkl                   # Trained ensemble model (~80MB)
├── IT_customer_churn.csv                        # Training dataset
├── Customer Churn Analysis and Prediction.ipynb # Training notebook
├── requirements.txt                             # Python dependencies
├── RUN_PROJECT_STEPS.md                         # Manual run guide
├── .gitignore
├── static/
│   ├── Churn.jpg                                # Favicon / logo
│   ├── style.css                                # Global stylesheet
│   └── Background.jpg                           # Background image
└── templates/
    ├── login.html                               # Login page
    ├── index.html                               # 3-step prediction form
    └── result.html                              # Prediction result page
```

---

## 🚀 Quick Start

### Option 1 — Double-click (Windows)
```
Double-click Run_Project.bat
```
### Quick Start (Windows)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PawanSimha/Customer-Churn-Prediction.git
   cd "Customer Churn Prediction"
   ```

2. **Configure Environment** (Optional but recommended):
   Copy `.env.example` to `.env` and update the secret key:
   ```bash
   copy .env.example .env
   ```

3. **Run the One-Click Installer**:
   Double-click `Run_Project.bat`.
   *It will install dependencies, check the model, and launch the app automatically.*

### Manual Installation

1. **Install Python 3.10+**
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the App**:
   ```bash
   python app.py
   ```
4. **Open Browser**: `http://127.0.0.1:5000`

---

## 🔑 Login Credentials

| Username | Password |
|---|---|
| `PawanSimha` | `simha@123` |
| `Prajwal` | `raju@123` |
| `Ankitha` | `reddy@123` |

---

## 🧠 Model Details

| Component | Details |
|---|---|
| **Algorithm** | VotingClassifier (soft voting) |
| **Base Models** | RandomForestClassifier, XGBClassifier, LGBMClassifier, CatBoostClassifier |
| **Balancing** | SMOTE (Synthetic Minority Oversampling) |
| **Encoding** | LabelEncoder for all categorical features |
| **Features** | 19 telecom features (Gender, Tenure, Contract, etc.) |
| **Target** | Binary: Churn (1) / No Churn (0) |

---

## 📋 Requirements

```
flask
numpy
pandas
scikit-learn
xgboost
lightgbm
catboost
imbalanced-learn
seaborn
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Pawan Simha**
- GitHub: [@PawanSimha](https://github.com/PawanSimha)
- LinkedIn: [linkedin.com/in/pawansimha](https://linkedin.com/in/pawansimha)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
