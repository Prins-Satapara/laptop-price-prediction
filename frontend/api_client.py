import requests


API_URL = "http://127.0.0.1:8000"

def check_api_health():
    
    try:
        response = requests.get(
            f"{API_URL}/health", 
            timeout=5
        )
        
        response.raise_for_status()
        data = response.json()
        
        return data.get("status") == "healthy"

    except requests.RequestException:
        return False
    

def get_model_info():

    try:

        response = requests.get(
            f"{API_URL}/model-info",
            timeout=5
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException:
        return None

def predict_laptop_price(laptop_data):

    response = requests.post(
        f"{API_URL}/predict",
        json=laptop_data,
        timeout=30
    )

    response.raise_for_status()

    return response.json()