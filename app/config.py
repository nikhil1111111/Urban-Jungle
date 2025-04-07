# API_KEY_GOOGLE_MAPS = "your_api_key_here"
# MODEL_PATH = "ml_models/air_quality_predictor.pkl"
import os
from dotenv import load_dotenv

load_dotenv()

FIREBASE_KEY_PATH = os.getenv("FIREBASE_KEY_PATH")
MODEL_PATH = os.getenv("MODEL_PATH")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
