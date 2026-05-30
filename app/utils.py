import joblib
import os
import shap
import reportlab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "model")


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
