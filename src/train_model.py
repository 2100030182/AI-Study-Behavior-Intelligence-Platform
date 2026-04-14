import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import joblib

# Load processed dataset
df = pd.read_csv("data/processed_student_behavior_data.csv")

# Drop rows with missing values
df = df.dropna()

# Features (inputs)
X = df[[
    "study_hours",
    "sleep_hours",
    "break_minutes",
    "focus_score",
    "study_7day_avg",
    "sleep_7day_avg",
    "productivity_7day_avg",
    "burnout_risk_score"
]]

# Target (what we predict)
y = df["productivity_score"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print(f"Mean Absolute Error: {mae}")

# Save trained model
joblib.dump(model, "models/productivity_model.pkl")

print("Model saved successfully!")