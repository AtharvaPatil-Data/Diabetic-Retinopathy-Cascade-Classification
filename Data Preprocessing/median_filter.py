from tqdm import tqdm
import os
import cv2
from glob import glob

def median_filter(input_dir, output_dir, kernel_size=5):
    os.makedirs(output_dir, exist_ok=True)
    image_files = glob(os.path.join(input_dir, "*.jpeg")) + glob(os.path.join(input_dir, "*.png"))

    for img_path in tqdm(image_files, desc=f"Denoising images in {input_dir}", unit="img"):
        img = cv2.imread(img_path)
        denoised_img = cv2.medianBlur(img, kernel_size)
        file_name = os.path.basename(img_path)
        output_path = os.path.join(output_dir, file_name)
        cv2.imwrite(output_path, denoised_img)

# Paths for input and output directories
input_train_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/training/resize'
output_train_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/training/median_filter'

# input_test_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/aptos/testing/resize'
# output_test_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/aptos/testing/median_filter'

# Apply denoising to train and test images
median_filter(input_train_dir, output_train_dir)
# median_filter(input_test_dir, output_test_dir)