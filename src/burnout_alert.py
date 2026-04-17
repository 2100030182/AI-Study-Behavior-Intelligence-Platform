import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "data/processed_student_behavior_data.csv"
)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# -------------------------
# Get Last 7 Days
# -------------------------

last_week = df.tail(7)

# -------------------------
# Check Burnout Risk
# -------------------------

high_burnout_days = last_week[
    last_week["burnout_risk_score"] > 0.6
]

sleep_deficit_days = last_week[
    last_week["sleep_deficit"] == 1
]

overstudy_days = last_week[
    last_week["study_hours"] > 7
]

# -------------------------
# Alert Logic
# -------------------------

print("\nBurnout Alert System")
print("----------------------")

if len(high_burnout_days) >= 3:
    print("⚠️ ALERT: High Burnout Risk Detected!")
    print(
        "Recommendation: Reduce workload and increase sleep."
    )

if len(sleep_deficit_days) >= 3:
    print("⚠️ ALERT: Sleep Deficit Detected!")
    print(
        "Recommendation: Aim for at least 7 hours sleep."
    )

if len(overstudy_days) >= 4:
    print("⚠️ ALERT: Overstudy Pattern Detected!")
    print(
        "Recommendation: Take regular breaks."
    )

if (
    len(high_burnout_days) < 3
    and len(sleep_deficit_days) < 3
    and len(overstudy_days) < 4
):
    print("✅ No major burnout risks detected.")

print("\nAlert system check completed.")