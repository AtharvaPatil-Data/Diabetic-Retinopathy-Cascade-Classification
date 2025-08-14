# 📂 Dataset Information

## Overview
This project uses **two publicly available retinal fundus image datasets** for Diabetic Retinopathy (DR) classification:

1. **APTOS 2019 Blindness Detection**
2. **Diabetic Retinopathy Resized Dataset**

Both datasets classify DR into **five severity stages**:
- **0**: No DR
- **1**: Mild DR
- **2**: Moderate DR
- **3**: Severe DR
- **4**: Proliferative DR

Due to file size and licensing restrictions, the datasets **are not included** in this repository.  
Please download them from the official sources listed below.

---

## 📥 Dataset Sources

1. **APTOS 2019 Blindness Detection**  
   [https://www.kaggle.com/competitions/aptos2019-blindness-detection/data](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data)  
   - Contains **3,662 images**.
   - Captured under varied imaging conditions with clinician annotations.

2. **Diabetic Retinopathy Resized Dataset**  
   [https://www.kaggle.com/datasets/tanlikesmath/diabetic-retinopathy-resized](https://www.kaggle.com/datasets/tanlikesmath/diabetic-retinopathy-resized)  
   - Contains **35,126 images**.
   - Resized and preprocessed for easier training.

---

## 📊 Combined Dataset Class Distribution

| Class | Severity Level   | DRC   | APTOS  | Total   |
|-------|------------------|-------|--------|---------|
| 0     | No DR            | 1,805 | 25,810 | 27,615  |
| 1     | Mild DR          | 370   | 2,443  | 2,813   |
| 2     | Moderate DR      | 999   | 5,292  | 6,291   |
| 3     | Severe DR        | 193   | 873    | 1,066   |
| 4     | Proliferative DR | 295   | 708    | 1,003   |
| **—** | **Total**        | 3,662 | 35,126 | 38,788  |

---

## 📂 Directory Structure After Download
After downloading, your `data/` folder should look like this:
