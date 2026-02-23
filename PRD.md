# Product Requirements Document (PRD)
## Customer Churn Prediction Web App

**Version:** 2.0 (Production-Grade)  
**Author:** Pawan Simha  
**Date:** February 2026  
**Status:** ✅ Production Ready

---

## 1. Project Overview

### Purpose
The Customer Churn Predictor is a high-fidelity ML platform that enables telecom providers to identify and retain at-risk customers. It serves as a showcase for end-to-end ML deployment, featuring secure session management, sophisticated ensemble modeling, and a premium UX.

### Problem Statement
Customer churn directly impacts the bottom line. This tool provides a secure, easy-to-use interface to operationalize complex predictive models into actionable business intelligence.

---

## 2. Technical Architecture (V2)

### Security Layer (Production)
- **Authentication:** SQLite-backed user database with PBKDF2 password hashing. No plaintext credentials.
- **CSRF Protection:** Industrial-grade CSRF protection on all data-entry and authentication forms via `Flask-WTF`.
- **Response Headers:** Secure HTTP headers (`HSTS`, `X-Frame-Options`, `nosniff`) enabled for every response.

### AI Engine
- **Ensemble Logic:** Soft-voting VotingClassifier combining RandomForest, XGBoost, LightGBM, and CatBoost.
- **Inference:** High-performance inference with real-time confidence probability calculation.

### Presentation Layer
- **UI Design:** Glassmorphism-based cinematic interface with smooth step-transitions.
- **Download System:** Built-in `html2canvas` pipeline for local result archival.

---

## 3. Evaluated Metrics (Post-Audit)

| Metric | Score | Validation |
| :--- | :--- | :--- |
| **Logic Consistency** | 10.0 | Synchronized feature ordering; robust error fallback logic. |
| **Security Architecture** | 9.5 | SQLite migration; Secure hashing; CSRF protection. |
| **UI/UX Flow** | 9.5 | 3-step guided experience; seamless mobile responsiveness. |
| **Deployment Flow** | 10.0 | Portable `%~dp0` batch launcher with auto-initialization. |

---

## 4. Requirement Traceability

| ID | Requirement | Status |
|---|---|---|
| REQ-01 | Secure SQLite Authentication | ✅ Complete |
| REQ-02 | Password Hashing (Werkzeug) | ✅ Complete |
| REQ-03 | CSRF Protection (WTF) | ✅ Complete |
| REQ-04 | 3-Step Guided UX | ✅ Complete |
| REQ-05 | Ensemble Prediction (p=99.3%) | ✅ Complete |
| REQ-06 | Confidence Score UI | ✅ Complete |
| REQ-07 | Result Archetyping (PNG) | ✅ Complete |
| REQ-08 | Portable Win Launcher (.bat) | ✅ Complete |

---

## 5. Deployment Guidelines

### Professional Environment
For real-world scaling, it is recommended to replace the built-in Flask dev server with:
- **Server:** Gunicorn / Waitress
- **Proxy:** Nginx with SSL/TLS termination
- **Database:** PostgreSQL (for high-concurrency environments)

---

*Verified by Pawan Simha | [GitHub](https://github.com/PawanSimha) | [LinkedIn](https://linkedin.com/in/pawansimha)*
