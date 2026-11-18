
# ISM2411 Capstone — Shipment Analysis
# Author: William Baker
# Date:   

# Business Questions:
 # 1. [Your question 1]
 # 2. [Your question 2]
 # 3. [Your question 3]

# AI Disclosure: [What, if anything, you used AI for]


#  ────────────────────────────────────────────────────────────────────


import pandas as pd

df = pd.read_csv("data/capstone_shipments.csv")  
print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print(df.describe())

# ── 1. LOAD ───────────────────────────────────────────────────
DATA_FILE = "data/capstone_shipments.csv" 
df = pd.read_csv(DATA_FILE)
print("Raw shape:", df.shape)
print(df.head())
df.info()
print(df.isnull().sum())

