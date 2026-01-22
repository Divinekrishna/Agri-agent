# Agri-agent: AI-Powered Agriculture Platform

## Overview
An intelligent web platform for smart and sustainable agriculture using Python and Streamlit. Provides AI-powered crop recommendations, yield prediction, disease detection, price prediction, analytics dashboard, and farmer collaboration features.

## Project Structure
```
├── main.py                     # Main Streamlit app entry point
├── config.py                   # Configuration settings
├── pages/                      # Streamlit page modules
│   ├── pages_2_crop_recommendations.py
│   ├── pages_3_yield_prediction.py
│   ├── pages_4_disease_detection.py
│   ├── pages_5_price_prediction.py
│   ├── pages_6_analytics_dashboard.py
│   └── pages_7_collaboration.py
├── src/                        # Source modules
├── models/trained_models/      # Pre-trained ML model storage
├── requirements.txt            # Python dependencies
└── .env                        # Environment variables
```

## Running the Application
The application runs as a Streamlit web app on port 5000:
```bash
streamlit run main.py --server.port 5000 --server.address 0.0.0.0 --server.headless true
```

## Features
- Crop Recommendations: AI-powered suggestions based on soil, climate, and conditions
- Yield Prediction: ML-based forecasting for crop yields
- Disease Detection: Image upload for crop disease identification
- Price Prediction: Market price forecasting
- Analytics Dashboard: Real-time farming metrics and insights
- Collaboration: Community forum, expert network, and resources

## Tech Stack
- Python 3.11
- Streamlit (web framework)
- Pandas, NumPy, scikit-learn (data/ML)
- Plotly, Seaborn, Matplotlib (visualization)
- PIL/Pillow (image processing)

## Environment Variables
- `GEMINI_API_KEY` - Optional API key for AI features

## Recent Changes
- January 2026: Initial setup for Replit environment
- Created page modules for all features
- Configured Streamlit to run on port 5000
