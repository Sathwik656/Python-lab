import pandas as pd
import numpy as np

df=pd.read_csv("Employee.csv")

print("Original data frame: \n",df)
print("Check for null values using isnull(): \n",df.isnull())
print("Check for non-null values using notnull(): \n",df.notnull())

df_filled_scalar = df.fillna(0)
print("Data frame after filling NaN with 0: \n",df_filled_scalar)

df_fill = df.fillna(method='ffill')
print("Data frame after forward fill (pad/ffill): \n",df_fill)

df_bfill = df.fillna(method='bfill')
print("Dataframe after backward fill (bfill): \n",df_bfill)

df_row_filled = df.ffill(axis=0)
print("Dataframe after row-wise forward fill: \n",df_row_filled)

df_dropped_rows = df.dropna()
print("Dataframe after dropping rows with NaN: ",df_dropped_rows)

df_dropped_cols = df.dropna(axis=1)
print("Dataframe after dropping columns with Nan: ",df_dropped_cols)