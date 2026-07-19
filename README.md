# Build ML REST API with FastAPI \| Student Score Prediction Project

In this episode of the MLOps series, we will expose our Machine Learning
model as a REST API using FastAPI.

## Topics Covered

-   Why ML models need APIs
-   Introduction to FastAPI
-   Project Structure
-   Creating `app.py`
-   Loading the trained model
-   Creating API endpoints
-   Testing APIs
-   Using Swagger UI
-   Testing predictions

## Project

**Student Score Prediction API**

## Why ML Models Need APIs

Examples: - Netflix movie recommendations - Amazon product suggestions -
Spotify music recommendations - Fraud detection systems - Student score
prediction

``` text
Frontend
   ↓
Backend
   ↓
ML API (FastAPI)
   ↓
Trained Model
   ↓
Prediction
```

## Project Structure

``` text
student-ml-project/

api/
   app.py

src/
   train.py
   predict.py

models/
   student_model.pkl

data/
   student_data.csv
```

## API Endpoints

### GET /

``` json
{
  "message": "Student ML API is running successfully!"
}
```

### GET /health

``` json
{
  "status": "UP"
}
```

### POST /predict

Request:

``` json
{
  "study_hours": 8,
  "sleep_hours": 6,
  "attendance": 90,
  "previous_marks": 75
}
```

Response:

``` json
{
  "predicted_score": 84.12
}
```

## Checkout the API Branch

``` bash
git checkout api_url
```

## Setup

``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the Application

``` bash
uvicorn api.app:app --reload
```

Open:

``` text
http://127.0.0.1:8000/docs
```

## API Summary

  Endpoint     Method   Description
  ------------ -------- -----------------------
  `/`          GET      Application status
  `/health`    GET      Health check endpoint
  `/predict`   POST     Predict student score

## Real World Use Cases

-   Netflix Recommendation Engine
-   Amazon Personalization
-   YouTube Recommendations
-   Banking Fraud Detection
-   Healthcare Prediction Systems

## Next Video

-   Dockerize the FastAPI application
-   Build a Docker image
-   Prepare for Kubernetes deployment

#MLOps #FastAPI #MachineLearning #DevOps #Kubernetes
