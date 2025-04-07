import firebase_admin
from firebase_admin import credentials, firestore
import datetime

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_tree_data(data: dict, prediction: dict):
    doc = {
        "user_id": data["user_id"],
        "location": {
            "latitude": data["latitude"],
            "longitude": data["longitude"]
        },
        "tree_type": data["tree_type"],
        "num_trees": data["num_trees"],
        "predicted_aqi_drop": prediction["estimated_aqi_drop"],
        "timestamp": datetime.datetime.utcnow()
    }
    db.collection("tree_plantings").add(doc)
