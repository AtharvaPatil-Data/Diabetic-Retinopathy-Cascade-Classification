# Model: Cascaded ResNet50

This folder contains the **Cascaded ResNet50 model implementation** for Diabetic Retinopathy classification.

---

## 📄 File
### `cascade_resnet50.ipynb`
**Purpose:**  
Implements the multi-stage cascaded classification framework described in the paper using **ResNet50** as the backbone at each stage.

**Key Features:**
- **Stage 1:**  
  Classifies images into **Grouped Early Stages (0, 1, 2)** vs **Advanced Stages (3, 4)**.
- **Stage 2:**  
  Further classifies advanced stage images into **Severe DR (3)** and **Proliferative DR (4)**.
- **Stage 3:**  
  Refines classification of grouped early stage images into **No DR (0)**, **Mild DR (1)**, and **Moderate DR (2)**.
- Supports **multiple pre-trained backbones** for comparison:
  - ResNet50
  - DenseNet201
  - MobileNetV2
  - AlexNet (custom implementation)
- **Generates and displays confusion matrices** for each cascade stage **inside the notebook**.

---

## 🚀 Usage
### In Google Colab:
1. Mount Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
