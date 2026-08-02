import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/WaitData.Published.xlsx")
df["Hour"] = df["x_ScheduledDTTM"].dt.hour
delayed = df[df["Wait"] > 0]

#Delay Rate By Hours

delay_rate = (
    delayed.groupby("Hour").size()
    /
    df.groupby("Hour").size()
    * 100
)

plt.figure(figsize=(10,5))

delay_rate.plot(kind="bar")

plt.title("Percentage of Appointments Delayed by Scheduled Hour")
plt.xlabel("Scheduled Hour")
plt.ylabel("Delay Rate (%)")

plt.tight_layout()

plt.savefig("visualizations/delay_rate_by_hour.png")

plt.show()

# creates blank graph
plt.figure(figsize=(10,5))
#Creates histogram divided into 30 groups
delayed["Wait"].hist(bins=30)

plt.title("Distribution of Appointment Delays")
plt.xlabel("Delay Minutes")
plt.ylabel("Number of Appointments")

plt.tight_layout()

plt.savefig("visualizations/delay_distribution.png")

plt.show()