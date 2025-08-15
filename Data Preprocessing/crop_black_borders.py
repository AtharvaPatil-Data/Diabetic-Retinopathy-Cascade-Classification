from PIL import Image
import os
import matplotlib.pyplot as plt
import glob
import cv2
import numpy as np
from tqdm import tqdm

def crop_image_from_gray(img,tol=7):
    """
    Crop out black borders
    https://www.kaggle.com/ratthachat/aptos-updated-preprocessing-ben-s-cropping
    """  
    
    if img.ndim ==2:
        mask = img>tol
        return img[np.ix_(mask.any(1),mask.any(0))]
    elif img.ndim==3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = gray_img>tol        
        check_shape = img[:,:,0][np.ix_(mask.any(1),mask.any(0))].shape[0]
        if (check_shape == 0):
            return img
        else:
            img1=img[:,:,0][np.ix_(mask.any(1),mask.any(0))]
            img2=img[:,:,1][np.ix_(mask.any(1),mask.any(0))]
            img3=img[:,:,2][np.ix_(mask.any(1),mask.any(0))]
            img = np.stack([img1,img2,img3],axis=-1)
        return img


def circle_crop(img):   
    """
    Create circular crop around image centre    
    """    
    
    img = cv2.imread(img)
    img = crop_image_from_gray(img)    
    
    height, width, depth = img.shape    
    
    x = int(width/2)
    y = int(height/2)
    r = np.amin((x,y))
    
    circle_img = np.zeros((height, width), np.uint8)
    cv2.circle(circle_img, (x,y), int(r), 1, thickness=-1)
    img = cv2.bitwise_and(img, img, mask=circle_img)
    img = crop_image_from_gray(img)
    
    return img


def crop_and_fill_images(input_dir, output_dir):
    """
    Crop and fill images in input_dir and save them in output_dir.
    """
    os.makedirs(output_dir, exist_ok=True)
    image_paths = glob.glob(input_dir + '/*.jpeg')
    for img_path in tqdm(image_paths, desc=f"Processing {input_dir}", unit="img"):
        img = circle_crop(img_path)
        img_name = os.path.basename(img_path)
        img_path = os.path.join(output_dir, img_name)
        cv2.imwrite(img_path, img)

    print(f"Completed processing: {input_dir}")


input_train_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/Datasets/diabeticRetinopathyResized/resized_train/resized_train'
output_train_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/drc/training/crop_and_fill'

# input_test_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/Datasets/aptos2019/test_images'
# output_test_dir = '/Users/abhiruppaul/Abhirup/DCU/Practicum/preprocessed_dataset/aptos/testing/crop_and_fill'

crop_and_fill_images(input_train_dir, output_train_dir)

