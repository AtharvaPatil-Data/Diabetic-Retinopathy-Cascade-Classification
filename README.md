# Diabetic Retinopathy Cascade Classification

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-TensorFlow%2FKeras-orange)]()
[![Medical Imaging](https://img.shields.io/badge/Domain-Medical%20Imaging-red)]()

---

## 📌 Overview
This project implements a **multi-stage cascaded deep learning framework** for **Diabetic Retinopathy (DR) classification** using a pre-trained **ResNet50** backbone.  
The approach improves both **early-stage** and **advanced-stage** DR detection by:
- Grouping visually similar DR stages.
- Refining classification in multiple cascade stages.

The model is trained and evaluated using **two public datasets**:
- **APTOS 2019 Blindness Detection**
- **Diabetic Retinopathy Resized Dataset**

By combining datasets and applying a **Smooth Data Augmentation** strategy, this system effectively addresses **class imbalance** and enhances detection of subtle early-stage DR cases.

---

## ✨ Key Features
- **Cascaded ResNet50 architecture** for staged DR classification.
- **Dual dataset integration** for increased diversity and robustness.
- **Structured augmentation pipeline** (flip, brightness, saturation) for class balancing.
- **Detailed evaluation metrics**: class-wise F1-scores, precision, and recall.
- **Improved early-stage sensitivity**, critical for real-world screening.

---

## 📂 Repository Structure

```plaintext
├── Augmentation/                # Data augmentation scripts
├── Data Management/              # Dataset organization & splitting
├── Data Preprocessing/           # Image preprocessing scripts
├── Data/                         
│   ├── Raw/                      # Raw dataset info (not actual data files)
│   │   └── README.md              # Dataset sources & original distribution
│   ├── Processed/                 # Processed dataset info
│       └── README.md              # Post-preprocessing & augmentation counts
├── Docs/                          # Full project report & documentation
├── Model/                         # Model training notebook/script
├── Results/                       # Performance metrics & visualizations
├── Weights/                       # Trained model weights (Google Drive link)
├── LICENSE
└── README.md
