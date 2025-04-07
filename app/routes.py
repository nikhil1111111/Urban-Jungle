from fastapi import APIRouter
from pydantic import BaseModel
from app.models import predict_aqi_benefit
from app.database import save_tree_data

router = APIRouter()

class TreePlantRequest(BaseModel):
    latitude: float
    longitude: float
    tree_type: str = "Neem"
    num_trees: int = 1
    user_id: str

@router.post("/plant-tree/")
def plant_tree(data: TreePlantRequest):
    prediction = predict_aqi_benefit(data.latitude, data.longitude, data.tree_type, data.num_trees)
    save_tree_data(data.dict(), prediction)
    
    return {
        "message": f"{data.num_trees} {data.tree_type} tree(s) planted!",
        "location": {"lat": data.latitude, "lon": data.longitude},
        "predicted_aqi_benefit": prediction
    }
