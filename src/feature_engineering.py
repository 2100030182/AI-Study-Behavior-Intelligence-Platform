import pandas as pd

# Load dataset
df = pd.read_csv("data/student_behavior_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# -----------------------------
# Feature 1 — 7-Day Rolling Study Average
# -----------------------------
df["study_7day_avg"] = df["study_hours"].rolling(window=7).mean()

# -----------------------------
# Feature 2 — 7-Day Rolling Sleep Average
# -----------------------------
df["sleep_7day_avg"] = df["sleep_hours"].rolling(window=7).mean()

# -----------------------------
# Feature 3 — Productivity Trend
# -----------------------------
df["productivity_7day_avg"] = df["productivity_score"].rolling(window=7).mean()

# -----------------------------
# Feature 4 — Sleep Deficit Indicator
# -----------------------------
df["sleep_deficit"] = df["sleep_hours"].apply(
    lambda x: 1 if x < 6 else 0
)

# -----------------------------
# Feature 5 — Burnout Risk Score
# -----------------------------
df["burnout_risk_score"] = (
    df["sleep_deficit"] * 0.4 +
    (df["study_hours"] > 7).astype(int) * 0.3 +
    (df["break_minutes"] < 30).astype(int) * 0.3
)

# Save processed dataset
df.to_csv("data/processed_student_behavior_data.csv", index=False)

print("Feature engineering completed!")
print(df.head())