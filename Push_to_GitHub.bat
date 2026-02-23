@echo off
title Push to GitHub – Customer Churn Predictor
color 0B

echo ======================================================
echo   GITHUB PUSH AUTOMATION - CUSTOMER CHURN PREDICTOR
echo ======================================================
echo.

:: Check for Git
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed or not in PATH.
    pause
    exit /b
)

echo [1/4] Initializing Git LFS...
git lfs install
git lfs track "*.pkl"
git add .gitattributes
echo.

echo [2/4] Staging all production-grade updates...
git add .
echo.

echo [3/4] Creating final production commit...
set /p msg="Enter commit message (or press Enter for default): "
if "%msg%"=="" set msg="Elevate to Production: Secure Auth, CSRF, Confidence Scores, and Portability"
git commit -m "%msg%"
echo.

echo [4/4] Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] Primary push failed. Attempting 'master' branch...
    git push origin master
)

echo.
echo ======================================================
echo   PROCESS COMPLETE!
echo ======================================================
pause
