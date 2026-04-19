import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table
)
from reportlab.lib.styles import getSampleStyleSheet

# Load dataset
df = pd.read_csv(
    "data/processed_student_behavior_data.csv"
)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Last 7 days
last_week = df.tail(7)

# Calculate metrics
avg_study = round(
    last_week["study_hours"].mean(),
    2
)

avg_sleep = round(
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
# Create PDF
# -------------------------

styles = getSampleStyleSheet()

document = SimpleDocTemplate(
    "data/weekly_report.pdf"
)

elements = []

# Title
elements.append(
    Paragraph(
        "Weekly Productivity Report",
        styles["Title"]
    )
)

elements.append(Spacer(1, 12))

# Table Data
table_data = [
    ["Metric", "Value"],
    ["Average Study Hours", avg_study],
    ["Average Sleep Hours", avg_sleep],
    ["Average Productivity", avg_productivity],
    ["Burnout Risk Days", burnout_days],
    ["Sleep Deficit Days", sleep_deficit_days]
]

table = Table(table_data)

elements.append(table)

# Build PDF
document.build(elements)

print("Weekly PDF report generated successfully!")``