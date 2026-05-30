import os
import joblib
import pandas as pd

# =====================================
# PATHS
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "model"
)

# =====================================
# MODEL LOADERS
# =====================================

def load_model():

    return joblib.load(
        os.path.join(
            MODEL_DIR,
            "churn_model.pkl"
        )
    )


def load_encoders():

    return joblib.load(
        os.path.join(
            MODEL_DIR,
            "label_encoders.pkl"
        )
    )


def load_feature_columns():

    return joblib.load(
        os.path.join(
            MODEL_DIR,
            "feature_columns.pkl"
        )
    )


def load_feature_importance():

    return joblib.load(
        os.path.join(
            MODEL_DIR,
            "feature_importance.pkl"
        )
    )


def load_kmeans():

    return joblib.load(
        os.path.join(
            MODEL_DIR,
            "kmeans_model.pkl"
        )
    )


def load_scaler():

    return joblib.load(
        os.path.join(
            MODEL_DIR,
            "scaler.pkl"
        )
    )

# =====================================
# PREPROCESS INPUT
# =====================================

def preprocess_input(
    df,
    encoders,
    feature_columns
):

    df = df.copy()

    # Encode categorical columns

    for column, encoder in encoders.items():

        if column in df.columns:

            try:

                df[column] = encoder.transform(
                    df[column]
                )

            except:

                pass

    # Add missing columns

    for column in feature_columns:

        if column not in df.columns:

            df[column] = 0

    # Keep same order as training

    df = df[
        feature_columns
    ]

    return df

# =====================================
# RISK LEVEL
# =====================================

def risk_level(
    probability
):

    if probability < 0.30:

        return "Low Risk"

    elif probability < 0.70:

        return "Medium Risk"

    else:

        return "High Risk"

# =====================================
# REVENUE LOSS ESTIMATION
# =====================================

def revenue_loss_estimation(
    probability,
    monthly_charges
):

    annual_revenue = (
        monthly_charges * 12
    )

    expected_loss = (
        annual_revenue * probability
    )

    return round(
        expected_loss,
        2
    )
