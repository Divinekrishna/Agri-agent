# Gemini API Setup Guide

This guide explains how to set up and use Google's Gemini API with Agri-agent.

---

## Table of Contents
1. [Quick Setup](#quick-setup)
2. [Getting Gemini API Key](#getting-gemini-api-key)
3. [Configuration](#configuration)
4. [Installation](#installation)
5. [Troubleshooting](#troubleshooting)
6. [API Models Available](#api-models-available)

---

## Quick Setup

### Step 1: Get API Key
1. Visit https://aistudio.google.com/app/apikey
2. Click "Create API key in new project"
3. Copy the API key (starts with `AIza...`)

### Step 2: Add to .env
```bash
GEMINI_API_KEY=YOUR API KEY
```

### Step 3: Install Dependencies
```bash
pip install langchain-google-genai google-generativeai
```

### Step 4: Run Application
```bash
streamlit run main.py
```

---

## Getting Gemini API Key

### Method 1: Google AI Studio (Easiest)
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API key"
4. Select "Create API key in new project" or existing project
5. Copy the generated API key
6. ✅ Free tier available (rate-limited)

### Method 2: Google Cloud Console
1. Go to https://console.cloud.google.com
2. Create a new project (or select existing)
3. Enable "Generative Language API"
4. Go to "Credentials"
5. Create "API Key"
6. Copy the key
7. ✅ Paid tier available (more requests)

### API Key Format
```
AIzaSyD0mtvS6dq-0IXYgs6Kk65WUvCzjVQEVhQ
```
- Starts with `AIza`
- 39 characters total
- Keep it secret!

---

## Configuration

### Option 1: Environment Variable (.env)
```bash
# .env file
GEMINI_API_KEY=AIzaSyD0mtvS6dq-0IXYgs6Kk65WUvCzjVQEVhQ
```

### Option 2: System Environment Variable
**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY = "AIzaSyD0mtvS6dq-0IXYgs6Kk65WUvCzjVQEVhQ"
```

**macOS/Linux Bash:**
```bash
export GEMINI_API_KEY="AIzaSyD0mtvS6dq-0IXYgs6Kk65WUvCzjVQEVhQ"
```

### Option 3: Direct in Python (NOT RECOMMENDED)
```python
import os
os.environ["GEMINI_API_KEY"] = "AIzaSyD0mtvS6dq-0IXYgs6Kk65WUvCzjVQEVhQ"
```

### Verify Configuration
```bash
python -c "from config import GEMINI_API_KEY; print('OK' if GEMINI_API_KEY else 'NOT SET')"
```

---

## Installation

### Install Gemini Support
```bash
# Install required packages
pip install langchain-google-genai google-generativeai

# Or install from requirements
pip install -r requirements.txt
```

### Verify Installation
```python
python -c "from langchain_google_genai import ChatGoogleGenerativeAI; print('OK')"
```

### Full Setup
```bash
# Clone/navigate to project
cd c:\Users\losha\hackathon\Agri-agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Verify Gemini support
python -c "from langchain_google_genai import ChatGoogleGenerativeAI; print('OK')"

# Run application
streamlit run main.py
```

---

## Troubleshooting

### Issue: "GEMINI_API_KEY is not set"
**Solution:**
1. Check `.env` file exists in project root
2. Verify key is set: `GEMINI_API_KEY=AIza...`
3. Reload environment: Restart terminal/app
4. Check key format (starts with `AIza`)

### Issue: "LangChain Google Generative AI is not installed"
**Solution:**
```bash
pip install langchain-google-genai google-generativeai
```

### Issue: "API key invalid or unauthorized"
**Solution:**
1. Verify key is correct from https://aistudio.google.com/app/apikey
2. Check key has no extra spaces
3. Verify API is enabled in Google Cloud Console
4. Try generating new key
5. Check for special characters in key

### Issue: "Rate limit exceeded"
**Solution:**
- Free tier has limits (~60 requests/minute)
- Upgrade to paid tier for higher limits
- Add delays between requests:
```python
import time
time.sleep(1)  # 1 second delay
```

### Issue: "gemini-pro model not found"
**Solution:**
- Use alternative models:
  - `gemini-pro` (text only)
  - `gemini-pro-vision` (with images)
  - `gemini-1.5-pro` (latest)
  - `gemini-1.5-flash` (faster)

Update `src/utils/langchain_integration.py`:
```python
ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Use this model
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)
```

### Issue: "Connection timeout or network error"
**Solution:**
1. Check internet connection
2. Verify firewall isn't blocking Google API
3. Add retry logic:
```python
from tenacity import retry, wait_random_exponential, stop_after_attempt

@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(6))
def get_crop_recommendations(...):
    # Your code here
    pass
```

### Issue: "ImportError: cannot import name ChatGoogleGenerativeAI"
**Solution:**
```bash
# Upgrade packages
pip install --upgrade langchain-google-genai google-generativeai

# Or reinstall
pip uninstall langchain-google-genai google-generativeai -y
pip install langchain-google-genai google-generativeai
```

---

## API Models Available

### Text Generation
| Model | Speed | Quality | Cost | Use Case |
|-------|-------|---------|------|----------|
| `gemini-pro` | ⚡ Medium | 🌟🌟🌟 | 🆓 Free | General text |
| `gemini-1.5-pro` | ⚡ Slow | 🌟🌟🌟🌟 | 💰 Paid | Complex tasks |
| `gemini-1.5-flash` | ⚡⚡ Fast | 🌟🌟🌟 | 💰 Cheap | Quick responses |

### Vision (Image Analysis)
| Model | Description |
|-------|-------------|
| `gemini-pro-vision` | Analyze images with text |
| `gemini-1.5-pro-vision` | Advanced image understanding |
| `gemini-1.5-flash-vision` | Fast image processing |

### Usage in Code
```python
# Recommended for Agri-agent
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Fast & cheap
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)
```

---

## Features Supported

### ✅ Crop Recommendations
- Uses Gemini to analyze soil, climate, season, water
- Returns top 3 crop recommendations with details
- Provides fertilizer and harvest info

### ✅ Disease Advisory
- Uses Gemini to suggest disease management strategies
- Analyzes severity and affected area
- Provides prevention measures

### ✅ Structured Output
- Consistent response formatting
- Error handling with fallbacks
- Rate limiting support

---

## Security Best Practices

### ✅ DO
- Store key in `.env` file
- Add `.env` to `.gitignore`
- Use environment variables
- Keep key private
- Rotate keys periodically
- Use paid tier for production

### ❌ DON'T
- Hardcode key in Python files
- Share key in version control
- Commit `.env` to git
- Log API keys
- Use in public repositories
- Share key with others

### Example .gitignore
```gitignore
.env
.env.local
*.pth
__pycache__/
*.pyc
logs/
data/raw/
venv/
```

---

## Rate Limits & Quotas

### Free Tier
- 60 requests/minute
- ~1 million tokens/day
- Text-only models
- Suitable for: Development & testing

### Paid Tier
- 30 requests/second
- Unlimited tokens (pay per use)
- All models available
- Suitable for: Production

### Checking Usage
Go to https://aistudio.google.com/app/monitoring

---

## Advanced Configuration

### Custom Temperature
```python
# More creative responses (0.0 - 2.0)
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GEMINI_API_KEY,
    temperature=0.9  # More random
)
```

### Max Output Tokens
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GEMINI_API_KEY,
    max_output_tokens=500
)
```

### With Retry Logic
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def get_recommendation(crop_type):
    return get_crop_recommendations(...)
```

---

## Testing Gemini Integration

### Test 1: Import Check
```bash
python -c "from langchain_google_genai import ChatGoogleGenerativeAI; print('✅ OK')"
```

### Test 2: API Connection
```bash
python -c "
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY
llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=GEMINI_API_KEY)
print('✅ Connection successful')
"
```

### Test 3: Simple Query
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=GEMINI_API_KEY)
response = llm.invoke("What is the best crop for clay soil?")
print(response)
```

### Test 4: In Streamlit
```bash
streamlit run main.py
# Navigate to "Crop Recommendations" page
# Fill in form and click "Generate Recommendations"
# Should show AI-powered response
```

---

## Migration from OpenAI to Gemini

If you previously used OpenAI API:

### Changes Made
1. ✅ Updated imports: `langchain_google_genai` 
2. ✅ Updated config: Using `GEMINI_API_KEY` instead of `OPENAI_API_KEY`
3. ✅ Updated requirements.txt: Added `langchain-google-genai`
4. ✅ Updated initialize_llm(): Uses `ChatGoogleGenerativeAI`
5. ✅ Model selection: Using `gemini-pro` (can be changed)

### No Changes Needed
- ✅ LLMChain usage
- ✅ Prompt templates
- ✅ Response handling
- ✅ Error handling
- ✅ Streamlit pages

### Cost Comparison
| API | Cost | Notes |
|-----|------|-------|
| OpenAI GPT-3.5 | $0.0005/1K tokens | Stable pricing |
| OpenAI GPT-4 | $0.03/1K tokens | Higher quality |
| Gemini Free | Free | 60 req/min limit |
| Gemini Paid | $0.00075/1K input | Cheaper |

---

## Support & Resources

### Google AI Documentation
- https://ai.google.dev/docs
- https://ai.google.dev/tutorials/python_quickstart
- https://ai.google.dev/models/gemini

### LangChain Documentation
- https://python.langchain.com/docs/integrations/llms/google_generative_ai
- https://python.langchain.com/docs/modules/chains

### Community Support
- Stack Overflow: Tag `google-generativeai`
- GitHub Issues: langchain repo
- Google AI Community: ai.google.dev/community

---

## FAQ

**Q: Can I use Gemini instead of OpenAI?**
A: Yes! Gemini is now the default. It's cheaper and works great.

**Q: What if I want to go back to OpenAI?**
A: Update `langchain_integration.py` and install `langchain-openai`. See migration guide.

**Q: Is Gemini API free?**
A: Yes, free tier available with rate limits (60 req/min). Paid tier for more.

**Q: Which model should I use?**
A: Use `gemini-1.5-flash` for best balance of speed and cost.

**Q: How accurate are the recommendations?**
A: Depends on input quality. More detailed inputs = better recommendations.

**Q: Can I use Gemini for disease detection?**
A: Yes! Use `gemini-pro-vision` model with image inputs.

---

**Last Updated:** January 2026
**Gemini Integration Status:** ✅ Active

