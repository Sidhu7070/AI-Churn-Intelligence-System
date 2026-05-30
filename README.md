# AI-Powered Customer Churn Intelligence System

## Overview

The AI-Powered Customer Churn Intelligence System is a machine learning-based application designed to predict customer churn and provide actionable business insights. The project leverages a Random Forest Classifier to identify customers who are likely to leave a service and combines explainable AI, customer segmentation, revenue impact analysis, and retention recommendations within an interactive Streamlit dashboard.

This project demonstrates the practical application of machine learning in customer retention and business decision-making.

---

## Features

### Customer Churn Prediction

Predicts whether a customer is likely to churn or remain with the company.

### Risk Score Analysis

Provides churn probability and categorizes customers into:

* Low Risk
* Medium Risk
* High Risk

### Explainable AI (SHAP)

Explains why the model made a specific prediction by identifying the most influential features.

### Customer Segmentation

Uses K-Means clustering to categorize customers into different business segments:

* New Customer
* Loyal Customer
* Premium Customer
* At-Risk Customer

### Revenue Loss Estimation

Calculates potential annual revenue loss if a customer churns.

### Retention Recommendations

Generates business recommendations to help retain high-risk customers.

### Batch CSV Prediction

Allows prediction for multiple customers simultaneously through CSV upload.

### Feature Importance Dashboard

Visualizes the most important features affecting customer churn.

### PDF Report Generation

Generates a professional one-page business report summarizing prediction results and recommendations.

---

## Project Architecture

Customer Data
↓
Data Preprocessing
↓
Random Forest Model
↓
Churn Prediction
↓
Risk Analysis
↓
SHAP Explainability
↓
Customer Segmentation
↓
Revenue Loss Estimation
↓
Retention Recommendations
↓
PDF Report Generation

---

## Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* K-Means Clustering

### Explainable AI

* SHAP

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Web Application

* Streamlit

### Reporting

* ReportLab

### Model Persistence

* Joblib

---

## Dataset

Dataset Used:
IBM Telco Customer Churn Dataset

The dataset contains customer demographic information, service usage details, account information, and churn status.

Target Variable:

* Churn

---

## Project Structure

AI-Churn-Intelligence-System/
│
├── app/
│   ├── app.py
│   ├── utils.py
│   ├── retention.py
│   ├── shap_analysis.py
│   ├── visualizations.py
│   └── report_generator.py
│
├── dataset/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── model/
│   ├── churn_model.pkl
│   ├── label_encoders.pkl
│   ├── feature_columns.pkl
│   ├── feature_importance.pkl
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── train_model.py
├── train_kmeans.py
├── requirements.txt
├── README.md
└── .gitignore
---

## Installation

### Clone Repository

git clone <repository-url>

cd AI-Churn-Intelligence-System

### Install Dependencies

pip install -r requirements.txt

---

## Training Models

### Train Random Forest Model

python train_model.py

### Train K-Means Segmentation Model

python train_kmeans.py

---

## Run Application

streamlit run app/app.py

---

## Sample Output

### Churn Prediction

Prediction: Likely To Churn

Risk Score: 89%

Risk Level: High

### Customer Segment

At-Risk Customer

### Revenue Impact

Expected Annual Revenue Loss: $1174.80

### Retention Recommendations

* Offer Discount Plan
* Provide Loyalty Rewards
* Promote Annual Contract
* Offer Premium Service Trial

---

## Business Value

This project helps organizations:

* Identify customers at risk of leaving.
* Understand key churn drivers.
* Estimate potential revenue loss.
* Improve customer retention strategies.
* Support data-driven decision-making.

---

## Future Enhancements

* Deep Learning-based Churn Prediction
* Real-Time Prediction API
* Cloud Deployment
* Customer Lifetime Value Prediction
* Automated Email Retention Campaigns
* Advanced Customer Segmentation
* Interactive Executive Dashboard

---

## Author

Sidhant Mahadik

AI-Powered Customer Churn Intelligence System

Machine Learning | Data Analytics | Business Intelligence
