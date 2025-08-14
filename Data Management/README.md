# Data Organise

This folder contains scripts to **arrange** and **split** the Diabetic Retinopathy dataset into the correct structure for preprocessing, augmentation, and model training.

---

## 📜 Scripts

### 1. `organise.py`
**Purpose:**  
Organizes raw dataset images into class-wise folders based on the label CSV file.

**How it works:**
- Reads the dataset CSV containing image IDs and corresponding DR class labels.
- Copies/moves images into class-specific subfolders:
