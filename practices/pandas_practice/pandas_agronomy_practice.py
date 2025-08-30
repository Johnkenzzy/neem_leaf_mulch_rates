
# pandas_agronomy_practice.py
# ---------------------------------------------------
# Agronomy-themed Pandas practice (Step 2)
# ---------------------------------------------------
# Instructions:
# 1) Ensure you have pandas and matplotlib installed:
#       pip install pandas matplotlib
# 2) Place agronomy_data.csv in the same directory as this file.
# 3) Fill in the TODOs below and run with:
#       python pandas_agronomy_practice.py
#
# Goal: Learn Pandas basics while exploring agronomic data.

import pandas as pd
import matplotlib.pyplot as plt

# 1) Load the dataset
# TODO: df = pd.read_csv(...)

# 2) Inspect the dataset
# TODO: print first 5 rows (head)
# TODO: print info() to check column types
# TODO: print describe() for numeric stats

# 3) Select & filter data
# TODO: Create a DataFrame 'south_df' with only rows where region == "South"
# TODO: Create a DataFrame 'recent_df' with only rows where year >= 2020

# 4) Column operations
# TODO: Create a new column 'rain_m' = rain_mm / 1000  (convert to meters)

# 5) Aggregations
# TODO: Compute mean yield per region (groupby + mean)
# TODO: Compute mean rainfall per year across regions

# 6) Sorting
# TODO: Sort the dataset by 'yield_t_ha' descending, show top 5 rows

# 7) Pivot table
# TODO: Create a pivot table with index=year, columns=region, values=yield_t_ha, aggfunc='mean'

# 8) Plotting
# TODO: Plot a line chart of average yield per year (use the pivot table or groupby result)
# Hint: use .plot() and plt.show()

if __name__ == "__main__":
    print("Pandas practice file ready. Fill in the TODOs and run this script.")
