# Troubleshooting Guide

## Installation Issues

### 1. Virtual Environment Problems

**Issue**: `python: can't open file 'venv': [Errno 2] No such file or directory`

**Solution**:
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

---

### 2. Pip Not Found

**Issue**: `pip: command not found` or `'pip' is not recognized`

**Solution**:
```bash
# Use Python module instead
python -m pip install --upgrade pip

# Then install requirements
python -m pip install -r requirements.txt
```

---

### 3. Permission Denied on macOS/Linux

**Issue**: `Permission denied` when running pip

**Solution**:
```bash
# Use sudo carefully (last resort)
sudo -H pip install -r requirements.txt

# Better: ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

---

## Dependency Issues

### 4. PyTorch Installation Fails

**Issue**: `ERROR: Could not find a version that satisfies the requirement torch`

**Solution**:
```bash
# For CPU only (recommended for most users)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# For NVIDIA GPU (CUDA 12.1)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# For AMD GPU (ROCm)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.7
```

---

### 5. LangChain/OpenAI Import Errors

**Issue**: 
```
Import "langchain" could not be resolved
Import "langchain_openai" could not be resolved
```

**Solution**:
```bash
# Install LangChain components
pip install langchain langchain-openai langchain-community

# Verify installation
python -c "from langchain_openai import ChatOpenAI; print('✓ LangChain installed')"
```

---

### 6. scikit-learn Build Fails

**Issue**: `error: Microsoft Visual C++ 14.0 or greater is required`

**Solution**: 
On Windows, install Visual C++ Build Tools:
1. Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Run installer
3. Select "C++ build tools"
4. Restart and retry pip install

Or use pre-built wheel:
```bash
pip install --only-binary :all: scikit-learn
```

---

## Runtime Issues

### 7. OpenAI API Key Not Found

**Issue**: `OpenAI API key not found` or `API key is not set`

**Solution**:
1. Verify `.env` file exists:
   ```bash
   # Check if file exists
   ls .env          # macOS/Linux
   dir .env         # Windows
   ```

2. Verify `.env` format:
   ```env
   OPENAI_API_KEY=sk-proj-your_actual_key_here
   ```

3. Verify key is valid:
   - Visit: https://platform.openai.com/api-keys
   - Create new key if needed
   - Copy ENTIRE key (starts with `sk-proj-`)

4. Reload environment (restart app):
   ```bash
   # Stop Streamlit (Ctrl+C)
   # Then restart
   streamlit run main.py
   ```

---

### 8. Port Already in Use

**Issue**: `Address already in use` or `Port 8501 is already in use`

**Solution**:
```bash
# Find process using port (macOS/Linux)
lsof -i :8501

# Kill process (macOS/Linux)
kill -9 <PID>

# Or use different port
streamlit run main.py --server.port 8502

# For Flask API
python src/api/app.py --port 5001
```

On Windows:
```bash
# Find process
netstat -ano | findstr :8501

# Kill process
taskkill /PID <PID> /F

# Or use different port
streamlit run main.py --server.port 8502
```

---

### 9. Streamlit Cache Issues

**Issue**: `Permission denied` or cache corruption

**Solution**:
```bash
# Clear Streamlit cache
streamlit cache clear

# Or manually delete cache
rm -rf ~/.streamlit/cache/  # macOS/Linux
rmdir %USERPROFILE%\.streamlit\cache  # Windows
```

---

### 10. Module Import Errors

**Issue**: `ModuleNotFoundError: No module named 'streamlit'`

**Solution**:
```bash
# Check if virtual environment is activated
which python  # Should show venv path

# If not activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall requirements
pip install -r requirements.txt

# Verify
python -c "import streamlit; print('✓ Streamlit OK')"
```

---

## Application Issues

### 11. Crop Recommendations Not Working

**Issue**: Error when clicking "Generate Recommendations"

**Solution**:
1. Verify OpenAI API key is valid and has credits
2. Check API status: https://status.openai.com/
3. Verify internet connection
4. Check `logs/app.log` for detailed error
5. Try with fewer parameters first

---

### 12. Disease Detection Not Working

**Issue**: `No module named 'torchvision'` or image processing fails

**Solution**:
```bash
# Install torchvision with correct PyTorch version
pip install torchvision

# Or reinstall completely
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

---

### 13. Database Connection Error

**Issue**: `sqlite3.OperationalError: unable to open database file`

**Solution**:
```bash
# Create required directory
mkdir -p models/trained_models

# Or change DATABASE_URL in .env
DATABASE_URL=sqlite:///./agri_agent.db
```

---

### 14. Image Upload Issues

**Issue**: Image not uploading or processing fails

**Solution**:
1. Verify image format: JPEG, PNG, or BMP
2. Check image size: < 10MB recommended
3. Ensure PIL/Pillow is installed:
   ```bash
   pip install --upgrade Pillow
   ```
4. Check file permissions

---

## Performance Issues

### 15. Application Running Slowly

**Issue**: App takes long time to start or respond

**Solution**:
1. Clear cache:
   ```bash
   streamlit cache clear
   ```

2. Reduce model complexity:
   - Use CPU-only PyTorch
   - Reduce image resolution
   - Batch fewer predictions

3. Monitor resource usage:
   ```bash
   # macOS/Linux
   top -p $(pgrep -f streamlit)
   
   # Windows
   tasklist | findstr streamlit
   ```

---

### 16. High Memory Usage

**Issue**: App crashes with `MemoryError` or `Out of Memory`

**Solution**:
```bash
# Free up system memory
# Close unnecessary applications

# Reduce batch size in config.py
# Restart app

# Or run with limited memory
python -m streamlit run main.py --logger.level=warning
```

---

## Data Issues

### 17. CSV Import Errors

**Issue**: `Error parsing CSV` or `Column not found`

**Solution**:
1. Verify CSV format and headers
2. Ensure no special characters in column names
3. Check file encoding (should be UTF-8)
4. Verify data types match expectations

---

### 18. Model Loading Failed

**Issue**: `FileNotFoundError: models/trained_models/...` 

**Solution**:
1. Create directories:
   ```bash
   mkdir -p models/trained_models
   ```

2. Train models first:
   ```bash
   python src/models/train_yield_model.py
   python src/models/train_price_model.py
   ```

3. Verify files exist:
   ```bash
   ls models/trained_models/
   ```

---

## API Issues

### 19. API Connection Refused

**Issue**: `Connection refused` or `Cannot connect to localhost:5000`

**Solution**:
1. Verify Flask API is running:
   ```bash
   python src/api/app.py
   ```

2. Check firewall settings
3. Use correct URL: `http://localhost:5000`
4. Verify Flask is installed:
   ```bash
   pip install Flask flask-cors
   ```

---

### 20. CORS Issues

**Issue**: `CORS error` or `blocked by CORS policy`

**Solution**:
```bash
# Ensure flask-cors is installed
pip install flask-cors

# Verify app.py has CORS enabled
# Check line: CORS(app)
```

---

## Getting Help

### Debugging Steps

1. **Check Error Message**: Read the full error carefully
2. **Search Logs**:
   ```bash
   tail -f logs/app.log
   grep ERROR logs/app.log
   ```
3. **Check Dependencies**:
   ```bash
   pip list | grep streamlit
   ```
4. **Verify Paths**:
   ```bash
   pwd  # Current directory
   ls -la  # List files
   ```
5. **Test Imports**:
   ```bash
   python -c "import streamlit; print('OK')"
   ```

### If Issue Persists

1. Try fresh installation:
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```

2. Check Python version:
   ```bash
   python --version  # Should be 3.8+
   ```

3. Review SETUP_INSTRUCTIONS.md again
4. Check project README.md for additional info

---

## System-Specific Notes

### Windows Specific
- Use `venv\Scripts\activate` to activate virtual environment
- Use `where python` to verify environment
- May need Visual C++ Build Tools for some packages

### macOS Specific
- May need Xcode Command Line Tools:
  ```bash
  xcode-select --install
  ```
- Use `source venv/bin/activate` to activate

### Linux Specific
- Verify Python 3 is installed:
  ```bash
  python3 --version
  ```
- May need additional system dependencies:
  ```bash
  sudo apt-get install python3-dev python3-pip
  ```

---

**Still having issues? Check the full documentation in README.md and SETUP_INSTRUCTIONS.md**
