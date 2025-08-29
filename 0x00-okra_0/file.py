import pandas as pd

df = pd.read_excel("okra_0_data.xlsx", "Sheet1", index_col=None, na_values=["NA"])
print(df)
