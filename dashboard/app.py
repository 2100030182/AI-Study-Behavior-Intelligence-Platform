import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AI Study Behavior Intelligence Platform",
    layout="wide"
)

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
# Load Dataset
# -------------------------

df = pd.read_csv(
    "data/processed_student_behavior_data.csv"
)

# -------------------------
# Title
# -------------------------

st.title("AI Study Behavior Intelligence Platform")

st.subheader(
    "Predict Productivity and Burnout Risk"
)

# -------------------------
# Input Layout
# -------------------------

col1, col2 = st.columns(2)

with col1:

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

with col2:

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
        input_data.drop(
            columns=["burnout_risk_score"]
        )
    )[0]

    # -------------------------
    # Show Predictions
    # -------------------------

    st.success(
        f"Predicted Productivity Score: "
        f"{round(productivity_prediction, 2)}"
    )

    st.warning(
        f"Predicted Burnout Level: "
        f"{burnout_prediction}"
    )

    # -------------------------
    # Smart Recommendations
    # -------------------------

    st.markdown("### 🧠 Smart Recommendations")

    recommendations = []

    if sleep_hours < 6:
        recommendations.append(
            "⚠️ Sleep is below recommended level. Try sleeping at least 7 hours."
        )

    if study_hours > 7:
        recommendations.append(
            "📚 Study hours are high. Consider reducing workload."
        )

    if break_minutes < 40:
        recommendations.append(
            "☕ Break time is low. Take breaks every 60–90 minutes."
        )

    if burnout_prediction == "High":
        recommendations.append(
            "🔥 High burnout risk detected. Reduce workload and improve rest."
        )

    if len(recommendations) == 0:

        st.success(
            "✅ Your study habits look healthy!"
        )

    else:

        for rec in recommendations:

            st.info(rec)

# -------------------------
# Divider
# -------------------------

st.markdown("---")

# -------------------------
# Visualization Section
# -------------------------

st.header("📊 Study Behavior Trends")

# Study Hours Trend

fig1, ax1 = plt.subplots()

ax1.plot(df["study_hours"])

ax1.set_title("Study Hours Trend")

ax1.set_xlabel("Days")

ax1.set_ylabel("Study Hours")

st.pyplot(fig1)

# -------------------------
# Productivity Distribution
# -------------------------

st.header("📈 Productivity Distribution")

fig2, ax2 = plt.subplots()

sns.histplot(
    df["productivity_score"],
    bins=20,
    ax=ax2
)

ax2.set_title(
    "Productivity Score Distribution"
)

st.pyplot(fig2)

# -------------------------
# Sleep vs Productivity
# -------------------------

st.header("😴 Sleep vs Productivity")

fig3, ax3 = plt.subplots()

sns.scatterplot(
    x=df["sleep_hours"],
    y=df["productivity_score"],
    ax=ax3
)

ax3.set_title(
    "Sleep Hours vs Productivity"
)

st.pyplot(fig3)