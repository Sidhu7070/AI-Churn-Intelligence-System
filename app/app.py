import streamlit as st
import pandas as pd
import joblib

from utils import (
    load_model,
    load_encoders,
    load_feature_columns,
    load_feature_importance,
    load_kmeans,
    load_scaler,
    preprocess_input,
    risk_level,
    revenue_loss_estimation
)

from retention import (
    churn_reason,
    retention_strategy
)

from shap_analysis import (
    get_shap_explanation
)

from visualizations import (
    create_risk_chart,
    create_feature_importance_chart,
    create_shap_chart
)

from report_generator import (
    generate_report
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Churn Intelligence System",
    layout="wide"
)

st.title(
    "AI-Powered Customer Churn Intelligence System"
)

st.markdown(
    """
    Predict churn, explain predictions,
    estimate revenue loss, segment customers,
    and generate reports.
    """
)

# =====================================
# LOAD MODELS
# =====================================

model = load_model()

encoders = load_encoders()

feature_columns = load_feature_columns()

feature_importance = load_feature_importance()

kmeans = load_kmeans()

scaler = load_scaler()

# =====================================
# CUSTOMER SEGMENTS
# =====================================

segments = {

    0: "New Customer",

    1: "Loyal Customer",

    2: "Premium Customer",

    3: "At-Risk Customer"
}

# =====================================
# SIDEBAR
# =====================================

st.sidebar.header(
    "Customer Information"
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior = st.sidebar.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.sidebar.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

phone_service = st.sidebar.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

contract = st.sidebar.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

monthly_charges = st.sidebar.slider(
    "Monthly Charges",
    0,
    150,
    70
)

total_charges = st.sidebar.slider(
    "Total Charges",
    0,
    10000,
    2000
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# =====================================
# INPUT DATAFRAME
# =====================================

input_df = pd.DataFrame({

    "gender":
        [gender],

    "SeniorCitizen":
        [senior],

    "Partner":
        [partner],

    "Dependents":
        [dependents],

    "tenure":
        [tenure],

    "PhoneService":
        [phone_service],

    "InternetService":
        [internet_service],

    "Contract":
        [contract],

    "MonthlyCharges":
        [monthly_charges],

    "TotalCharges":
        [total_charges],

    "PaymentMethod":
        [payment_method]

})

processed_df = preprocess_input(

    input_df.copy(),

    encoders,

    feature_columns
)

# =====================================
# PREDICTION BUTTON
# =====================================

if st.button(
    "Predict Churn"
):

    prediction = model.predict(
        processed_df
    )[0]

    probability = model.predict_proba(
        processed_df
    )[0][1]

    score = round(
        probability * 100,
        2
    )

    # ===============================
    # RESULT
    # ===============================

    st.subheader(
        "Prediction Result"
    )

    if prediction == 1:

        prediction_text = (
            "Likely To Churn"
        )

        st.error(
            prediction_text
        )

    else:

        prediction_text = (
            "Customer Will Stay"
        )

        st.success(
            prediction_text
        )

    # ===============================
    # RISK SCORE
    # ===============================

    st.metric(
        "Risk Score",
        f"{score}%"
    )

    risk = risk_level(
        probability
    )

    st.info(
        f"Risk Level: {risk}"
    )

    # ===============================
    # SEGMENTATION
    # ===============================

    cluster = kmeans.predict(

        scaler.transform([[
            tenure,
            monthly_charges,
            total_charges
        ]])

    )[0]

    segment = segments.get(
        cluster,
        "Unknown"
    )

    st.subheader(
        "Customer Segment"
    )

    st.success(
        segment
    )

    # ===============================
    # REVENUE LOSS
    # ===============================

    revenue_loss = (

        revenue_loss_estimation(

            probability,

            monthly_charges
        )

    )

    st.subheader(
        "Estimated Revenue Loss"
    )

    st.metric(
        "Expected Annual Loss",
        f"${revenue_loss}"
    )

    # ===============================
    # CHURN REASONS
    # ===============================

    reasons = churn_reason({

        "MonthlyCharges":
            monthly_charges,

        "tenure":
            tenure,

        "Contract":
            processed_df["Contract"][0],

        "TotalCharges":
            total_charges
    })

    st.subheader(
        "Possible Reasons"
    )

    for reason in reasons:

        st.write(
            "•",
            reason
        )

    # ===============================
    # RETENTION
    # ===============================

    strategies = retention_strategy({

        "MonthlyCharges":
            monthly_charges,

        "tenure":
            tenure,

        "Contract":
            processed_df["Contract"][0],

        "TotalCharges":
            total_charges
    })

    st.subheader(
        "Retention Strategies"
    )

    for item in strategies:

        st.write(
            "•",
            item
        )

    # ===============================
    # SHAP
    # ===============================

    st.subheader(
        "Why This Prediction?"
    )

    shap_df = get_shap_explanation(

        model,

        processed_df
    )

    st.dataframe(
        shap_df
    )

    shap_fig = create_shap_chart(
        shap_df
    )

    st.plotly_chart(
        shap_fig,
        use_container_width=True
    )

    # ===============================
    # RISK CHART
    # ===============================

    risk_fig = create_risk_chart(
        score
    )

    st.plotly_chart(
        risk_fig,
        use_container_width=True
    )

    # ===============================
    # FEATURE IMPORTANCE
    # ===============================

    st.subheader(
        "Feature Importance Dashboard"
    )

    feature_fig = (
        create_feature_importance_chart(
            feature_importance
        )
    )

    st.plotly_chart(
        feature_fig,
        use_container_width=True
    )

    # ===============================
    # PDF REPORT
    # ===============================

    st.markdown("---")
    
    st.subheader("📊 Generate Professional Report")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(
            """
            <div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; border-left: 4px solid #1f4788;'>
            <b>Download Comprehensive Report</b><br/>
            Generate a professionally formatted PDF report with all analysis insights.
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        pdf_file = generate_report(

        prediction_text,

        probability,

        risk,

        segment,

        revenue_loss,

        reasons,

        strategies
)

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(

                label="📥 Download PDF Report",

                data=file,

                file_name=
                "Churn_Analysis_Report.pdf",

                mime=
                "application/pdf",
                
                use_container_width=True
            )

# =====================================
# BATCH CSV PREDICTION
# =====================================

st.header(
    "Batch CSV Prediction"
)

uploaded_file = st.file_uploader(

    "Upload CSV File",

    type=["csv"]
)

if uploaded_file:

    batch_df = pd.read_csv(
        uploaded_file
    )

    try:

        processed_batch = (
            preprocess_input(

                batch_df.copy(),

                encoders,

                feature_columns
            )
        )

        batch_df[
            "Prediction"
        ] = model.predict(
            processed_batch
        )

        batch_df[
            "Probability"
        ] = model.predict_proba(
            processed_batch
        )[:, 1]

        st.success(
            "Prediction Completed"
        )

        st.dataframe(
            batch_df.head()
        )

        csv = batch_df.to_csv(
            index=False
        )

        st.download_button(

            "Download Results",

            csv,

            "batch_predictions.csv",

            "text/csv"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )