from fastapi import FastAPI, HTTPException

from .schemas import LaptopInput, PredictionResponse
from .predictor import predict_price


app = FastAPI(
    title="Laptop Price Prediction API",
    description=(
        "Production-ready API for predicting "
        "laptop prices using Machine Learning."
    ),
    version="1.0.0"
)
    

@app.get("/")
def home():
    return {
        "message": "Laptop Price Prediction API is running!",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/model-info")
def model_info():
    return {
        "model": "Gradient Boosting Regressor",
        "version": "1.0.0",
        "framework": "scikit-learn",
        "task": "Regression",
        "target": "Laptop Price",
        "currency": "INR",
        "metrics": {
            "r2": 0.8961,
            "mae": 11043.35,
            "rmse": 18206.07
        }
    }
    

@app.post("/predict", response_model=PredictionResponse)
def predict(laptop: LaptopInput):

    try:

        prediction = predict_price(laptop)

        return {
            "predicted_price": prediction,
            "currency": "INR",
            "message": "Laptop price predicted successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )