import os
import glob
import cv2
from tqdm import tqdm

def resize_image(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    image_paths = glob.glob(input_dir + '/*.jpeg')
    
    for img_path in tqdm(image_paths, desc=f"Resizing images in {input_dir}", unit="img"):
        img = cv2.imread(img_path)
        img = cv2.resize(img, (244, 244))
        img_name = os.path.basename(img_path)
        img_path = os.path.join(output_dir, img_name)
        cv2.imwrite(img_path, img)


input_train_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/training/crop_and_fill'
output_train_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/training/resize'

# input_test_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/aptos/testing/crop_and_fill'
# output_test_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/aptos/testing/resize'

resize_image(input_train_dir, output_train_dir)
# resize_image(input_test_dir, output_test_dir)