import pandas as pd
import sqlite3

# Read Excel
df = pd.read_excel("data/WaitData.Published.xlsx")

# Connect/create database
connection = sqlite3.connect("data/hospital_operations.db")

# Upload dataframe as table
df.to_sql(
    "appointments",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Database created")