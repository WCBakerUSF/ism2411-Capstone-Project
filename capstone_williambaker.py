
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


# ── 1. LOAD ───────────────────────────────────────────────────
DATA_FILE = "data/capstone_shipments.csv"  

# Load raw data from the dataset
df = pd.read_csv(DATA_FILE) 

# Check shape (rows, columns)
print("Shape:", df.shape)

# Inspect first 5 rows
print(df.head())

# Summary of data types and missing values
df.info()

# Check missing values per column
print(df.isnull().sum())

# Statistical summary (for numeric columns)
print(df.describe())

# ── 2. DATA CLEANING ──────────────────────────────────────────────────
# The columns in the dataset need to be standardized
# 












# ── 5. BUSINESS QUESTION 1 ────────────────────────────────────
# [State your question in a comment]
# [Your analysis code here]
# [Your chart code here — with title, axis labels, savefig, show]
# [Write a one-sentence finding in a comment]

# ── 6. BUSINESS QUESTION 2 ────────────────────────────────────
# [State your question]
# [Analysis + chart]

# ── 7. BUSINESS QUESTION 3 ────────────────────────────────────
# [State your question]
# [Analysis + chart]

# ── 8. SAVE CLEAN DATA ────────────────────────────────────────
df.to_csv("data/clean_data.csv", index=False)
print("\nCapstone complete. Clean data saved to data/clean_data.csv")
