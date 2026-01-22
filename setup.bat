@echo off
REM Quick setup script for Windows

echo 🌾 Setting up Agri-agent...

REM Check Python version
python --version
echo ✓ Python version checked

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create necessary directories
echo Creating project directories...
mkdir models\trained_models 2>nul
mkdir logs 2>nul
mkdir data\raw 2>nul
mkdir data\processed 2>nul

REM Create .env if it doesn't exist
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
    echo ⚠️  Please edit .env and add your OpenAI API key
)

REM Verify installation
echo Verifying installation...
python -c "import streamlit; import torch; import sklearn; print('✓ All packages installed successfully!')"

echo.
echo 🎉 Setup complete!
echo Next steps:
echo 1. Edit .env and add your OpenAI API key
echo 2. Run: streamlit run main.py
echo.
pause
