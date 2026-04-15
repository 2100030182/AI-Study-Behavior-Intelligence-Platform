import joblib
import pandas as pd

# Load trained models
productivity_model = joblib.load(
    "models/productivity_model.pkl"
)

burnout_model = joblib.load(
    "models/burnout_model.pkl"
)

# ---------------------------------
# Example Input Data
# ---------------------------------

new_data = {
    "study_hours": 5,
    "sleep_hours": 6,
    "break_minutes": 60,
    "focus_score": 8,
    "study_7day_avg": 5.5,
    "sleep_7day_avg": 6.5,
    "productivity_7day_avg": 6.0,
    "burnout_risk_score": 0.4
}

# Convert to DataFrame
input_df = pd.DataFrame([new_data])

# ---------------------------------
# Productivity Prediction
# ---------------------------------

productivity_prediction = productivity_model.predict(
    input_df
)

# ---------------------------------
# Burnout Prediction
# ---------------------------------

burnout_prediction = burnout_model.predict(
    input_df.drop(columns=["burnout_risk_score"])
)

# ---------------------------------
# Output Results
# ---------------------------------

print("Prediction Results")
print("-------------------")

print(
    f"Predicted Productivity Score: "
    f"{round(productivity_prediction[0], 2)}"
)

print(
    f"Predicted Burnout Level: "
    f"{burnout_prediction[0]}"
)