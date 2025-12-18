import streamlit as st
import pandas as pd
import numpy as np
import pickle


model = pickle.load(open("kidney_model.pkl", "rb"))

st.set_page_config(page_title="Kidney Disease Prediction", layout="centered")

st.title("Kidney Disease Prediction App")
st.write("Enter patient details to predict Chronic Kidney Disease")

# ---- Input Fields ----
NAME = st.text_input("ENTER YOUR NAME")
st.write(NAME)

DETAILS = st.subheader("Enter Patient Details")



Age = st.number_input("Age", 0, 120)
Creatinine_Level = st.number_input("Creatinine Level", 0.1, 5.0)
BUN = st.number_input("Bun", 5.0,100.0)
Diabetes = st.selectbox("Diabetes", [0,1])
Hypertension = st.selectbox("Hypertension",[0,1])
GFR = st.number_input("Gfr", 1.0,150.0)
Urine_Output = st.number_input("Urine Output", 100.0, 3000.0)


# ---- Prediction ----


if st.button("predict"):
    input_data = pd.DataFrame([[Age, Creatinine_Level, BUN, Diabetes, Hypertension, GFR, Urine_Output]], columns=["Age", "Creatinine_Level", "BUN", "Diabetes", "Hypertension", "GFR", "Urine_Output"])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Patient is **Likely to have kidney Disease**")
    
    else:
        st.success("Patient Likely has **NO Chronic Kidney Disease**")