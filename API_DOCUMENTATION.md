# API Documentation

## Overview

The Agri-agent API provides REST endpoints for model predictions and recommendations. It's built with Flask and can be deployed independently or run alongside the Streamlit web interface.

## Getting Started

### Start the API Server
```bash
python src/api/app.py
```

Server runs at: `http://localhost:5000`

### Health Check
```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "healthy",
  "service": "agri-agent-api"
}
```

---

## API Endpoints

### 1. Yield Prediction

**Endpoint**: `POST /api/predict/yield`

**Content-Type**: `application/json`

**Request Body**:
```json
{
  "temperature": 25,
  "humidity": 60,
  "rainfall": 150,
  "soil_ph": 7.0,
  "nitrogen": 100,
  "phosphorus": 50,
  "potassium": 100,
  "days_to_harvest": 120
}
```

**Parameters**:
| Parameter | Type | Unit | Range | Required |
|-----------|------|------|-------|----------|
| temperature | float | °C | 0-50 | Yes |
| humidity | float | % | 0-100 | Yes |
| rainfall | float | mm | 0-500 | Yes |
| soil_ph | float | pH | 3.5-9.0 | Yes |
| nitrogen | float | kg/ha | 0-200 | Yes |
| phosphorus | float | kg/ha | 0-100 | Yes |
| potassium | float | kg/ha | 0-200 | Yes |
| days_to_harvest | int | days | 30-300 | Yes |

**Response**:
```json
{
  "status": "success",
  "prediction": {
    "yield": 8.5,
    "confidence": 0.85,
    "unit": "tons/ha"
  }
}
```

**Example cURL**:
```bash
curl -X POST http://localhost:5000/api/predict/yield \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 25,
    "humidity": 60,
    "rainfall": 150,
    "soil_ph": 7.0,
    "nitrogen": 100,
    "phosphorus": 50,
    "potassium": 100,
    "days_to_harvest": 120
  }'
```

**Example Python**:
```python
import requests

url = "http://localhost:5000/api/predict/yield"
data = {
    "temperature": 25,
    "humidity": 60,
    "rainfall": 150,
    "soil_ph": 7.0,
    "nitrogen": 100,
    "phosphorus": 50,
    "potassium": 100,
    "days_to_harvest": 120
}

response = requests.post(url, json=data)
result = response.json()
print(f"Predicted Yield: {result['prediction']['yield']} tons/ha")
print(f"Confidence: {result['prediction']['confidence']*100:.1f}%")
```

---

### 2. Price Prediction

**Endpoint**: `POST /api/predict/price`

**Content-Type**: `application/json`

**Request Body**:
```json
{
  "season": 1,
  "supply": 100,
  "demand": 50,
  "market_index": 100,
  "weather": 5,
  "transport_cost": 100,
  "inflation": 5.0,
  "days_since_harvest": 30
}
```

**Parameters**:
| Parameter | Type | Unit | Range | Required |
|-----------|------|------|-------|----------|
| season | int | - | 1-4 | Yes |
| supply | float | 1000 tons | 10-500 | Yes |
| demand | float | index | 0-100 | Yes |
| market_index | float | index | 50-150 | Yes |
| weather | int | code | 1-5 | Yes |
| transport_cost | float | index | 50-150 | Yes |
| inflation | float | % | 0-10 | Yes |
| days_since_harvest | int | days | 0-365 | Yes |

**Response**:
```json
{
  "status": "success",
  "prediction": {
    "price": 25000,
    "confidence": 0.82,
    "currency": "INR",
    "unit": "per_ton"
  }
}
```

**Example cURL**:
```bash
curl -X POST http://localhost:5000/api/predict/price \
  -H "Content-Type: application/json" \
  -d '{
    "season": 1,
    "supply": 100,
    "demand": 50,
    "market_index": 100,
    "weather": 5,
    "transport_cost": 100,
    "inflation": 5.0,
    "days_since_harvest": 30
  }'
```

---

### 3. Disease Detection

**Endpoint**: `POST /api/detect/disease`

**Content-Type**: `multipart/form-data`

**Request Parameters**:
- `image` (file, required): Image file (JPEG, PNG, BMP)

**Supported Formats**: JPEG, PNG, BMP
**Max File Size**: 10MB
**Image Size**: Recommended 224×224 or larger

**Response**:
```json
{
  "status": "success",
  "detection": {
    "disease": "Rust",
    "confidence": 0.92,
    "class_probabilities": [0.01, 0.92, 0.03, 0.04, ...]
  }
}
```

**Example cURL**:
```bash
curl -X POST http://localhost:5000/api/detect/disease \
  -F "image=@path/to/image.jpg"
```

**Example Python**:
```python
import requests

url = "http://localhost:5000/api/detect/disease"
files = {'image': open('crop_image.jpg', 'rb')}

response = requests.post(url, files=files)
result = response.json()
print(f"Disease: {result['detection']['disease']}")
print(f"Confidence: {result['detection']['confidence']*100:.1f}%")
```

---

### 4. Crop Recommendations

**Endpoint**: `POST /api/recommend/crops`

**Content-Type**: `application/json`

**Request Body**:
```json
{
  "soil_type": "Loam",
  "climate": "Temperate",
  "season": "Spring",
  "water_availability": "Moderate",
  "budget": "Moderate"
}
```

**Parameters**:
| Parameter | Type | Options | Required |
|-----------|------|---------|----------|
| soil_type | string | Sandy, Silt, Clay, Loam, Peat | Yes |
| climate | string | Tropical, Subtropical, Temperate, Arid, Mediterranean | Yes |
| season | string | Spring, Summer, Fall, Winter | Yes |
| water_availability | string | Very Low, Low, Moderate, High, Very High | Yes |
| budget | string | Very Limited, Limited, Moderate, Good, Excellent | Yes |

**Response**:
```json
{
  "status": "success",
  "recommendations": {
    "status": "success",
    "conditions": {
      "soil_type": "Loam",
      "climate": "Temperate",
      "season": "Spring",
      "water_availability": "Moderate",
      "budget": "Moderate"
    },
    "recommendations": "Based on your conditions, we recommend wheat, rice, and maize..."
  }
}
```

**Example cURL**:
```bash
curl -X POST http://localhost:5000/api/recommend/crops \
  -H "Content-Type: application/json" \
  -d '{
    "soil_type": "Loam",
    "climate": "Temperate",
    "season": "Spring",
    "water_availability": "Moderate",
    "budget": "Moderate"
  }'
```

**Example Python**:
```python
import requests

url = "http://localhost:5000/api/recommend/crops"
data = {
    "soil_type": "Loam",
    "climate": "Temperate",
    "season": "Spring",
    "water_availability": "Moderate",
    "budget": "Moderate"
}

response = requests.post(url, json=data)
result = response.json()
print(result['recommendations']['recommendations'])
```

---

## Error Handling

### Error Response Format
```json
{
  "status": "error",
  "message": "Invalid input: temperature out of range"
}
```

### Common HTTP Status Codes
| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Request processed successfully |
| 400 | Bad Request | Check request format and parameters |
| 404 | Not Found | Endpoint doesn't exist |
| 500 | Server Error | Check server logs |

### Error Examples

**Missing Required Field**:
```json
{
  "status": "error",
  "message": "Missing required parameter: temperature"
}
```

**Invalid Value**:
```json
{
  "status": "error",
  "message": "Invalid value for temperature: must be between 0 and 50"
}
```

**No Image Provided**:
```json
{
  "status": "error",
  "message": "No image provided"
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production use, add:

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/api/predict/yield', methods=['POST'])
@limiter.limit("10 per minute")
def predict_yield():
    # Implementation
```

---

## Authentication

Currently no authentication is required. For production:

```python
from functools import wraps
from flask import request

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if not api_key or api_key != os.getenv('API_KEY'):
            return {'status': 'error', 'message': 'Unauthorized'}, 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/predict/yield', methods=['POST'])
@require_api_key
def predict_yield():
    # Implementation
```

---

## CORS Configuration

CORS is enabled for all routes. To restrict:

```python
CORS(app, resources={
    r"/api/*": {"origins": "https://yourdomain.com"}
})
```

---

## Deployment

### Using Gunicorn (Production)
```bash
pip install gunicorn

gunicorn --workers 4 --bind 0.0.0.0:5000 src.api.app:app
```

### Using Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "src.api.app:app"]
```

Build and run:
```bash
docker build -t agri-agent-api .
docker run -p 5000:5000 -e OPENAI_API_KEY=sk-proj-... agri-agent-api
```

---

## Performance Metrics

### Average Response Times
| Endpoint | Time |
|----------|------|
| Health Check | ~50ms |
| Yield Prediction | ~150ms |
| Price Prediction | ~120ms |
| Disease Detection | ~500ms |
| Crop Recommendations | ~2-5s* |

*Depends on OpenAI API latency

### Recommended Configuration
- Workers: 4 (CPU cores)
- Timeout: 300 seconds
- Memory: 2GB minimum

---

## Code Examples

### JavaScript/Fetch API
```javascript
// Yield Prediction
fetch('http://localhost:5000/api/predict/yield', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    temperature: 25,
    humidity: 60,
    rainfall: 150,
    soil_ph: 7.0,
    nitrogen: 100,
    phosphorus: 50,
    potassium: 100,
    days_to_harvest: 120
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Python Requests
```python
import requests

# Base URL
BASE_URL = "http://localhost:5000/api"

# Yield Prediction
response = requests.post(f"{BASE_URL}/predict/yield", json={
    "temperature": 25,
    "humidity": 60,
    "rainfall": 150,
    "soil_ph": 7.0,
    "nitrogen": 100,
    "phosphorus": 50,
    "potassium": 100,
    "days_to_harvest": 120
})

print(response.json())
```

### cURL Batch Request
```bash
#!/bin/bash

# Process multiple predictions
for i in {1..5}; do
  curl -X POST http://localhost:5000/api/predict/yield \
    -H "Content-Type: application/json" \
    -d '{
      "temperature": 20,
      "humidity": 55,
      "rainfall": 140,
      "soil_ph": 6.8,
      "nitrogen": 90,
      "phosphorus": 45,
      "potassium": 95,
      "days_to_harvest": 115
    }' > result_$i.json
done
```

---

## Monitoring & Logging

### Enable Debug Logging
```bash
export FLASK_ENV=development
export FLASK_DEBUG=True
python src/api/app.py
```

### View Logs
```bash
tail -f logs/app.log
grep "ERROR" logs/app.log
```

### Health Monitoring
```bash
# Check API status
curl -v http://localhost:5000/api/health

# Monitor response time
time curl -X POST http://localhost:5000/api/predict/yield ...
```

---

## Support & Contributing

- Report bugs: GitHub Issues
- Documentation: See README.md
- Examples: Check `examples/` directory
- Contributing: Follow CONTRIBUTING.md

---

**API Version**: 1.0.0  
**Last Updated**: January 2026
