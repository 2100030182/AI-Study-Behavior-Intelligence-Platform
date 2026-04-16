import pandas as pd

# Load processed dataset
df = pd.read_csv(
    "data/processed_student_behavior_data.csv"
)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# -------------------------
# Select Last 7 Days
# -------------------------

last_week = df.tail(7)

# -------------------------
# Calculate Metrics
# -------------------------

avg_study_hours = round(
    last_week["study_hours"].mean(),
    2
)

avg_sleep_hours = round(
    last_week["sleep_hours"].mean(),
    2
)

avg_productivity = round(
    last_week["productivity_score"].mean(),
    2
)

burnout_days = last_week[
    last_week["burnout_risk_score"] > 0.6
].shape[0]

sleep_deficit_days = last_week[
    last_week["sleep_deficit"] == 1
].shape[0]

# -------------------------
# Display Report
# -------------------------

print("\nWeekly Productivity Report")
print("----------------------------")

print(
    f"Average Study Hours: {avg_study_hours}"
)

print(
    f"Average Sleep Hours: {avg_sleep_hours}"
)

print(
    f"Average Productivity: {avg_productivity}"
)

print(
    f"Burnout Risk Days: {burnout_days}"
)

print(
    f"Sleep Deficit Days: {sleep_deficit_days}"
)

# -------------------------
# Save Report File
# -------------------------

report_data = {
    "Metric": [
        "Average Study Hours",
        "Average Sleep Hours",
        "Average Productivity",
        "Burnout Risk Days",
        "Sleep Deficit Days"
    ],
    "Value": [
        avg_study_hours,
        avg_sleep_hours,
        avg_productivity,
        burnout_days,
        sleep_deficit_days
    ]
}

report_df = pd.DataFrame(report_data)

report_df.to_csv(
    "data/weekly_report.csv",
    index=False
)

print("\nWeekly report saved successfully!")