import pandas as pd

df = pd.read_excel("data/WaitData.Published.xlsx")
#Shows first 5 rows 
print(df.describe)

print(df[df["Wait"] < 0][["Wait",
"x_ArrivalDTTM",
"x_ScheduledDTTM",
"x_BeginDTTM"]].head(10))

average_wait = df["Wait"].mean()
rounded_average_wait = round(average_wait, 2)
print("Average Wait Time: ", rounded_average_wait, " minutes")

Median_Wait = df["Wait"].median()
print("Median Wait Time: ", Median_Wait, " minutes")

max_wait = df["Wait"].max()
print("Longest Wait Time: ", max_wait, " minutes")

#How often are patients experiencing long long_delays (>30 minutes)?
long_delayed = df[df["Wait"]>30]
print("Patients Delayed: ", len(long_delayed))

#What percentage of all patients experience long long_delays (>30 minutes)?
long_delayed_percentile = round(len(long_delayed)/len(df) * 100, 2)
print(long_delayed_percentile, "% of patients exceed a 30 minute wait")

#Creates a new column with early or late
df["wait_status"] = df["Wait"].apply(
    lambda x: "Early" if x<0 else( "Delayed" if x>0 else "On Time")
)
#Counts late vs early
print("Total Appointments ", len(df))


#Percentages of Late, Early, and On Time appointments (normalize = true gives us proprotions not counts)
status_percentiles = (
    df["wait_status"].value_counts(normalize=True) *100
)
print(status_percentiles, "%")

#Gives us perentage of patients that experience late appointments and the average wait time"
percentage_late_starts = round(len(df[df["Wait"]>0])/len(df) * 100, 2)
print(percentage_late_starts, "% of patients experience late appoinments")
late_wait_time = df[df["Wait"] > 0]
print("The average wait time for late appointments is ", round(late_wait_time["Wait"].mean(),2), "minutes")

#Describes the delays - average delay, typical delay, worst delay, spread of delays
df["Hour"] = df["x_ScheduledDTTM"].dt.hour
delayed = df[df["Wait"] > 0]
print(delayed["Wait"].describe())

#When are the delays most frequently happening?
print(delayed.groupby("Hour")["Wait"].mean())
print("Appointments by hour: \n", df.groupby("Hour").size())

#What Hours of the day have the most late appointments (different from wait time)
print(delayed.groupby("Hour").size())

# Creates new data frame with everything included
hour_analysis = pd.DataFrame({
    "Total_Appointments": df.groupby("Hour").size(),
    "Delayed_Appointments": delayed.groupby("Hour").size(),
    "Average_Delay": delayed.groupby("Hour")["Wait"].mean()
})

print(hour_analysis)