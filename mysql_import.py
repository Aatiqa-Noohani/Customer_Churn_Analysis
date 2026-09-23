import pandas as pd

file_path = r"C:\Users\USER\OneDrive\Desktop\Customer_churn_python+ Sql project\OTT_Customer_Churn_1500.csv"

df = pd.read_csv(file_path)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())