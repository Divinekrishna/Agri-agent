# ✅ Agri-agent Setup Checklist

## Pre-Setup Checklist

- [ ] Python 3.8+ installed
- [ ] pip/conda package manager working
- [ ] Internet connection available
- [ ] Text editor or IDE ready (VS Code recommended)
- [ ] GitHub account (optional, for deployment)

---

## Installation Checklist

### Step 1: Clone/Download
- [ ] Project downloaded to local machine
- [ ] Located at: `c:\Users\losha\hackathon\Agri-agent`
- [ ] All files present

### Step 2: Virtual Environment
- [ ] Virtual environment created
  ```bash
  python -m venv venv
  ```
- [ ] Virtual environment activated
  ```bash
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
  ```
- [ ] Verified with: `which python` or `where python`

### Step 3: Dependencies
- [ ] requirements.txt present and readable
- [ ] All packages installed without errors
  ```bash
  pip install -r requirements.txt
  ```
- [ ] Installation verified:
  ```bash
  python -c "import streamlit; import torch; print('OK')"
  ```

### Step 4: Configuration
- [ ] `.env` file created in project root
- [ ] `.env.example` used as reference
- [ ] Database URL configured (or using default SQLite)
- [ ] Model directory set: `./models/trained_models`

### Step 5: API Key Setup
- [ ] OpenAI account created at https://platform.openai.com
- [ ] API key generated and copied (starts with `sk-proj-`)
- [ ] API key pasted into `.env` file
  ```env
  OPENAI_API_KEY=sk-proj-your_actual_key_here
  ```
- [ ] `.env` NOT committed to git (check `.gitignore`)
- [ ] API key verified to be valid and active

### Step 6: Directory Structure
- [ ] Project root verified
- [ ] `src/` directory contains all modules
- [ ] `src/pages/` contains all Streamlit pages (7 files)
- [ ] `src/models/` contains ML models
- [ ] `src/utils/` contains utilities
- [ ] `src/api/` contains Flask API
- [ ] Directories created as needed:
  ```bash
  mkdir -p models/trained_models logs data/raw data/processed
  ```

---

## Pre-Launch Verification

### Python & Environment
- [ ] Python version: `python --version` shows 3.8+
- [ ] Virtual environment active
- [ ] Correct Python executable: `which python` or `where python`

### Dependencies
- [ ] Streamlit installed: `python -c "import streamlit; print(streamlit.__version__)"`
- [ ] PyTorch installed: `python -c "import torch; print(torch.__version__)"`
- [ ] scikit-learn installed: `python -c "import sklearn; print(sklearn.__version__)"`
- [ ] All imports work: `python -c "from src.models import *; print('OK')"`

### Configuration
- [ ] `.env` file exists in project root
- [ ] `.env` contains valid values
- [ ] `config.py` contains correct settings
- [ ] No hardcoded secrets in Python files
- [ ] Sensitive files in `.gitignore`:
  - [ ] `.env`
  - [ ] `*.pth` (model files)
  - [ ] `__pycache__/`
  - [ ] `venv/`

### File Permissions
- [ ] All files readable by user
- [ ] `.env` file readable
- [ ] `setup.sh` executable (macOS/Linux): `chmod +x setup.sh`
- [ ] `setup.bat` works (Windows)

---

## Launch Checklist

### Before First Run
- [ ] Terminal/Command prompt ready
- [ ] Virtual environment activated
- [ ] Current directory is project root: `pwd` or `cd c:\Users\losha\hackathon\Agri-agent`
- [ ] API key is set in `.env`
- [ ] No port conflicts (8501 for Streamlit, 5000 for Flask)

### Launch Commands
- [ ] Streamlit command ready: `streamlit run main.py`
- [ ] Flask command ready: `python src/api/app.py`
- [ ] Alternative port ready if needed: `streamlit run main.py --server.port 8502`

### First Launch
- [ ] Streamlit starts without errors
- [ ] Application loads at: `http://localhost:8501`
- [ ] Home page displays correctly
- [ ] Sidebar menu shows all 7 pages
- [ ] No error messages in console

---

## Feature Verification

### Home Page
- [ ] Loads without errors
- [ ] All feature cards display
- [ ] Navigation links work
- [ ] Overview text visible

### Crop Recommendations
- [ ] Page loads correctly
- [ ] Input fields respond
- [ ] "Generate Recommendations" button clickable
- [ ] Returns recommendations (or proper error if API issue)

### Yield Prediction
- [ ] Page loads correctly
- [ ] Sliders work properly
- [ ] "Predict Yield" button clickable
- [ ] Shows results with confidence score

### Disease Detection
- [ ] Page loads correctly
- [ ] File uploader works
- [ ] "Analyze Image" button appears
- [ ] Handles image upload (test with any image)

### Price Prediction
- [ ] Page loads correctly
- [ ] Toggle between prediction types works
- [ ] "Predict Price" button clickable
- [ ] Shows price forecast

### Analytics Dashboard
- [ ] Page loads correctly
- [ ] Displays KPI cards
- [ ] Charts render properly
- [ ] Data table shows correctly

### Collaboration
- [ ] Page loads correctly
- [ ] Tabs switch properly
- [ ] Content displays in each tab
- [ ] Buttons are interactive

---

## API Verification

### API Server
- [ ] Flask API starts: `python src/api/app.py`
- [ ] No errors in console
- [ ] Server running message visible
- [ ] Running at `http://localhost:5000`

### API Endpoints
- [ ] Health check works:
  ```bash
  curl http://localhost:5000/api/health
  ```
- [ ] Returns valid JSON response
- [ ] Status shows "healthy"

### Test Predictions
- [ ] Yield prediction endpoint works
- [ ] Price prediction endpoint works
- [ ] Disease detection endpoint handles images
- [ ] Crop recommendations endpoint works

---

## Documentation Review

- [ ] README.md reviewed
- [ ] QUICKSTART.md reviewed
- [ ] SETUP_INSTRUCTIONS.md reviewed
- [ ] TROUBLESHOOTING.md bookmarked
- [ ] API_DOCUMENTATION.md saved
- [ ] PROJECT_SUMMARY.md reviewed

---

## Security Verification

- [ ] API key NOT in code files
- [ ] API key NOT in git history
- [ ] `.env` in `.gitignore`
- [ ] No hardcoded passwords
- [ ] CORS properly configured for API
- [ ] No debug mode in production

### Git Configuration
- [ ] `.gitignore` excludes:
  - [ ] `.env`
  - [ ] `venv/`
  - [ ] `__pycache__/`
  - [ ] `*.pyc`
  - [ ] `.streamlit/`
  - [ ] `logs/`
  - [ ] Model files

---

## Performance Baseline

- [ ] Streamlit app load time noted: ___ seconds
- [ ] First prediction time noted: ___ ms
- [ ] API response time noted: ___ ms
- [ ] No memory warnings or errors
- [ ] CPU usage reasonable

---

## Backup & Deployment Prep

- [ ] Project backed up locally
- [ ] `.env` backed up securely (separate from git)
- [ ] Model weights backed up (if any)
- [ ] Git repository initialized (optional)
- [ ] Remote repository set up (optional)

---

## Production Readiness

- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Input validation in place
- [ ] Rate limiting considered
- [ ] CORS properly configured
- [ ] Environment variables used for config
- [ ] No debug mode enabled
- [ ] Dependencies pinned in requirements.txt

---

## Team Handoff Checklist

If sharing with team:
- [ ] README.md explains setup
- [ ] SETUP_INSTRUCTIONS.md is clear
- [ ] Team has access to `.env` template
- [ ] Team knows where to get API key
- [ ] Team has write access to repository
- [ ] Deployment instructions provided
- [ ] Support contact information shared

---

## Ongoing Maintenance

### Weekly
- [ ] Check API usage and costs
- [ ] Monitor application logs
- [ ] Verify backups working

### Monthly
- [ ] Update dependencies: `pip list --outdated`
- [ ] Review security advisories
- [ ] Performance monitoring

### Quarterly
- [ ] Model accuracy review
- [ ] Feature request evaluation
- [ ] Security audit

---

## Troubleshooting Started?

If something isn't working:
- [ ] Check error message carefully
- [ ] Search `TROUBLESHOOTING.md`
- [ ] Check console/terminal logs
- [ ] Verify `.env` configuration
- [ ] Verify virtual environment active
- [ ] Try restarting application
- [ ] Clear Streamlit cache: `streamlit cache clear`
- [ ] Try different port if conflict
- [ ] Review application logs: `tail -f logs/app.log`

---

## Final Sign-Off

- [ ] All checklist items completed
- [ ] Application running successfully
- [ ] All features tested
- [ ] Documentation reviewed
- [ ] Ready to start development/production

**Project Status**: ✅ READY TO USE

---

**Date Completed**: _______________

**Completed By**: _______________

**Notes**:
```
_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________
```

---

## Quick Reference Commands

```bash
# Activate virtual environment
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# Run Streamlit app
streamlit run main.py

# Run Flask API
python src/api/app.py

# Run both (separate terminals)
# Terminal 1: streamlit run main.py
# Terminal 2: python src/api/app.py

# Test imports
python -c "import streamlit; import torch; import sklearn; print('OK')"

# Check Python version
python --version

# List installed packages
pip list

# Clear Streamlit cache
streamlit cache clear

# View logs
tail -f logs/app.log              # macOS/Linux
type logs\app.log                 # Windows

# Test API health
curl http://localhost:5000/api/health

# Deactivate virtual environment
deactivate
```

---

**🎉 Congratulations! You're all set to use Agri-agent!**

**Next Step**: Start the application with `streamlit run main.py`
