import os
import joblib
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# =====================================
# CREATE MODEL DIRECTORY
# =====================================

os.makedirs(
    "model",
    exist_ok=True
)

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv(
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# =====================================
# CLEAN DATA
# =====================================

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df.dropna(inplace=True)

# =====================================
# SEGMENTATION FEATURES
# =====================================

features = df[[
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]]

# =====================================
# SCALING
# =====================================

scaler = StandardScaler()

scaled_data = scaler.fit_transform(
    features
)

# =====================================
# KMEANS MODEL
# =====================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

kmeans.fit(
    scaled_data
)

# =====================================
# SAVE MODELS
# =====================================

joblib.dump(
    kmeans,
    "model/kmeans_model.pkl"
)

joblib.dump(
    scaler,
    "model/scaler.pkl"
)

print(
    "KMeans Model Saved Successfully"
)