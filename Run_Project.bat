@echo off
title Customer Churn Prediction
color 0A

:: ── Absolute path to the project root (edit this if you move the folder) ──
set "PROJECT=c:\Users\pawan\SNPSU\Projects\Customer Churn Prediction"

:: ── Always run from the project root ──
cd /d "%PROJECT%"

echo ============================================
echo   Customer Churn Prediction App
echo ============================================
echo.
echo   Project folder: %PROJECT%
echo.

:: Kill any existing process on port 5000
for /f "tokens=5" %%a in ('netstat -ano 2^>nul ^| findstr /R ":5000 "') do (
    taskkill /PID %%a /F >nul 2>&1
)

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found in PATH.
    pause & exit /b 1
)

:: Install Flask if missing
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing dependencies...
    pip install -r "%PROJECT%\requirements.txt"
    echo.
)

:: Check model file
if not exist "%PROJECT%\churn_prediction_model.pkl" (
    echo [ERROR] churn_prediction_model.pkl not found.
    echo         Run the Jupyter notebook first to generate it.
    pause & exit /b 1
)

echo [OK] Starting server from: %PROJECT%
echo.
echo ============================================
echo   URL     : http://127.0.0.1:5000
echo   Logins  : PawanSimha / simha@123
echo             Prajwal    / raju@123
echo             Ankitha    / reddy@123
echo ============================================
echo.
echo   Browser opens in 3 seconds.
echo   Close this window to stop the server.
echo.

:: 3-second delay then open browser (no extra window)
ping -n 4 127.0.0.1 >nul
start "" http://127.0.0.1:5000

:: Launch Flask using the explicit app.py path
python "%PROJECT%\app.py"
pause
