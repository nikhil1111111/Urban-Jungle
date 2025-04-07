# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from typing import Optional
# from app.models import predict_aqi_benefit

# app = FastAPI()

# # Request schema
# class TreePlantRequest(BaseModel):
#     latitude: float
#     longitude: float
#     tree_type: Optional[str] = "Neem"
#     num_trees: int = 1

# @app.get("/")
# def root():
#     return {"message": "Urban Jungle API is live!"}

# @app.post("/plant-tree/")
# def plant_tree(data: TreePlantRequest):
#     prediction = predict_aqi_benefit(data.latitude, data.longitude, data.tree_type, data.num_trees)
#     return {
#         "message": f"Planted {data.num_trees} {data.tree_type} trees!",
#         "location": {"lat": data.latitude, "lon": data.longitude},
#         "predicted_aqi_benefit": prediction
#     }

from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)

