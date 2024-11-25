import streamlit as st
import pickle
import numpy as np

with open("admission_model.pkl", "rb") as f:
    admission_model = pickle.load(f)

with open("length_of_stay_model.pkl", "rb") as f:
    length_of_stay_model = pickle.load(f)

# Title and description
st.title("Patient Admission and Length of Stay Prediction")
st.write("""
This application predicts:
1. Whether a patient will be admitted.
2. The estimated length of stay (only if the patient is admitted).
""")

# Collect input data
st.sidebar.header("Patient Information")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
arrival_transport = st.sidebar.selectbox("Arrival Transport", ["Ambulance", "Walk-in", "Other"])
race = st.sidebar.selectbox("Race", ["WHITE", "BLACK/AFRICAN AMERICAN", "ASIAN", "HISPANIC/LATINO", "OTHER"])
temperature = st.sidebar.number_input("Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)
heart_rate = st.sidebar.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=80)
resp_rate = st.sidebar.number_input("Respiratory Rate", min_value=10, max_value=40, value=20)
o2_sat = st.sidebar.number_input("Oxygen Saturation (%)", min_value=70, max_value=100, value=98)
sbp = st.sidebar.number_input("Systolic BP (mmHg)", min_value=80, max_value=200, value=120)
dbp = st.sidebar.number_input("Diastolic BP (mmHg)", min_value=40, max_value=120, value=80)
pain = st.sidebar.slider("Pain Level", min_value=0, max_value=10, value=5)
acuity = st.sidebar.selectbox("Acuity Level", [1, 2, 3, 4, 5])

# Convert categorical features to numeric
gender = 1 if gender == "Male" else 0
race_mapping = {"WHITE": 0, "BLACK/AFRICAN AMERICAN": 1, "ASIAN": 2, "HISPANIC/LATINO": 3, "OTHER": 4}
arrival_transport_mapping = {"Ambulance": 0, "Walk-in": 1, "Other": 2}

race = race_mapping[race]
arrival_transport = arrival_transport_mapping[arrival_transport]

# Prepare input array
input_data = np.array([[age, gender, arrival_transport, race, temperature, heart_rate, resp_rate, o2_sat, sbp, dbp, pain, acuity]])

# Predict Admission
admission_prediction = None
if st.button("Predict Admission"):
    admission_prediction = admission_model.predict(input_data)
    if admission_prediction[0] == 1:
        st.write("Prediction: **Patient will be Admitted**")
    else:
        st.write("Prediction: **Patient will NOT be Admitted**")

# Show Length of Stay Button if Patient is Admitted
if admission_prediction is not None and admission_prediction[0] == 1:
    if st.button("Predict Length of Stay"):
        length_of_stay_prediction = length_of_stay_model.predict(input_data)
        st.write(f"Estimated Length of Stay: **{length_of_stay_prediction[0]:.1f} days**")
