import pandas as pd
import os
import shutil
from tqdm import tqdm

# Paths
csv_path = '/Users/abhiruppaul/Abhirup/DCU/Practicum/Datasets/diabeticRetinopathyResized/trainLabels.csv'        # CSV with image and level
image_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/training/median_filter'      # Directory with all images
output_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/dataset_org'  # Output directory

# Ensure class directories exist
for i in range(5):  # Classes 0 to 4
    os.makedirs(os.path.join(output_dir, f'class_{i}'), exist_ok=True)

# Load CSV
df = pd.read_csv(csv_path)

# Move images to corresponding class folders
for _, row in tqdm(df.iterrows(), total=len(df), desc="Organizing images"):
    img_name = f"{row['image']}.jpeg"
    class_label = row['level']

    src_path = os.path.join(image_dir, img_name)
    dest_path = os.path.join(output_dir, f'class_{class_label}', img_name)

    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)  # Use shutil.move() to move instead of copy
    else:
        print(f"⚠️ Image not found: {src_path}")
