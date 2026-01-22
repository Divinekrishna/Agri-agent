#!/bin/bash
# Quick setup script for macOS/Linux

echo "🌾 Setting up Agri-agent..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating project directories..."
mkdir -p models/trained_models
mkdir -p logs
mkdir -p data/raw
mkdir -p data/processed

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your OpenAI API key"
fi

# Verify installation
echo "Verifying installation..."
python -c "import streamlit; import torch; import sklearn; print('✓ All packages installed successfully!')"

echo ""
echo "🎉 Setup complete!"
echo "Next steps:"
echo "1. Edit .env and add your OpenAI API key"
echo "2. Run: streamlit run main.py"
echo ""
