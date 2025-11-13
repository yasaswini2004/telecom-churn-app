import streamlit as st
import pandas as pd
import joblib

# Load the model and feature column order
svm_model = joblib.load("svm_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

st.title("📊 Telecom Customer Churn Prediction")
st.write("Fill in the customer details to predict whether the customer will churn or not.")

def user_input():
    Age = st.number_input("Age", min_value=18, max_value=90, value=30)
    Tenure = st.number_input("Tenure in Months", min_value=0, max_value=72, value=12)
    MonthlyCharge = st.number_input("Monthly Charge", min_value=0.0, max_value=200.0, value=70.0)
    Satisfaction = st.slider("Satisfaction Score", 1, 5, 3)
    OnlineSecurity = st.selectbox("Online Security (0 = No, 1 = Yes)", [0, 1])
    UnlimitedData = st.selectbox("Unlimited Data (0 = No, 1 = Yes)", [0, 1])
    ContractType = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])

    # Prepare dataframe for prediction
    df = pd.DataFrame({
        "Age": [Age],
        "Tenure_in_Months": [Tenure],
        "Monthly_Charge": [MonthlyCharge],
        "Satisfaction_Score": [Satisfaction],
        "Online_Security": [OnlineSecurity],
        "Unlimited_Data": [UnlimitedData],
        "Contract_Two Year": [1 if ContractType == "Two Year" else 0],
        "Contract_One Year": [1 if ContractType == "One Year" else 0]
        # Month-to-Month automatically becomes 0,0
    })

    # Ensure same column order as model training
    df = df.reindex(columns=feature_cols, fill_value=0)
    return df


input_df = user_input()

if st.button("Predict"):
    prediction = svm_model.predict(input_df)[0]
    if prediction == 1:
        st.error("❌ Customer is likely to CHURN")
    else:
        st.success("✔ Customer is likely to STAY")
