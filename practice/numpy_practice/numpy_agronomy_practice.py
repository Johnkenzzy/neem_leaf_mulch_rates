
# numpy_agronomy_practice.py
# --------------------------------------------
# Agronomy-themed NumPy practice (Step 1)
# --------------------------------------------
# Instructions:
# 1) Work through the TODOs below in order.
# 2) Run this file with:  python numpy_agronomy_practice.py
# 3) No extra packages required beyond NumPy.
#
# Datasets:
#   - years: 2016..2025 (10 seasons)
#   - regions: North, South, East, West (4 regions)
#   - rain_mm[region, year], temp_c[region, year], fert_kg_ha[region, year], yield_t_ha[region, year]
#     with realistic(ish) relationships + noise for practice.
#
# Hints are provided for each task. Try without them first!

import numpy as np

rng = np.random.default_rng(42)

years = np.arange(2016, 2026)                   # shape (10,)
regions = np.array(["North", "South", "East", "West"])  # shape (4,)

# --- Generate synthetic agronomic arrays (shapes all 4 x 10) ---
# Region-specific baselines
rain_base = np.array([950, 1300, 1100, 800])    # mean annual rainfall (mm) by region
temp_base = np.array([24.0, 27.5, 26.0, 23.0])  # average season temperature (°C) by region
fert_base = np.array([120, 140, 130, 110])      # baseline fertilizer (kg/ha) by region

# Build matrices by broadcasting and adding year-to-year variability
rain_mm = (rain_base[:, None] 
           + rng.normal(0, 120, size=(4, 10)))  # inter-annual variation
temp_c = (temp_base[:, None] 
          + rng.normal(0, 1.2, size=(4, 10)))
fert_kg_ha = (fert_base[:, None] 
              + rng.normal(0, 15, size=(4, 10)))

# Yield model (toy): baseline + rainfall effect - heat stress + fertilizer effect + noise
# Ensure non-negative with np.clip
yield_t_ha = (2.0
              + 0.004 * rain_mm
              - 0.03 * (temp_c - 25.0) ** 2
              + 0.0025 * fert_kg_ha
              + rng.normal(0, 0.25, size=(4, 10)))
yield_t_ha = np.clip(yield_t_ha, 0, None)

# --------------------------------------------
# TASKS (fill in the TODOs)
# --------------------------------------------

# 1) Warm-up: Create a 1D array of the last 5 years in 'years'.
#    Expected: shape (5,) with values [2021, 2022, 2023, 2024, 2025]
# TODO: last_five_years = ...

# 2) Slicing & boolean masks: For the 'North' region, get rainfall for years >= 2020.
#    Hint: find the index of "North" in regions, then slice rain_mm.
# TODO: north_idx = ...
# TODO: rain_north_2020_on = ...

# 3) Aggregations: Compute mean yield per region across all years.
#    Expected shape: (4,). Use axis=1.
# TODO: mean_yield_by_region = ...

# 4) Aggregations: Compute mean rainfall per year across regions.
#    Expected shape: (10,). Use axis=0.
# TODO: mean_rain_by_year = ...

# 5) Correlation: For the 'South' region, compute the correlation between rainfall and yield.
#    Hint: use np.corrcoef(a, b)[0,1].
# TODO: south_idx = ...
# TODO: corr_rain_yield_south = ...

# 6) Percentiles & masks: Identify drought years (by year) when mean rainfall across regions
#    falls below the 20th percentile of mean_rain_by_year.
# TODO: drought_threshold = ...
# TODO: drought_year_mask = ...
# TODO: drought_years = ...   # years[drought_year_mask]

# 7) Broadcasting: Compute fertilizer-use efficiency (FUE) = yield_t_ha / fert_kg_ha for each cell.
#    Units: t per kg. Then compute the per-region mean FUE across years.
# TODO: fue = ...
# TODO: mean_fue_by_region = ...

# 8) Standardization: Compute z-scores of yield per region (standardize each row separately).
#    Hint: subtract row means and divide by row std (keepdims to broadcast along columns).
# TODO: row_means = ...
# TODO: row_stds = ...
# TODO: yield_z = ...

# 9) Moving average (1D): For the 'East' region, compute a 3-year moving average of yield.
#    Hint: use np.convolve with kernel np.ones(3)/3 and 'valid' mode.
# TODO: east_idx = ...
# TODO: east_yield = ...
# TODO: east_yield_ma3 = ...

# 10) Reshaping (optional): Flatten the 4x10 rainfall matrix to 40 values, then reshape back.
# TODO: rain_flat = ...
# TODO: rain_back = ...

# ------------------------------
# QUICK CHECKS (optional prints)
# Uncomment these prints once you've filled in the TODOs to inspect results.
# ------------------------------
# print("1) last_five_years:", last_five_years)
# print("2) North rainfall 2020+ (mm):", np.round(rain_north_2020_on, 1))
# print("3) Mean yield by region (t/ha):", np.round(mean_yield_by_region, 2))
# print("4) Mean rainfall by year (mm):", np.round(mean_rain_by_year, 1))
# print("5) Corr(rain, yield) South:", round(float(corr_rain_yield_south), 3))
# print("6) Drought years:", drought_years)
# print("7) Mean FUE by region (t/kg):", np.round(mean_fue_by_region, 4))
# print("8) Yield z-scores shape:", yield_z.shape, " Means ~0:", np.round(yield_z.mean(axis=1), 6))
# print("9) East 3-yr MA:", np.round(east_yield_ma3, 2))
# print("10) Shapes -> flat:", rain_flat.shape, "back:", rain_back.shape)

if __name__ == "__main__":
    print("Practice file ready. Open and complete the TODOs. Happy hacking!")

