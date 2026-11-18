
print("ISM2411 Capstone — Shipment Analysis")
print("Author: William Baker")
print("Date:  ") 

# Business Questions:
 # 1. [Your question 1]
 # 2. [Your question 2]
 # 3. [Your question 3]

# AI Disclosure: [What, if anything, you used AI for]


print("----------------------------------------------------------------------------")


import pandas as pd

df = pd.read_csv("data/capstone_shipments.csv")  
print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print(df.describe())

