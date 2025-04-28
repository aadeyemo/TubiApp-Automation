@echo off
echo Starting Appium Server...
start cmd /k "appium"

timeout /t 10

echo Running Pytest Test Cases...
cd C:\Users\andre\TubiApp-Automation
pytest

pause
