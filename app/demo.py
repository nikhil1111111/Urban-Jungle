# # This version excludes Streamlit for environments where it's unavailable.
# # You can run this in a local Python environment with Streamlit installed.

# import pandas as pd
# import random
# from PIL import Image
# from io import BytesIO
# import base64

# # ---------------------------
# # Mock Tree CO2 Absorption Data
# # ---------------------------
# tree_data = {
#     "Neem": 30,  # kg CO2/year
#     "Peepal": 40,
#     "Banyan": 50,
#     "Mango": 35,
#     "Ashoka": 25
# }

# # ---------------------------
# # Mock Leaderboard (CSV backend)
# # ---------------------------
# def load_leaderboard():
#     try:
#         return pd.read_csv("leaderboard.csv")
#     except FileNotFoundError:
#         return pd.DataFrame(columns=["User", "Trees Planted", "CO2 Saved (kg)"])

# def update_leaderboard(user, co2):
#     df = load_leaderboard()
#     if user in df["User"].values:
#         df.loc[df["User"] == user, "Trees Planted"] += 1
#         df.loc[df["User"] == user, "CO2 Saved (kg)"] += co2
#     else:
#         df = pd.concat([df, pd.DataFrame({"User": [user], "Trees Planted": [1], "CO2 Saved (kg)": [co2]})], ignore_index=True)
#     df.to_csv("leaderboard.csv", index=False)
#     return df

# # ---------------------------
# # Extract EXIF Geolocation (mock for now)
# # ---------------------------
# def get_location_from_image(image):
#     # TODO: Use PIL + piexif to extract GPS info
#     return "Indore, MP"  # Mock location

# # ---------------------------
# # Mock Image Classifier (placeholder)
# # ---------------------------
# def is_tree_image(image):
#     return random.choice([True, True, False])  # 66% chance it's a tree

# # ---------------------------
# # CLI-style placeholder logic (if Streamlit is not available)
# # ---------------------------
# if __name__ == "__main__":
#     print("Welcome to Urban Jungle MVP CLI")
#     user = input("Enter your name: ")
#     print("Choose a tree species:")
#     for idx, species in enumerate(tree_data.keys()):
#         print(f"{idx + 1}. {species}")
#     species_choice = int(input("Enter choice (1-5): ")) - 1
#     tree_species = list(tree_data.keys())[species_choice]

#     image_path = input("Enter path to tree image (jpg/png): ")
#     try:
#         img = Image.open(image_path)
#         print("Image loaded successfully.")

#         if is_tree_image(img):
#             location = get_location_from_image(img)
#             co2_saved = tree_data[tree_species]
#             print(f"Tree Verified at {location}! You saved {co2_saved} kg CO₂/year 🌍")
#             leaderboard = update_leaderboard(user, co2_saved)
#         else:
#             print("Couldn't verify a tree in the image. Try again.")

#     except Exception as e:
#         print(f"Error loading image: {e}")

#     print("\nCommunity Leaderboard:")
#     leaderboard_df = load_leaderboard().sort_values(by="CO2 Saved (kg)", ascending=False)
#     print(leaderboard_df.to_string(index=False))

#     # Optional: Export leaderboard
#     leaderboard_df.to_csv("urban_jungle_leaderboard.csv", index=False)
#     print("\nLeaderboard saved to 'urban_jungle_leaderboard.csv'")






# Urban Jungle CLI (MVP without Streamlit)

import pandas as pd
import random
from PIL import Image
from utils.classifier import is_tree_image
from utils.geo_utils import get_location_from_image
from utils.leaderboard import update_leaderboard, load_leaderboard
from utils.tree_data import tree_data

if __name__ == "__main__":
    print("Welcome to Urban Jungle MVP CLI")
    user = input("Enter your name: ")
    print("Choose a tree species:")
    for idx, species in enumerate(tree_data.keys()):
        print(f"{idx + 1}. {species}")
    species_choice = int(input("Enter choice (1-5): ")) - 1
    tree_species = list(tree_data.keys())[species_choice]

    image_path = input("Enter path to tree image (jpg/png): ")
    try:
        img = Image.open(image_path)
        print("Image loaded successfully.")

        if is_tree_image(img):
            location = get_location_from_image(img)
            co2_saved = tree_data[tree_species]
            print(f"Tree Verified at {location}! You saved {co2_saved} kg CO₂/year 🌍")
            leaderboard = update_leaderboard(user, co2_saved)
        else:
            print("Couldn't verify a tree in the image. Try again.")

    except Exception as e:
        print(f"Error loading image: {e}")

    print("\nCommunity Leaderboard:")
    leaderboard_df = load_leaderboard().sort_values(by="CO2 Saved (kg)", ascending=False)
    print(leaderboard_df.to_string(index=False))

    leaderboard_df.to_csv("urban_jungle_leaderboard.csv", index=False)
    print("\nLeaderboard saved to 'urban_jungle_leaderboard.csv'")
