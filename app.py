import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
model = load('random_forest_model.joblib')

# Title of the app
st.title("Loan Approval Prediction")

# Collect input data from the user
person_age = st.number_input("Age", min_value=18, max_value=100)
person_gender = st.selectbox("Gender", ["male", "female"])
person_education = st.selectbox("Education", ["High School", "Associate", "Bachelor", "Master", "Doctorate"])
person_income = st.number_input("Income", min_value=0.0)
person_emp_exp = st.number_input("Years of Employment Experience", min_value=0)
person_home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE", "OTHER"])
loan_amnt = st.number_input("Loan Amount", min_value=0.0)
loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "VENTURE", "EDUCATION", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION", "MEDICAL"])
loan_int_rate = st.number_input("Interest Rate", min_value=0.0)
loan_percent_income = st.number_input("Loan Percent Income", min_value=0.0)
cb_person_cred_hist_length = st.number_input("Credit History Length", min_value=0.0)
previous_loan_defaults_on_file = st.selectbox("Previous Loan Defaults on File", ["No", "Yes"])

# Dictionary to encode categorical inputs as numbers, similar to training
input_data = {
    "person_age": person_age,
    "person_gender": 0 if person_gender == "female" else 1,
    "person_education": {"High School": 0, "Associate": 1, "Bachelor": 2, "Master": 3, "Doctorate": 4}[person_education],
    "person_income": person_income,
    "person_emp_exp": person_emp_exp,
    "person_home_ownership": {"RENT": 0, "OWN": 1, "MORTGAGE": 2, "OTHER": 3}[person_home_ownership],
    "loan_amnt": loan_amnt,
    "loan_intent": {"PERSONAL": 0, "VENTURE": 1, "EDUCATION": 2, "HOMEIMPROVEMENT": 3, "DEBTCONSOLIDATION": 4, "MEDICAL": 5}[loan_intent],
    "loan_int_rate": loan_int_rate,
    "loan_percent_income": loan_percent_income,
    "cb_person_cred_hist_length": cb_person_cred_hist_length,
    "previous_loan_defaults_on_file": 0 if previous_loan_defaults_on_file == "No" else 1,
}

# Convert the input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Predict loan approval
if st.button("Predict"):
    prediction = model.predict(input_df)
    result = "Approved" if prediction[0] == 1 else "Not Approved"
    st.write(f"Loan Status: {result}")
