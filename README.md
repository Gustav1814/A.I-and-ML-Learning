# 🧠 Scikit-Learn Learning Journey

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)

A hands-on, documented journey through **Machine Learning with Scikit-Learn** — from foundational concepts to real-world applications. Each notebook contains theory, code, and explanations written as I learn.

> **Why this repo?** I believe the best way to learn is by doing. Every notebook here represents concepts I've studied, implemented, and documented myself — not just copy-pasted tutorials.

---

## 📚 Learning Roadmap

| # | Topic | Key Concepts | Status |
|---|-------|-------------|--------|
| 01 | [Feature Scaling](./01-Feature-Scaling/) | Min-Max Normalization, Standardization (Z-score), Train-Test Split | ✅ Done |
| 02 | [Train-Test Split](./02-Train-Test-Split/) | Data Splitting, Stratify, Random State, Overfitting Prevention | ✅ Done |
| 03 | Linear Regression | Simple & Multiple Regression, Cost Function, Gradient Descent | 🔜 Coming Soon |
| 04 | Logistic Regression | Binary Classification, Sigmoid Function, Decision Boundary | 🔜 Coming Soon |
| 05 | Decision Trees & Random Forests | Entropy, Information Gain, Ensemble Methods | 🔜 Coming Soon |
| 06 | Support Vector Machines | Hyperplanes, Kernel Trick, Margin Optimization | 🔜 Coming Soon |
| 07 | K-Nearest Neighbors | Distance Metrics, Choosing K, Curse of Dimensionality | 🔜 Coming Soon |
| 08 | Clustering (K-Means) | Centroids, Elbow Method, Silhouette Score | 🔜 Coming Soon |
| 09 | Dimensionality Reduction (PCA) | Eigenvalues, Variance Explained, Component Selection | 🔜 Coming Soon |

---

## 🔬 What's Inside

### 01 — Feature Scaling
📓 [Open Notebook](./01-Feature-Scaling/feature_scaling.ipynb)

**Concepts covered:**
- **Why Feature Scaling matters** — how unscaled features bias model training
- **Min-Max Normalization** — rescaling features to [0, 1] using `MinMaxScaler`
- **Standardization (Z-score)** — centering features to mean=0, std=1 using `StandardScaler`
- **Train-Test Split** — proper data splitting with `train_test_split`
- **Best practice:** Fit scaler on training data only, then transform test data (avoiding data leakage)

**Datasets used:**
- `Placement_Data_Full_Class.csv` — Campus placement prediction (215 records)
- `Social_Network_Ads.csv` — Purchase prediction based on age & salary (400 records)

### 02 — Train-Test Split
📓 [Open Notebook](./02-Train-Test-Split/train_test_split.ipynb)

**Concepts covered:**
- **Why we split data** — preventing overfitting by evaluating on unseen data
- **Basic 80/20 split** — using `train_test_split` with `test_size` and `random_state`
- **Stratified splitting** — preserving class proportions with `stratify=y`
- **Effect of `test_size`** — comparing different split ratios
- **Reproducibility** — why `random_state` matters for consistent results

**Dataset used:**
- `Placement_Data_Full_Class.csv` — Campus placement prediction (215 records)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core language |
| **Pandas** | Data manipulation & analysis |
| **NumPy** | Numerical computing |
| **Scikit-Learn** | Machine learning algorithms & preprocessing |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical data visualization |
| **Jupyter Notebook** | Interactive coding environment |

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Scikit-Learn-Journey.git
cd Scikit-Learn-Journey

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook
```

---

## 📂 Project Structure

```
Scikit-Learn-Journey/
│
├── README.md                     # You are here
├── .gitignore                    # Files excluded from version control
├── requirements.txt              # Python dependencies
│
├── datasets/                     # All datasets in one place
│   ├── placement_data.csv
│   └── social_network_ads.csv
│
├── 01-Feature-Scaling/
│   └── feature_scaling.ipynb     # Normalization, Standardization, Train-Test Split
│
├── 02-Train-Test-Split/
│   └── train_test_split.ipynb    # Data splitting, Stratify, Random State
│
└── (more topics coming soon...)
```

---

## 📈 Progress

This is a living repository — I add new topics as I learn them. Star ⭐ the repo to follow along!

---

## 📝 License

This project is for educational purposes. Datasets are publicly available and used for learning only.
