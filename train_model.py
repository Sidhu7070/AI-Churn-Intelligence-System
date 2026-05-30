import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =====================================
# CREATE MODEL DIRECTORY
# =====================================

os.makedirs("model", exist_ok=True)

# =====================================
# LOAD DATASET
# =====================================

DATA_PATH = (
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")

# =====================================
# DATA CLEANING
# =====================================

if "customerID" in df.columns:
    df.drop(
        "customerID",
        axis=1,
        inplace=True
    )

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df.dropna(inplace=True)

# =====================================
# LABEL ENCODING
# =====================================

label_encoders = {}

for col in df.columns:

    if df[col].dtype == object:

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(
            df[col]
        )

        label_encoders[col] = encoder

# =====================================
# FEATURES & TARGET
# =====================================

X = df.drop(
    "Churn",
    axis=1
)

y = df["Churn"]

feature_columns = X.columns.tolist()

# =====================================
# SAVE FEATURE COLUMNS
# =====================================

joblib.dump(
    feature_columns,
    "model/feature_columns.pkl"
)

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
)

# =====================================
# RANDOM FOREST MODEL
# =====================================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    min_samples_split=5,
    random_state=42
)

print("Training Started...")

model.fit(
    X_train,
    y_train
)

print("Training Completed")

# =====================================
# PREDICTION
# =====================================

y_pred = model.predict(
    X_test
)

# =====================================
# EVALUATION
# =====================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(
    round(
        accuracy * 100,
        2
    ),
    "%"
)

print("\nClassification Report")

print(
    classification_report(
        y_test,
        y_pred
    )
)

print("\nConfusion Matrix")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

# =====================================
# FEATURE IMPORTANCE
# =====================================

importance_df = pd.DataFrame({

    "Feature":
        X.columns,

    "Importance":
        model.feature_importances_

})

importance_df = (
    importance_df
    .sort_values(
        by="Importance",
        ascending=False
    )
)

print(
    "\nTop Important Features\n"
)

print(
    importance_df.head(10)
)

# =====================================
# SAVE EVERYTHING
# =====================================

joblib.dump(
    model,
    "model/churn_model.pkl"
)

joblib.dump(
    label_encoders,
    "model/label_encoders.pkl"
)

joblib.dump(
    importance_df,
    "model/feature_importance.pkl"
)

print(
    "\nModel Saved Successfully"
)