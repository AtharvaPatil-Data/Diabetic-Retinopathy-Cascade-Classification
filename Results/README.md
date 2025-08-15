## 📊 Results Overview

This section presents the performance of our models in three stages:  
1. **Five-Class Classification (Direct)**  
2. **Round 1 – Initial Cascade Stage**  
3. **Round 2 – Final Cascade Stage**

---

### **1️⃣ Five-Class Classification (Direct)**
In this stage, the models classify directly into all five DR severity levels without grouping.

**F1-Scores**  
![Five-Class F1 Scores](Results/five_class/f1_scores.png)  

**Precision & Recall Table**  
![Five-Class Precision Recall](Results/five_class/precision_recall.png)  

**Key Observations:**
- **ResNet50** achieved balanced performance across all classes.
- "No DR" class had the highest scores, while **Mild DR** was the most challenging.
- Performance imbalance across classes motivated the cascaded approach.

---

### **2️⃣ Round 1 – Initial Cascade Stage**
This round still classifies into all five classes, but is the **first stage** of the cascaded setup.  
The model outputs here are later grouped for Round 2 refinement.

**F1-Scores**  
![Round 1 F1 Scores](Results/Round1/f1_scores.png)  

**Precision & Recall Table**  
![Round 1 Precision Recall](Results/Round1/precision_recall.png)  

**Key Observations:**
- **ResNet50** consistently outperforms others in detecting Moderate, Severe, and Proliferative DR.
- **MobileNet** achieves higher scores for "No DR" but lower for advanced stages.
- Mild DR detection remains low across all models.

---

### **3️⃣ Round 2 – Final Cascade Stage**
In this stage:
- Early DR stages (0, 1, 2) are grouped and classified separately from advanced stages (3, 4).
- Advanced stage predictions are finalized at Stage 1.
- Grouped early stages are refined into No DR, Mild DR, and Moderate DR.

**F1-Scores**  
![Round 2 F1 Scores](Results/Round2/f1_scores.png)  

**Precision & Recall Table**  
![Round 2 Precision Recall](Results/Round2/precision_recall.png)  

**Key Observations:**
- All models perform exceptionally well for the grouped early stages (F1 ~0.97).
- **ResNet50** has the strongest performance for Severe DR and Proliferative DR.
- Cascading reduces class confusion and improves advanced stage detection.

