import streamlit as st
import pickle

# Load model
model = pickle.load(open("stress_model.pkl", "rb"))

st.title("🧠 Stress Level Predictor")

# Inputs
sleep = st.slider("Sleep Hours", 0, 10, 5)
screen = st.slider("Screen Time", 0, 12, 6)
work = st.slider("Work Hours", 0, 12, 6)
activity = st.slider("Physical Activity", 0, 10, 3)

# Button
if st.button("Predict"):
    data = [[sleep, screen, work, activity]]
    prediction = model.predict(data)

    value = prediction[0]

    st.success(f"Stress Score: {round(value,2)}")

    if value <= 3:
        st.info("Low Stress 😊")
    elif value <= 6:
        st.warning("Medium Stress 😐")
    else:
        st.error("High Stress 😰")