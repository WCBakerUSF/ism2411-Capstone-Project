import pandas as pd

df = pd.read_csv("data/capstone_retail.csv")   # your dataset's file name
print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print(df.describe())
