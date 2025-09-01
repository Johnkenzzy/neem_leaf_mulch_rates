
# numpy_agronomy_solutions.py
# --------------------------------------------
# Solutions for Agronomy-themed NumPy practice (Step 1)
# --------------------------------------------

import numpy as np

rng = np.random.default_rng(42)

years = np.arange(2016, 2026)
regions = np.array(["North", "South", "East", "West"])

rain_base = np.array([950, 1300, 1100, 800])
temp_base = np.array([24.0, 27.5, 26.0, 23.0])
fert_base = np.array([120, 140, 130, 110])

rain_mm = (rain_base[:, None] + rng.normal(0, 120, size=(4, 10)))
temp_c = (temp_base[:, None] + rng.normal(0, 1.2, size=(4, 10)))
fert_kg_ha = (fert_base[:, None] + rng.normal(0, 15, size=(4, 10)))

yield_t_ha = (2.0
              + 0.004 * rain_mm
              - 0.03 * (temp_c - 25.0) ** 2
              + 0.0025 * fert_kg_ha
              + rng.normal(0, 0.25, size=(4, 10)))
yield_t_ha = np.clip(yield_t_ha, 0, None)

# 1)
last_five_years = years[-5:]

# 2)
north_idx = np.where(regions == "North")[0][0]
rain_north_2020_on = rain_mm[north_idx, years >= 2020]

# 3)
mean_yield_by_region = yield_t_ha.mean(axis=1)

# 4)
mean_rain_by_year = rain_mm.mean(axis=0)

# 5)
south_idx = np.where(regions == "South")[0][0]
corr_rain_yield_south = np.corrcoef(rain_mm[south_idx], yield_t_ha[south_idx])[0, 1]

# 6)
drought_threshold = np.percentile(mean_rain_by_year, 20)
drought_year_mask = mean_rain_by_year < drought_threshold
drought_years = years[drought_year_mask]

# 7)
fue = yield_t_ha / fert_kg_ha
mean_fue_by_region = fue.mean(axis=1)

# 8)
row_means = yield_t_ha.mean(axis=1, keepdims=True)
row_stds = yield_t_ha.std(axis=1, ddof=0, keepdims=True)
yield_z = (yield_t_ha - row_means) / row_stds

# 9)
east_idx = np.where(regions == "East")[0][0]
east_yield = yield_t_ha[east_idx]
east_yield_ma3 = np.convolve(east_yield, np.ones(3)/3, mode='valid')

# 10)
rain_flat = rain_mm.ravel()
rain_back = rain_flat.reshape(4, 10)

if __name__ == "__main__":
    print("Solutions summary")
    print("1) last_five_years:", last_five_years)
    print("2) North rainfall 2020+ (mm):", np.round(rain_north_2020_on, 1))
    print("3) Mean yield by region (t/ha):", np.round(mean_yield_by_region, 2))
    print("4) Mean rainfall by year (mm):", np.round(mean_rain_by_year, 1))
    print("5) Corr(rain, yield) South:", round(float(corr_rain_yield_south), 3))
    print("6) Drought years:", drought_years)
    print("7) Mean FUE by region (t/kg):", np.round(mean_fue_by_region, 4))
    print("8) Yield z-scores shape:", yield_z.shape, " Means ~0:", np.round(yield_z.mean(axis=1), 6))
    print("9) East 3-yr MA:", np.round(east_yield_ma3, 2))
    print("10) Shapes -> flat:", rain_flat.shape, "back:", rain_back.shape)

