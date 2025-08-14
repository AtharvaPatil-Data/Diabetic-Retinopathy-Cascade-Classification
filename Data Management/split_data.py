import os
import shutil
import random
import pandas as pd
from tqdm import tqdm

# Paths
dataset_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/dataset_org'  # Folder containing class_0 to class_4
output_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/split_data'     # Where to save the split dataset

train_csv_path = os.path.join(output_dir, 'train_labels.csv')
test_csv_path = os.path.join(output_dir, 'test_labels.csv')

# Split ratio
train_ratio = 0.8

# Ensure output structure exists
for split in ['training', 'testing']:
    for i in range(5):  # Assuming classes 0 to 4
        os.makedirs(os.path.join(output_dir, split, f'class_{i}'), exist_ok=True)

# Initialize CSV data
train_csv_data = []
test_csv_data = []

# Split and copy images
for class_label in range(5):
    class_path = os.path.join(dataset_dir, f'class_{class_label}')
    images = os.listdir(class_path)

    # Shuffle images randomly
    random.shuffle(images)

    # Determine split point
    split_point = int(len(images) * train_ratio)
    train_images = images[:split_point]
    test_images = images[split_point:]

    # Helper function to copy and log images
    def process_images(image_list, split_name, csv_data):
        dest_folder = os.path.join(output_dir, split_name, f'class_{class_label}')
        for img in tqdm(image_list, desc=f"Processing class_{class_label} -> {split_name}"):
            src_path = os.path.join(class_path, img)
            dest_path = os.path.join(dest_folder, img)
            shutil.copy(src_path, dest_path)  # Use shutil.move() to move instead of copy

            # Add image name (without extension) and class to CSV
            img_name = os.path.splitext(img)[0]
            csv_data.append((img_name, class_label))

    # Process training and testing images
    process_images(train_images, 'training', train_csv_data)
    process_images(test_images, 'testing', test_csv_data)

# Save CSVs
pd.DataFrame(train_csv_data, columns=['image', 'level']).to_csv(train_csv_path, index=False)
pd.DataFrame(test_csv_data, columns=['image', 'level']).to_csv(test_csv_path, index=False)