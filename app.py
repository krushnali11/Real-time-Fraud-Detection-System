import streamlit as st
import pickle
import numpy as np

# Load models
rf = pickle.load(open("rf_model.pkl", "rb"))
iso = pickle.load(open("iso_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("💳 Fraud Detection System")

amount = st.number_input("Transaction Amount")
time = st.slider("Time of Day", 0, 23)
device = st.slider("Device Score", 0.0, 1.0)
balance = st.number_input("Balance After Transaction")

if st.button("Check Fraud"):
    data = np.array([[amount, time, device, balance]])
    scaled = scaler.transform(data)

    rf_prob = rf.predict_proba(scaled)[0][1]
    iso_score = iso.decision_function(scaled)[0]

    final_score = 0.7 * rf_prob + 0.3 * (-iso_score)

    st.write("Fraud Probability:", round(rf_prob, 3))
    st.write("Risk Score:", round(final_score, 3))
