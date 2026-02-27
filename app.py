import streamlit as st
import pandas as pd
import joblib

rf_model = joblib.load("random_forest_model.pkl")

st.set_page_config(page_title="Smart Retail Analytics", layout="wide")

st.title("🛒 Smart Retail Analytics Dashboard")
st.subheader("Predict High-Margin Product Purchase")

st.sidebar.header("Customer Details")

age = st.sidebar.slider("Age", 18, 70, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
city_tier = st.sidebar.selectbox("City Tier", ["Tier 1", "Tier 2", "Tier 3"])
income_level = st.sidebar.selectbox("Income Level", ["Low", "Medium", "High"])
avg_monthly_spend = st.sidebar.number_input("Average Monthly Spend", 500.0, 20000.0, 6000.0)
visit_frequency = st.sidebar.slider("Visit Frequency", 0, 15, 5)
preferred_category = st.sidebar.selectbox(
    "Preferred Category",
    ["Groceries", "Electronics", "Fashion", "Home", "Beauty"]
)
discount_usage_rate = st.sidebar.slider("Discount Usage Rate", 0.0, 1.0, 0.3)
loyalty_points = st.sidebar.number_input("Loyalty Points", 0, 10000, 2500)
last_purchase_days = st.sidebar.slider("Days Since Last Purchase", 1, 180, 30)
app_usage_minutes = st.sidebar.slider("Weekly App Usage Minutes", 5, 200, 60)
complaints_count = st.sidebar.slider("Complaints Count", 0, 10, 1)
product_view_count = st.sidebar.slider("Product View Count", 0, 50, 10)

if st.sidebar.button("Predict"):

    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "city_tier": city_tier,
        "income_level": income_level,
        "avg_monthly_spend": avg_monthly_spend,
        "visit_frequency": visit_frequency,
        "preferred_category": preferred_category,
        "discount_usage_rate": discount_usage_rate,
        "loyalty_points": loyalty_points,
        "last_purchase_days": last_purchase_days,
        "app_usage_minutes": app_usage_minutes,
        "complaints_count": complaints_count,
        "product_view_count": product_view_count
    }])

    # Feature Engineering
    input_data["engagement_score"] = (
        input_data["visit_frequency"] * 0.3 +
        input_data["app_usage_minutes"] * 0.4 +
        input_data["product_view_count"] * 0.3
    )

    input_data["value_score"] = (
        input_data["avg_monthly_spend"] * 0.6 +
        input_data["loyalty_points"] * 0.4
    )

    input_data["discount_dependency"] = input_data["discount_usage_rate"]

    input_data["complaint_rate"] = (
        input_data["complaints_count"] /
        (input_data["visit_frequency"] + 1)
    )

    input_data["recency_score"] = 1 / (
        input_data["last_purchase_days"] + 1
    )

    # Apply get_dummies
    input_data = pd.get_dummies(input_data)

    # Align with model features
    model_features = rf_model.feature_names_in_
    input_data = input_data.reindex(columns=model_features, fill_value=0)

    prediction = rf_model.predict(input_data)[0]
    probability = rf_model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success("Customer is likely to purchase high-margin product.")
    else:
        st.error("Customer is unlikely to purchase high-margin product.")
