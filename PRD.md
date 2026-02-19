# Product Requirements Document (PRD)
## Customer Churn Prediction Web App

**Version:** 1.0  
**Author:** Pawan Simha  
**Date:** February 2026  
**Status:** ✅ Complete

---

## 1. Project Overview

### Purpose
The Customer Churn Prediction app enables telecom business analysts and data science students to predict whether a customer will churn (leave the service) based on their account and usage profile. It demonstrates a production-style ML pipeline from data preprocessing to a deployable web interface.

### Problem Statement
Telecom companies lose significant revenue to customer churn. Early identification of at-risk customers allows targeted retention campaigns. This tool operationalises a trained ML model into an accessible web interface.

### Target Audience
- Telecom business analysts
- Data science students and educators
- ML practitioners evaluating ensemble models

---

## 2. Core User Flows

### Flow 1: Login
```
User visits / → Enters username + password → POST /login
→ Valid: redirect to /index
→ Invalid: show error message on login page
```

### Flow 2: Churn Prediction
```
/index (Step 1: Personal & Account Info)
  → Next → (Step 2: Services)
  → Next → (Step 3: Billing & Payment)
  → Submit → POST /predict
  → /result: shows Churn / No Churn with input table
```

### Flow 3: Post-Result Actions
```
Result page → Download as Image (html2canvas)
           → Back to Form (/index)
           → Logout (/logout → /)
```

### Flow 4: Auth Protection
```
Any protected route (/index, /predict, /logout) without session
→ Redirect to / (login page)
```

---

## 3. Functional Requirements

| ID | Requirement | Status |
|---|---|---|
| FR-01 | Session-based login with username/password | ✅ |
| FR-02 | Invalid login shows error message | ✅ |
| FR-03 | 3-step multi-page form with Back/Next navigation | ✅ |
| FR-04 | All routes protected by login_required decorator | ✅ |
| FR-05 | Prediction using VotingClassifier ensemble model | ✅ |
| FR-06 | Result page shows Churn/No Churn with colour coding | ✅ |
| FR-07 | Result page shows full input feature table | ✅ |
| FR-08 | Download result as PNG image | ✅ |
| FR-09 | Logout clears session and redirects to login | ✅ |
| FR-10 | Graceful error handling for prediction failures | ✅ |

---

## 4. Non-Functional Requirements

| ID | Requirement | Status |
|---|---|---|
| NFR-01 | Fully responsive UI (mobile, tablet, desktop) | ✅ |
| NFR-02 | Page load < 3s on local network | ✅ |
| NFR-03 | SEO meta tags and OG tags on all pages | ✅ |
| NFR-04 | Consistent design system (CSS variables, Poppins font) | ✅ |
| NFR-05 | One-click launch via Run_Project.bat | ✅ |
| NFR-06 | Model file path resolved relative to app.py | ✅ |

---

## 5. Technical Architecture

```
┌─────────────────────────────────────────────┐
│                  Browser                    │
│  login.html / index.html / result.html      │
│  style.css (Poppins, CSS vars, responsive)  │
└──────────────────┬──────────────────────────┘
                   │ HTTP (Flask dev server)
┌──────────────────▼──────────────────────────┐
│               Flask App (app.py)            │
│  Routes: / /login /index /predict /logout   │
│  Auth: session + login_required decorator   │
│  Model: pickle.load(churn_prediction_model) │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         VotingClassifier (pkl, ~80MB)       │
│  RandomForest + XGBoost + LightGBM          │
│  + CatBoost  |  Trained on IT_churn.csv     │
│  Balanced with SMOTE                        │
└─────────────────────────────────────────────┘
```

### Feature Pipeline
```
Raw CSV → LabelEncoder (categorical) → Numeric conversion
→ SMOTE balancing → VotingClassifier training → pickle save
→ Flask loads pkl → np.array([19 features]) → predict()
```

### 19 Input Features (in order)
`Gender, SeniorCitizen, Partner, Dependents, Tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges`

---

## 6. Dataset

| Property | Value |
|---|---|
| File | `IT_customer_churn.csv` |
| Size | ~900KB |
| Rows | ~7,000 telecom customers |
| Target | `Churn` (binary: Yes/No) |
| Class Imbalance | Handled with SMOTE |

---

## 7. Security Considerations

- Credentials are hardcoded (suitable for demo/academic use only)
- For production: use a database with hashed passwords (bcrypt)
- `SECRET_KEY` should be set via environment variable (`SECRET_KEY` env var supported)
- Debug mode should be disabled in production (`debug=False`)

---

## 8. Future Roadmap
- [x] **Production Readiness Audit** (Completed 2026-02-19): Comprehensive review of UI/UX, Security, Testing, and Documentation.
- [ ] **Database Integration**: Replace hardcoded users with SQLite/PostgreSQL.
- [ ] **Docker Support**: Add `Dockerfile` and `docker-compose.yml`.
- [ ] **Cloud Deployment**: Deploy to AWS Elastic Beanstalk or Azure App Service.
- [ ] **Model Retraining Pipeline**: API endpoint to accept new data and retrain the model.
- [ ] **Dashboard**: Add an admin dashboard to view churn statistics.
- [ ] **Prediction Confidence Score**: Add probability score to predictions.
- [ ] **Feature Importance Chart**: Display feature importance on the result page.
- [ ] **REST API Endpoint**: `/api/predict` for programmatic access.
- [ ] **Dark Mode Toggle**: UI option for dark mode.
- [ ] **Export Prediction History**: Export past predictions as CSV.
- [ ] **Admin Dashboard**: With prediction analytics.

---

## 9. Known Limitations

1. **Model size**: The pkl file is ~80MB — too large for GitHub without Git LFS
2. **Hardcoded users**: Not suitable for multi-user production deployment
3. **No HTTPS**: Flask dev server only; use Gunicorn + Nginx for production
4. **Low-risk profiles may predict Churn**: The ensemble model may over-predict churn on some edge cases — model tuning (threshold adjustment) is recommended

---

*Developed by Pawan Simha | [GitHub](https://github.com/PawanSimha) | [LinkedIn](https://linkedin.com/in/pawansimha)*
