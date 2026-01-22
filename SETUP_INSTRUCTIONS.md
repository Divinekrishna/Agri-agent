# Agri-agent Setup Instructions

## Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- Git

## Step 1: Clone/Download Project
```bash
cd Agri-agent
```

## Step 2: Create Virtual Environment

### Using venv (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Using conda
```bash
conda create -n agri-agent python=3.9
conda activate agri-agent
```

## Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

If you face any issues with PyTorch installation on Windows, try:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## Step 4: Configure Environment Variables

### Create `.env` file
The `.env` file already exists in the project. You need to update it with your actual API keys:

```bash
# Copy the example (if needed)
cp .env.example .env
```

### Edit `.env` file
Open `.env` and update:

```env
# Replace with your actual OpenAI API key
OPENAI_API_KEY=sk-proj-your_actual_openai_api_key_here

# Database configuration (optional - uses SQLite by default)
DATABASE_URL=sqlite:///agri_agent.db

# Model directory
MODEL_DIR=./models/trained_models

# Logging level
LOG_LEVEL=INFO
```

## Step 5: Get Your OpenAI API Key

### How to get OpenAI API Key:
1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign up or log in to your OpenAI account
3. Click "Create new secret key"
4. Copy the key (you won't see it again!)
5. Paste it in your `.env` file:
   ```env
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
   ```

## Step 6: Verify Installation
```bash
# Test imports
python -c "import streamlit; import torch; import sklearn; print('All packages installed successfully!')"

# Check Python version
python --version

# Check virtual environment
which python  # macOS/Linux
where python  # Windows
```

## Step 7: Run the Application

### Run Streamlit App (Main UI)
```bash
streamlit run main.py
```
The app will open at `http://localhost:8501`

### Run Flask API (Backend)
```bash
python src/api/app.py
```
The API will run at `http://localhost:5000`

### Run Both (in separate terminals)
Terminal 1:
```bash
streamlit run main.py
```

Terminal 2:
```bash
python src/api/app.py
```

## Troubleshooting

### Issue: ModuleNotFoundError: No module named 'streamlit'
**Solution**: Ensure virtual environment is activated and dependencies are installed
```bash
# Activate venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt
```

### Issue: "OpenAI API key not found"
**Solution**: 
1. Verify `.env` file exists in project root
2. Check that `OPENAI_API_KEY=` is not empty
3. Ensure `.env` is in the same directory as `main.py`
4. Restart the Streamlit app after updating `.env`

### Issue: PyTorch installation fails
**Solution**: For CPU-only installation (faster)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

Or for GPU (CUDA 11.8):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Issue: "No module named 'langchain_openai'"
**Solution**: Install LangChain components
```bash
pip install langchain langchain-openai
```

### Issue: Streamlit cache permission denied
**Solution**: Clear Streamlit cache
```bash
streamlit cache clear
```

### Issue: Port already in use
**Solution**: Use different port
```bash
# For Streamlit
streamlit run main.py --server.port 8502

# For Flask API
python src/api/app.py --port 5001
```

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for LLM features | `sk-proj-...` |
| `DATABASE_URL` | Database connection string | `sqlite:///agri_agent.db` |
| `MODEL_DIR` | Directory for trained models | `./models/trained_models` |
| `LOG_LEVEL` | Logging verbosity | `INFO`, `DEBUG` |
| `FLASK_ENV` | Flask environment | `development`, `production` |
| `API_PORT` | Flask API port | `5000` |
| `STREAMLIT_THEME_BASE` | Streamlit theme | `light`, `dark` |

## File Structure After Setup
```
Agri-agent/
├── venv/                    # Virtual environment
├── src/
│   ├── pages/              # Streamlit pages
│   ├── models/             # ML models
│   ├── utils/              # Utilities
│   ├── data/               # Data processing
│   └── api/                # Flask API
├── models/trained_models/  # Trained model files (add after training)
├── logs/                   # Application logs
├── .env                    # Environment variables (private - not in git)
├── .env.example           # Template for .env
├── main.py                # Main Streamlit app
├── config.py              # Configuration
└── requirements.txt       # Dependencies
```

## Next Steps

1. **Train Models** (Optional):
   ```bash
   python src/models/train_yield_model.py
   python src/models/train_price_model.py
   ```

2. **Test the Application**:
   - Open Streamlit app at `http://localhost:8501`
   - Try each feature from the sidebar

3. **Check API**:
   ```bash
   curl http://localhost:5000/api/health
   ```

4. **View Logs**:
   ```bash
   tail -f logs/app.log
   ```

## Security Notes

⚠️ **Important:**
- Never commit `.env` file to version control
- Never share your OpenAI API key
- Use `.gitignore` to exclude sensitive files
- Rotate API keys regularly
- Use environment-specific configurations for production

## Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review error messages carefully
3. Check logs in `logs/app.log`
4. Ensure all dependencies are installed correctly
5. Make sure virtual environment is activated

## Getting Help

If you encounter issues not listed above:
1. Check the error message carefully
2. Search GitHub issues for similar problems
3. Review the requirements.txt for version compatibility
4. Try `pip install --upgrade -r requirements.txt`

---

**Happy farming with Agri-agent! 🌾**
