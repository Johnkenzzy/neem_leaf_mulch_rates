
# pandas_agronomy_solutions.py
# ---------------------------------------------------
# Solutions for Agronomy-themed Pandas practice (Step 2)
# ---------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("agronomy_data.csv")

print("\n=== First 5 rows ===")
print(df.head())

print("\n=== Info ===")
print(df.info())

print("\n=== Describe ===")
print(df.describe())

south_df = df[df["region"] == "South"]
recent_df = df[df["year"] >= 2020]

df["rain_m"] = df["rain_mm"] / 1000

mean_yield_by_region = df.groupby("region")["yield_t_ha"].mean()
print("\n=== Mean yield per region ===")
print(mean_yield_by_region)

mean_rain_by_year = df.groupby("year")["rain_mm"].mean()
print("\n=== Mean rainfall per year ===")
print(mean_rain_by_year)

sorted_yield = df.sort_values("yield_t_ha", ascending=False)
print("\n=== Top 5 yields ===")
print(sorted_yield.head())

pivot_yield = df.pivot_table(index="year", columns="region", values="yield_t_ha", aggfunc="mean")
print("\n=== Pivot table (mean yield per year × region) ===")
print(pivot_yield)

pivot_yield.mean(axis=1).plot(title="Average Yield per Year (All Regions)")
plt.ylabel("Yield (t/ha)")
plt.xlabel("Year")
plt.tight_layout()
plt.show()
