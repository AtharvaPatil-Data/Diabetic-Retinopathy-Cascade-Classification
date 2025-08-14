# Diabetic Retinopathy Cascade Classification

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-TensorFlow%2FKeras-orange)]()
[![Medical Imaging](https://img.shields.io/badge/Domain-Medical%20Imaging-red)]()

## 📌 Overview
This project implements a **multi-stage cascaded deep learning framework** for **Diabetic Retinopathy (DR) classification** using pre-trained **ResNet50**.  
The approach enhances early and advanced stage detection accuracy by **grouping visually similar DR stages** and refining classification through multiple cascade steps.

The model was trained and evaluated using **two public datasets**:
- **APTOS 2019 Blindness Detection**
- **Diabetic Retinopathy Resized Dataset**

By combining datasets and applying a **Smooth Data Augmentation** strategy, this system addresses **class imbalance** and improves detection of subtle early-stage DR cases.

---

## ✨ Key Features
- **Cascaded ResNet50 Architecture** for multi-stage classification.
- **Dual dataset integration** for greater variability and robustness.
- **Structured data augmentation** (flip, brightness, saturation) to handle imbalance.
- **Detailed class-wise metrics** including F1-scores, precision, and recall.
- **Early-stage sensitivity** improvement for real-world screening.

---

## 📂 Dataset Documentation
- [📄 Raw Dataset README](Data/Raw/README.md) — Contains dataset sources and original class distribution (Table I).
- [📄 Processed Dataset README](Data/Processed/README.md) — Contains final training/testing counts after preprocessing and augmentation (Table II).
