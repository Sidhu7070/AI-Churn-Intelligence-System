import joblib
import pandas as pd


# ===============================
# LOAD MODEL
# ===============================

def load_model():

    return joblib.load(
        "../model/churn_model.pkl"
    )


# ===============================
# LOAD ENCODERS
# ===============================

def load_encoders():

    return joblib.load(
        "../model/label_encoders.pkl"
    )


# ===============================
# LOAD FEATURE COLUMNS
# ===============================

def load_feature_columns():

    return joblib.load(
        "../model/feature_columns.pkl"
    )


# ===============================
# LOAD FEATURE IMPORTANCE
# ===============================

def load_feature_importance():

    return joblib.load(
        "../model/feature_importance.pkl"
    )


# ===============================
# LOAD KMEANS
# ===============================

def load_kmeans():

    return joblib.load(
        "../model/kmeans_model.pkl"
    )


# ===============================
# LOAD SCALER
# ===============================

def load_scaler():

    return joblib.load(
        "../model/scaler.pkl"
    )


# ===============================
# RISK LEVEL
# ===============================

def risk_level(probability):

    score = probability * 100

    if score <= 30:

        return "Low Risk"

    elif score <= 70:

        return "Medium Risk"

    return "High Risk"


# ===============================
# REVENUE LOSS
# ===============================

def revenue_loss_estimation(
    probability,
    monthly_charges
):

    yearly_revenue = (
        monthly_charges * 12
    )

    loss = (
        probability
        *
        yearly_revenue
    )

    return round(
        loss,
        2
    )


# ===============================
# PREPROCESS INPUT
# ===============================

def preprocess_input(
    input_df,
    encoders,
    feature_columns
):

    for col in input_df.columns:

        if col in encoders:

            try:

                input_df[col] = (
                    encoders[col]
                    .transform(
                        input_df[col]
                    )
                )

            except:

                input_df[col] = 0

    for col in feature_columns:

        if col not in input_df.columns:

            input_df[col] = 0

    input_df = input_df[
        feature_columns
    ]

    return input_df