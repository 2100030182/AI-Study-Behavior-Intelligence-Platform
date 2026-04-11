import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Number of days (6 months)
num_days = 180

# Start date
start_date = datetime(2025, 1, 1)

data = []

for i in range(num_days):

    date = start_date + timedelta(days=i)

    # Generate realistic values
    study_hours = round(np.random.uniform(1, 8), 2)
    sleep_hours = round(np.random.uniform(4, 9), 2)
    break_minutes = round(np.random.uniform(20, 120), 0)

    focus_score = round(np.random.uniform(5, 10), 2)

    productivity_score = round(
        (study_hours * 0.5 +
         sleep_hours * 0.3 +
         focus_score * 0.2),
        2
    )

    data.append([
        date,
        study_hours,
        sleep_hours,
        break_minutes,
        focus_score,
        productivity_score
    ])

# Create DataFrame
columns = [
    "date",
    "study_hours",
    "sleep_hours",
    "break_minutes",
    "focus_score",
    "productivity_score"
]

df = pd.DataFrame(data, columns=columns)

# Save dataset
df.to_csv("data/student_behavior_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())