# ai-service/tree_recommender.py
import tensorflow as tf
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

class TreeRecommender:
    def __init__(self):
        self.model = joblib.load('models/tree_recommender.pkl')
        self.tree_db = pd.read_csv('data/tree_database.csv')
        
    def recommend_trees(self, location, soil_type, sunlight):
        # Get climate zone from coordinates
        climate_zone = self.get_climate_zone(location['lat'], location['lng'])
        
        # Filter suitable trees
        suitable = self.tree_db[
            (self.tree_db['climate_zones'].str.contains(climate_zone)) &
            (self.tree_db['soil_preference'] == soil_type) &
            (self.tree_db['sunlight_needs'] <= sunlight)
        ]
        
        # Predict success probability
        features = suitable[['growth_rate', 'hardiness', 'water_needs']]
        suitable['success_prob'] = self.model.predict_proba(features)[:,1]
        
        return suitable.sort_values('success_prob', ascending=False).head(5)

    def get_climate_zone(self, lat, lng):
        # Simplified version - would use climate API in production
        if lat > 35: return 'temperate'
        elif lat < -35: return 'temperate'
        else: return 'tropical'