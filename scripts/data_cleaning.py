import pandas as pd

import os
df = pd.read_excel("data/WaitData.Published.xlsx")
#Shows first 5 rows 
print(df.head())

#Number of rows, columns, column names, data types, missing values
print(df.info())

#Count, mean, standard dev, min, max, percentiles
print(df.describe())
print("Number of missing values: \n", df.isnull().sum())
print("Number of duplicated values: ", df.duplicated().sum())

# These 3 columns represent arrival time, scheduled time, start time
print(df[["x_ArrivalDTTM",
          "x_ScheduledDTTM",
          "x_BeginDTTM",
          "Wait"]].head(10))

print(df["Wait"].value_counts().head(20))

#Boolean Indexing ↓: Acts like if statement that takes true values (negative waits = list of true statements less than 0)
negative_waits = df[df["Wait"] < 0]
print("Early Starts/ Negative Wait Times: ", len(negative_waits))
