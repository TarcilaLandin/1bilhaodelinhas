import pandas as pd

df = pd.read_csv("data\measurements.txt",
                 sep = ";",
                 header = None,
                 names=["station", "measure"])
print(df)
#df_agg = df.groupby("station")
#df_kpi = df_agg["measure"].agg({
#         "min": "min", 
#         "max": "max" , "mean"})