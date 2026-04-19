import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA

# -------------------------
# Load Dataset
# -------------------------

df = pd.read_csv(
    "data/processed_student_behavior_data.csv"
)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

# Use productivity score
productivity_series = df["productivity_score"]

# -------------------------
# Train ARIMA Model
# -------------------------

model = ARIMA(
    productivity_series,
    order=(5, 1, 0)
)

model_fit = model.fit()

# -------------------------
# Forecast Next 7 Days
# -------------------------

forecast = model_fit.forecast(
    steps=7
)

print("\nNext 7-Day Productivity Forecast")
print("----------------------------------")

for i, value in enumerate(forecast):

    print(
        f"Day {i+1}: "
        f"{round(value, 2)}"
    )

# -------------------------
# Plot Forecast
# -------------------------

plt.figure()

plt.plot(
    productivity_series,
    label="Historical"
)

plt.plot(
    range(
        len(productivity_series),
        len(productivity_series) + 7
    ),
    forecast,
    label="Forecast"
)

plt.title(
    "Productivity Forecast"
)

plt.legend()

plt.show()