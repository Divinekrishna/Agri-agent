"""
Configuration settings for Agri-agent platform
"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Model paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models", "trained_models")
DISEASE_MODEL_PATH = os.path.join(MODEL_DIR, "disease_detection_model.pth")
YIELD_MODEL_PATH = os.path.join(MODEL_DIR, "yield_prediction_model.pkl")
PRICE_MODEL_PATH = os.path.join(MODEL_DIR, "price_prediction_model.pkl")

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///agri_agent.db")

# Streamlit config
STREAMLIT_CONFIG = {
    "page_icon": "🌾",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# ML Model parameters
DISEASE_DETECTION_CONFIDENCE_THRESHOLD = 0.7
YIELD_PREDICTION_CONFIDENCE_THRESHOLD = 0.75
PRICE_PREDICTION_CONFIDENCE_THRESHOLD = 0.8

# Crop types
CROP_TYPES = [
    "Wheat",
    "Maize",
    "Rice",
    "Soybeans",
    "Cotton",
    "Potato",
    "Tomato",
    "Sugarcane",
    "Coffee",
    "Tea",
]

# Soil types
SOIL_TYPES = ["Sandy", "Silt", "Clay", "Loam", "Peat"]

# Common crop diseases
CROP_DISEASES = {
    "Wheat": ["Rust", "Septoria", "Powdery Mildew", "Fusarium Head Blight"],
    "Maize": ["Gray Leaf Spot", "Northern Corn Leaf Blight", "Common Rust"],
    "Rice": ["Blast", "Sheath Blight", "Brown Spot"],
    "Tomato": ["Early Blight", "Late Blight", "Septoria Leaf Spot"],
    "Potato": ["Late Blight", "Early Blight", "Verticillium Wilt"],
}

# Feature scaling parameters
FEATURE_SCALING_PARAMS = {
    "temperature": {"min": 0, "max": 50},
    "humidity": {"min": 0, "max": 100},
    "rainfall": {"min": 0, "max": 500},
    "soil_ph": {"min": 3.5, "max": 9},
}
