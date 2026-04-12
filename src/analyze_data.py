import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/student_behavior_data.csv")

# Show first rows
print("First 5 rows:")
print(df.head())

# Show summary statistics
print("\nDataset Summary:")
print(df.describe())

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# -----------------------------
# Plot 1 — Study Hours Over Time
# -----------------------------
plt.figure()
plt.plot(df["date"], df["study_hours"])
plt.title("Study Hours Over Time")
plt.xlabel("Date")
plt.ylabel("Study Hours")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------
# Plot 2 — Sleep vs Productivity
# -----------------------------
plt.figure()
sns.scatterplot(
    x=df["sleep_hours"],
    y=df["productivity_score"]
)

plt.title("Sleep Hours vs Productivity")
plt.xlabel("Sleep Hours")
plt.ylabel("Productivity Score")

plt.tight_layout()
plt.show()

# -----------------------------
# Plot 3 — Productivity Distribution
# -----------------------------
plt.figure()
sns.histplot(df["productivity_score"], bins=20)

plt.title("Productivity Score Distribution")
plt.xlabel("Productivity Score")

plt.tight_layout()
plt.show()