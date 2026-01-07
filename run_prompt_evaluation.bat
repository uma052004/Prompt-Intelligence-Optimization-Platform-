@echo off
echo ================================
echo Prompt Evaluation System
echo ================================

REM Go to project folder
cd /d "%USERPROFILE%\Desktop\PromptEvaluationSystem"

REM Run Streamlit app
python -m streamlit run app.py

pause
