# Quick Start Guide

## 🚀 5-Minute Setup

### Windows
```bash
# 1. Run setup
setup.bat

# 2. Edit .env with your OpenAI API key
# Open .env and replace: OPENAI_API_KEY=sk-proj-your_key_here

# 3. Start the app
streamlit run main.py
```

### macOS/Linux
```bash
# 1. Run setup
bash setup.sh

# 2. Edit .env with your OpenAI API key
nano .env  # or vim .env

# 3. Start the app
streamlit run main.py
```

## 📋 Manual Setup

### Step 1: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Get OpenAI API Key
1. Visit: https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key starting with `sk-proj-`

### Step 4: Configure .env
```bash
# Edit .env file and update:
OPENAI_API_KEY=sk-proj-your_actual_key_here
```

### Step 5: Create Directories
```bash
mkdir -p models/trained_models logs data/raw data/processed
```

### Step 6: Run Application
```bash
streamlit run main.py
```

App opens at: **http://localhost:8501**

## 🎯 Features to Try

1. **Home** - Overview of all features
2. **Crop Recommendations** - Get AI crop suggestions
3. **Yield Prediction** - Predict harvest yield
4. **Disease Detection** - Upload crop images
5. **Price Prediction** - Forecast market prices
6. **Analytics Dashboard** - View farming metrics
7. **Collaboration** - Connect with farmers

## 🔌 API Usage

### Start API Server
```bash
python src/api/app.py
```

### Test API
```bash
# Health check
curl http://localhost:5000/api/health

# Predict yield
curl -X POST http://localhost:5000/api/predict/yield \
  -H "Content-Type: application/json" \
  -d '{"temperature": 25, "humidity": 60, "rainfall": 150}'
```

## ⚠️ Common Issues & Solutions

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt
```

### "OpenAI API key not found"
1. Check `.env` file exists in project root
2. Verify format: `OPENAI_API_KEY=sk-proj-xxxxx`
3. Restart Streamlit: `Ctrl+C` then run again

### "Port 8501 already in use"
```bash
streamlit run main.py --server.port 8502
```

### PyTorch installation issues
```bash
# CPU only (faster)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# With GPU support (CUDA 11.8)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 📚 Documentation Files

- **README.md** - Full project documentation
- **SETUP_INSTRUCTIONS.md** - Detailed setup guide
- **TROUBLESHOOTING.md** - Common issues & fixes
- **.env.example** - Environment variable template

## 🔐 Security Checklist

- [ ] Added OpenAI API key to `.env`
- [ ] `.env` is NOT committed to git
- [ ] Using HTTPS for API calls
- [ ] No credentials in code files
- [ ] `.gitignore` properly configured

## 📞 Need Help?

1. Check error message carefully
2. Review TROUBLESHOOTING.md
3. Check logs: `tail -f logs/app.log`
4. Verify all dependencies: `pip list`
5. Reinstall if needed: `pip install --upgrade -r requirements.txt`

---

**Ready to farm smarter with Agri-agent! 🌾**
