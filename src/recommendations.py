import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/processed_student_behavior_data.csv"
)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Get last 7 days
last_week = df.tail(7)

print("\nSmart Recommendations")
print("----------------------")

# -------------------------
# Sleep Recommendation
# -------------------------

avg_sleep = last_week["sleep_hours"].mean()

if avg_sleep < 6:
    print("⚠️ Sleep is below recommended level.")
    print("➡️ Try sleeping at least 7 hours daily.\n")

# -------------------------
# Study Recommendation
# -------------------------

avg_study = last_week["study_hours"].mean()

if avg_study > 7:
    print("📚 Study hours are too high.")
    print("➡️ Consider reducing study load.\n")

elif avg_study < 3:
    print("📚 Study hours are too low.")
    print("➡️ Try maintaining consistent study time.\n")

# -------------------------
# Break Recommendation
# -------------------------

avg_break = last_week["break_minutes"].mean()

if avg_break < 40:
    print("☕ Break time is too low.")
    print("➡️ Take short breaks every 60–90 minutes.\n")

# -------------------------
# Burnout Recommendation
# -------------------------

high_burnout = last_week[
    last_week["burnout_risk_score"] > 0.6
].shape[0]

if high_burnout >= 3:
    print("🔥 High burnout risk detected.")
    print("➡️ Reduce workload and improve rest.\n")

# -------------------------
# Safe State Message
# -------------------------

if (
    avg_sleep >= 6
    and avg_study <= 7
    and avg_break >= 40
    and high_burnout < 3
):
    print("✅ Your study habits look healthy!")