# 📂 Processed Dataset Information

## Overview
This folder contains the **processed and augmented datasets** used for training and evaluation of the Diabetic Retinopathy Cascade Classification model.

The original datasets (**APTOS 2019** and **Diabetic Retinopathy Resized**) underwent:
1. **Preprocessing**:
   - Cropping to remove black borders.
   - Resizing images to **224×224** pixels.
   - Applying median filter to enhance small vascular structures.
2. **Smooth Data Augmentation**:
   - Horizontal flip
   - Vertical flip
   - Brightness enhancement
   - Saturation enhancement

This process was performed to:
- Address **class imbalance**.
- Improve **model generalization**.
- Increase dataset size for robust training.

---

## 📊 Dataset Distribution

### **Before and After Augmentation**

| Stage                | No DR  | Mild  | Moderate | Severe | PDR    |
|----------------------|--------|-------|----------|--------|--------|
| Original Dataset     | 27,615 | 2,813 | 6,291    | 1,066  | 1,003  |
| Training Before Aug. | 22,092 | 2,252 | 5,032    | 852    | 802    |
| Training After Aug.  | 27,615 | 27,615| 27,615   | 27,615 | 27,615 |
| Testing              | 5,523  | 563   | 1,259    | 214    | 201    |

> **Note:** Augmentation was applied **only on training data**, not on test data.

---

## 📂 Directory Structure
