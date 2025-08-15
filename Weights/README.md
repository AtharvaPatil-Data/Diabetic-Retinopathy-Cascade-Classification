# Model Weights

This folder contains the **trained model weights** for the Cascaded ResNet50 Diabetic Retinopathy classification framework and its comparison CNN backbones.  

Due to their large file sizes, the weights are **not stored in this repository**. Instead, they are hosted on Google Drive for easy access.

---

## 📥 Download Weights

🔗 **[Download All Model Weights from Google Drive](https://drive.google.com/drive/folders/1LBS1P6avymm-V-CukNqQJdO87qFuSVDD?usp=sharing)**  

After downloading, place the `.h5` files into the same folder structure shown below.

---

## 📂 Folder Structure

### 1. `round1_initial/`
Contains model weights from the **first stage of training**, where the models directly classify images into **five DR classes**:
- **0**: No DR
- **1**: Mild DR
- **2**: Moderate DR
- **3**: Severe DR
- **4**: Proliferative DR

**Files:**
- `alexnet_model_stage1.h5` — AlexNet backbone trained on 5-class classification.
- `densenet201_model_stage1.h5` — DenseNet201 backbone trained on 5-class classification.
- `mobilenetv2_model_stage1.h5` — MobileNetV2 backbone trained on 5-class classification.
- `resnet50_model_stage1.h5` — ResNet50 backbone trained on 5-class classification (**final chosen backbone** for cascaded stages due to superior performance).

---

### 2. `round2_cascaded/`
Contains model weights for the **second training stage** in the cascaded framework:
- Stage 1: Separates **early stages** (0, 1, 2) from **advanced stages** (3, 4).
- Stage 2: Further classifies the grouped early stages into **No DR**, **Mild DR**, and **Moderate DR**.

**Files:**
- `alexnet_group1_stage2.h5` — AlexNet backbone for early-stage DR classification.
- `densenet201_group1_stage2.h5` — DenseNet201 backbone for early-stage DR classification.
- `mobilenetv2_group1_stage2.h5` — MobileNetV2 backbone for early-stage DR classification.
- `resnet50_group1_stage2.h5` — ResNet50 backbone for early-stage DR classification (**final chosen backbone**).

---

## 📊 How These Weights Are Used

1. **Round 1 (Initial Classification)**  
   - All images are classified into the 5 DR classes in a single step.  
   - This step evaluates multiple backbones (AlexNet, DenseNet201, MobileNetV2, ResNet50) to determine the best performer.

2. **Round 2 (Cascaded Classification)**  
   - Early stages (0, 1, 2) are grouped together and separated from advanced stages (3, 4).  
   - Advanced stages are finalized at Stage 1.  
   - Grouped early stages are passed to a second model for finer classification into No DR, Mild DR, and Moderate DR.  
   - ResNet50 is the backbone used in the final cascaded framework.

---

## ⚠️ Important Notes
- **ResNet50** is the primary backbone used in the final cascaded model because it achieved the best balance of precision, recall, and F1-score in experiments.
- Weights are stored in `.h5` format and can be loaded using TensorFlow/Keras:
  ```python
  from tensorflow.keras.models import load_model
  
  # Example: Load Round 1 ResNet50 weights
  model = load_model('weights/round1_initial/resnet50_model_stage1.h5')
