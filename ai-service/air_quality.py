# ai-service/air_quality.py
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from geopy.distance import geodesic

class AirQualityPredictor:
    def __init__(self):
        self.model = GradientBoostingRegressor()
        self.load_data()
        
    def load_data(self):
        self.trees = pd.read_csv('data/tree_locations.csv')
        self.air_stations = pd.read_csv('data/air_quality_stations.csv')
        self.model = joblib.load('models/air_quality_model.pkl')
    
    def predict_improvement(self, new_tree):
        # Find nearby trees and stations
        new_point = (new_tree['lat'], new_tree['lng'])
        
        # Calculate weighted influence of existing trees
        self.trees['distance'] = self.trees.apply(
            lambda x: geodesic(new_point, (x['lat'], x['lng'])).meters, axis=1)
        nearby_trees = self.trees[self.trees['distance'] < 500]  # 500m radius
        
        # Calculate features for prediction
        features = {
            'tree_count': len(nearby_trees) + 1,
            'avg_distance': nearby_trees['distance'].mean() if not nearby_trees.empty else 0,
            'tree_diversity': nearby_trees['type'].nunique(),
            'tree_size': new_tree.get('mature_size', 10)  # Default to medium tree
        }
        
        # Predict air quality improvement (µg/m³ reduction in PM2.5)
        improvement = self.model.predict([list(features.values())])[0]
        return max(0, min(improvement, 10))  # Cap between 0-10