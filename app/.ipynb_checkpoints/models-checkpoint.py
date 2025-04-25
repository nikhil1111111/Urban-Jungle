def predict_aqi_benefit(lat, lon, tree_type="Neem", num_trees=1):
    """
    Dummy model for now — replace with trained ML later.
    """
    tree_impact = {
        "Neem": 0.75,
        "Peepal": 0.85,
        "Banyan": 0.9,
        "Other": 0.6
    }

    impact_factor = tree_impact.get(tree_type, 0.6)
    predicted_drop = round(num_trees * impact_factor, 2)
    return {
        "estimated_aqi_drop": predicted_drop,
        "tree_type": tree_type
    }
