# Preprocessing

This folder contains scripts to prepare raw dataset images before augmentation and model training.  
The preprocessing steps improve **image quality**, **uniformity**, and **focus on relevant retinal structures**.

---

## 📜 Scripts

### 1. `crop_black_borders.py`
**Purpose:**  
Removes black borders from retinal fundus images and centers the retina in the frame.

**How it works:**
- Detects the circular retinal region.
- Crops out unnecessary black edges.
- Saves cleaned images to the output directory.

---

### 2. `resize_images.py`
**Purpose:**  
Resizes all images to the **224×224** resolution required by ResNet50 and other CNN backbones.

**How it works:**
- Reads each image from the source folder.
- Resizes to fixed dimensions (224×224) while maintaining aspect ratio.
- Saves resized images to output directory.

---

### 3. `apply_median_filter.py`
**Purpose:**  
Enhances small retinal features (microaneurysms, hemorrhages) by reducing noise.

**How it works:**
- Applies a **3×3 median filter** to smooth out noise.
- Preserves important edge details for medical diagnosis.

---

## 🚀 Recommended Execution Order
Run the scripts in this order for best results:
1. `crop_black_borders.py`
2. `resize_images.py`
3. `apply_median_filter.py`


