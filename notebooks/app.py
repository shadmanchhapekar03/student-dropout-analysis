import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('dropout_pipeline.pkl')

st.title("🎓 Student Dropout Prediction App")

# Input form
famsize_LE3 = st.selectbox("Family Size: Is your family size less than or equal to 3?", ["Yes", "No"])
gender = st.selectbox("Gender", ["Male", "Female"])
internet = st.selectbox("Do you have Internet access at home?", ["Yes", "No"])
studytime = st.slider("Weekly Study Time (hours)", 1, 20, 5)
absences = st.slider("Number of Absences", 0, 50, 3)
failures = st.slider("Number of Past Class Failures", 0, 4, 0)

# Encode inputs manually
input_data = pd.DataFrame([{
    'famsize_LE3': 1 if famsize_LE3 == "Yes" else 0,
    'gender': 1 if gender == "Male" else 0,
    'internet': 1 if internet == "Yes" else 0,
    'studytime': studytime,
    'absences': absences,
    'failures': failures
}])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ Student is at risk of dropping out.")
    else:
        st.success("✅ Student is not at risk of dropping out.")
