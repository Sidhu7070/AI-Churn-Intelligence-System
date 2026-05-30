import plotly.express as px
import pandas as pd


# ==================================
# RISK CHART
# ==================================

def create_risk_chart(
    risk_score
):

    df = pd.DataFrame({

        "Metric":
            ["Risk Score"],

        "Value":
            [risk_score]

    })

    fig = px.bar(

        df,

        x="Metric",

        y="Value",

        title="Customer Churn Risk"

    )

    return fig


# ==================================
# FEATURE IMPORTANCE
# ==================================

def create_feature_importance_chart(
    feature_df
):

    fig = px.bar(

        feature_df.head(10),

        x="Importance",

        y="Feature",

        orientation="h",

        title="Top Features Affecting Churn"

    )

    return fig


# ==================================
# SHAP CHART
# ==================================

def create_shap_chart(
    shap_df
):

    fig = px.bar(

        shap_df,

        x="Impact",

        y="Feature",

        orientation="h",

        title="SHAP Explanation"

    )

    return fig