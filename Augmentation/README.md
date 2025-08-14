# Smooth Data Augmentation

This module implements the **deterministic, sequential augmentation** pipeline used in the project to balance classes and improve generalization.

**Script:** `smooth_augmentation.py`  
**Applies (in order):** Horizontal flip → Vertical flip → Brightness enhance → Saturation enhance  
**Scope:** Training split only (test set is never augmented)

---

## ✅ What it does
- Reads images from a class‑wise folder structure.
- Applies the *same* fixed sequence of operations to each image.
- Saves augmented images into **the same class folder** with suffixes for traceability.

---
