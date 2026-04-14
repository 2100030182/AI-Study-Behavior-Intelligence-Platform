import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

# Load processed dataset
df = pd.read_csv("data/processed_student_behavior_data.csv")

# Drop missing values
df = df.dropna()

# -----------------------------------
# Create Burnout Risk Label
# -----------------------------------

def categorize_burnout(score):
    if score < 0.3:
        return "Low"
    elif score < 0.6:
        return "Medium"
    else:
        return "High"

df["burnout_category"] = df["burnout_risk_score"].apply(
    categorize_burnout
)

# -----------------------------------
# Features (inputs)
# -----------------------------------

X = df[[
    "study_hours",
    "sleep_hours",
    "break_minutes",
    "focus_score",
    "study_7day_avg",
    "sleep_7day_avg",
    "productivity_7day_avg"
]]

# Target (what we predict)
y = df["burnout_category"]

# -----------------------------------
# Train/Test Split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------
# Create Model
# -----------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Burnout model trained successfully!")
print(f"Model Accuracy: {accuracy}")

# Save model
joblib.dump(model, "models/burnout_model.pkl")

print("Burnout model saved successfully!")