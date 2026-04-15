import streamlit as st
import joblib
import pandas as pd

# -------------------------
# Load Models
# -------------------------

productivity_model = joblib.load(
    "models/productivity_model.pkl"
)

burnout_model = joblib.load(
    "models/burnout_model.pkl"
)

# -------------------------
# App Title
# -------------------------

st.title("AI Study Behavior Intelligence Platform")

st.subheader("Predict Productivity and Burnout Risk")

# -------------------------
# User Inputs
# -------------------------

study_hours = st.slider(
    "Study Hours",
    1.0, 10.0, 5.0
)

sleep_hours = st.slider(
    "Sleep Hours",
    3.0, 10.0, 6.0
)

break_minutes = st.slider(
    "Break Minutes",
    10, 180, 60
)

focus_score = st.slider(
    "Focus Score",
    1.0, 10.0, 7.0
)

study_7day_avg = st.slider(
    "7-Day Study Average",
    1.0, 10.0, 5.0
)

sleep_7day_avg = st.slider(
    "7-Day Sleep Average",
    3.0, 10.0, 6.0
)

productivity_7day_avg = st.slider(
    "7-Day Productivity Average",
    1.0, 10.0, 6.0
)

burnout_risk_score = st.slider(
    "Burnout Risk Score",
    0.0, 1.0, 0.3
)

# -------------------------
# Prediction Button
# -------------------------

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "study_hours": study_hours,
        "sleep_hours": sleep_hours,
        "break_minutes": break_minutes,
        "focus_score": focus_score,
        "study_7day_avg": study_7day_avg,
        "sleep_7day_avg": sleep_7day_avg,
        "productivity_7day_avg": productivity_7day_avg,
        "burnout_risk_score": burnout_risk_score
    }])

    # Productivity Prediction
    productivity_prediction = productivity_model.predict(
        input_data
    )[0]

    # Burnout Prediction
    burnout_prediction = burnout_model.predict(
        input_data.drop(columns=["burnout_risk_score"])
    )[0]

    # Show Results
    st.success(
        f"Predicted Productivity Score: "
        f"{round(productivity_prediction, 2)}"
    )

    st.warning(
        f"Predicted Burnout Level: "
        f"{burnout_prediction}"
    )