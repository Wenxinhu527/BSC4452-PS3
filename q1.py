# Code for ps3-q1 


import pandas as pd

df = pd.read_csv("/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv")


# Define variables
highest_water = float("-inf")
highest_date = None
highest_time = None

# Using for loop to read through the file
for index, row in df.iterrows():
    date = row["Date"]
    time = row["Time (GMT)"]
    water_level = float(row["Preliminary (ft)"])

    # Get and evaluate the hightest water level and observation time
    if water_level > highest_water:
        highest_water = water_level
        highest_date = date
        highest_time = time

# Print results
print(f"Highest water level: {highest_water}ft")
print(f"Observed date: {highest_date}")
print(f"Observed time: {highest_time}")
