#
# ==========================================
# STEP 7: SEVERITY ANALYSIS
# ==========================================

#

# ==========================================
# STEP 8: DAY OF WEEK ANALYSIS
# ==========================================

#
##
##
#
import pandas as pd
import matplotlib.pyplot as plt
import os

print("Loading dataset...")

df = pd.read_csv(
    "data/accidents_sample.csv",
    usecols=["State"]
)

print("Dataset loaded!")
print("Rows:", len(df))

# Remove missing states
df["State"] = df["State"].fillna("Unknown")

# Top 10 states
top_states = df["State"].value_counts().head(10)

print("\nTop 10 States by Accident Count:")
print(top_states)

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_states.index,
    top_states.values
)

plt.title("Top 10 States by Traffic Accident Count")
plt.xlabel("State")
plt.ylabel("Number of Accidents")

plt.tight_layout()

plt.savefig(
    "outputs/top_10_states.png",
    dpi=300
)

plt.close()

print("\nSUCCESS!")
print("Chart saved: outputs/top_10_states.png")