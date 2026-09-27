"""Pandas preparation and exploratory analysis for the Heart Disease project.

Place heart_disease_clean.csv in ../data/ before running.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "heart_disease_clean.csv"
OUTPUT = ROOT / "data" / "heart_disease_clean.csv"

if not DATA.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA}\nCopy your 303-row cleaned CSV into the data folder first.")

df = pd.read_csv(DATA)
print("Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Normalize target to binary when the source uses 0-4 Cleveland labels.
if "target" in df.columns:
    df["target"] = pd.to_numeric(df["target"], errors="coerce")
    df["target"] = (df["target"] > 0).astype(int)

# Remove exact duplicate rows for a clean analytical dataset.
df = df.drop_duplicates().reset_index(drop=True)

# Derived columns used by the dashboard.
df["Disease Status"] = df["target"].map({0: "No Disease", 1: "Heart Disease"})
df["Gender"] = df["sex"].map({0: "Female", 1: "Male"})
df["Chest Pain Type"] = df["cp"].map({1: "Typical Angina", 2: "Atypical Angina", 3: "Non-anginal Pain", 4: "Asymptomatic"})
df["FBS Category"] = df["fbs"].map({0: "FBS ≤ 120 mg/dl", 1: "FBS > 120 mg/dl"})
df["Exercise Angina"] = df["exang"].map({0: "No Angina", 1: "With Angina"})
df["ST Slope"] = df["slope"].map({1: "Upsloping", 2: "Flat", 3: "Downsloping"})
df["Age Group"] = pd.cut(df["age"], bins=[0, 39, 49, 59, 69, float("inf")], labels=["<40", "40-49", "50-59", "60-69", "70+"])

print("\nTotal patients:", len(df))
print("Heart disease patients:", int(df["target"].sum()))
print("Heart disease %:", round(df["target"].mean() * 100, 1))
print("Average age:", round(df["age"].mean(), 2))
print("Average cholesterol:", round(df["chol"].mean(), 2))

# Save the analytical dataset used by the web app/Tableau.
df.to_csv(OUTPUT, index=False)
print("\nSaved:", OUTPUT)

# Simple EDA plots (saved only when run directly).
if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    df["Disease Status"].value_counts().plot(kind="bar", ax=axes[0], title="Disease Distribution")
    df["Age Group"].value_counts().sort_index().plot(kind="bar", ax=axes[1], title="Age Distribution")
    plt.tight_layout()
    out = ROOT / "docs" / "pandas_eda.png"
    fig.savefig(out, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print("Saved chart:", out)
