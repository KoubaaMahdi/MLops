import requests
import streamlit as st
import pandas as pd
import datetime
import json
import os

# Get the backend URL from the environment variable
backend_url = os.getenv("BACKEND_URL", "http://localhost:8080")

# Title of the app
st.title("Mental Health Prediction Web App")
st.subheader("Enter details below to predict mental health risk")

# Creating the form for user input
with st.form("form1", clear_on_submit=False):
    # Input fields
    Age = st.number_input("Enter Age", min_value=0, max_value=120, value=35)
    Marital_Status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
    Education_Level = st.selectbox("Education Level", ["High School", "Associate Degree", "Bachelor's Degree", "Master's Degree", "PhD"])
    Number_of_Children = st.number_input("Number of Children", min_value=0, max_value=20, value=2)
    Smoking_Status = st.selectbox("Smoking Status", ["Non-smoker", "Former", "Current"])
    Physical_Activity_Level = st.selectbox("Physical Activity Level", ["Sedentary", "Moderate", "Active"])
    Employment_Status = st.selectbox("Employment Status", ["Employed", "Unemployed"])
    Income = st.number_input("Income (USD)", min_value=0.0, value=60000.0, step=1000.0)
    Alcohol_Consumption = st.selectbox("Alcohol Consumption", ["Low", "Moderate", "High"])
    Dietary_Habits = st.selectbox("Dietary Habits", ["Unhealthy", "Moderate", "Healthy"])
    Sleep_Patterns = st.selectbox("Sleep Patterns", ["Poor", "Fair", "Good"])
    History_of_Mental_Illness = st.selectbox("History of Mental Illness", ["Yes", "No"])
    History_of_Substance_Abuse = st.selectbox("History of Substance Abuse", ["Yes", "No"])
    Family_History_of_Depression = st.selectbox("Family History of Depression", ["Yes", "No"])
    Chronic_Medical_Conditions = st.selectbox("Chronic Medical Conditions", ["Yes", "No"])
    
    # Collect data in a dictionary
    input_data = {
        "Age": Age,
        "Marital_Status": Marital_Status,
        "Education_Level": Education_Level,
        "Number_of_Children": Number_of_Children,
        "Smoking_Status": Smoking_Status,
        "Physical_Activity_Level": Physical_Activity_Level,
        "Employment_Status": Employment_Status,
        "Income": Income,
        "Alcohol_Consumption": Alcohol_Consumption,
        "Dietary_Habits": Dietary_Habits,
        "Sleep_Patterns": Sleep_Patterns,
        "History_of_Mental_Illness": History_of_Mental_Illness,
        "History_of_Substance_Abuse": History_of_Substance_Abuse,
        "Family_History_of_Depression": Family_History_of_Depression,
        "Chronic_Medical_Conditions": Chronic_Medical_Conditions
    }

    # Submit button
    submit = st.form_submit_button("Submit this form")

    if submit:
        # Send data to the backend API
        try:
            response = requests.post(f"{backend_url}/predict", data=json.dumps(input_data))
            predictions = response.json().get("predictions")

            # Display the prediction result
            if predictions == [0]:
                st.success("The person is not at risk of mental illness.")
            elif predictions == [1]:
                st.warning("The person may be at risk of mental illness.")
            else:
                st.error("An error occurred while processing the prediction.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# File upload for historical CSV data
st.subheader("Or upload your historical data (CSV file)")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Send the file to the backend API
        file = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{backend_url}/predict/csv", files=file)
        predictions = response.json().get("predictions")

        # Display predictions for each record
        st.subheader("Predictions for uploaded data")
        for idx, prediction in enumerate(predictions, start=1):
            st.text(f"Record {idx}: {'At risk' if prediction == 1 else 'Not at risk'}")
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
