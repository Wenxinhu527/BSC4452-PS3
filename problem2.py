import pandas as pd

# Load the CSV file
file_path = '/blue/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv'
data = pd.read_csv(file_path)

# Drop rows where the 'Preliminary (ft)' value is missing or non-numeric
data['Preliminary (ft)'] = pd.to_numeric(data['Preliminary (ft)'], errors='coerce')
data = data.dropna(subset=['Preliminary (ft)'])

# Calculate the lowest, highest, and average water levels
lowest_level = data['Preliminary (ft)'].min()
highest_level = data['Preliminary (ft)'].max()
average_level = data['Preliminary (ft)'].mean()

# Find the date and time for the lowest and highest water levels
lowest_reading = data[data['Preliminary (ft)'] == lowest_level].iloc[0]
highest_reading = data[data['Preliminary (ft)'] == highest_level].iloc[0]

# Print the results
print(f"Lowest water level: {lowest_level} ft on {lowest_reading['Date']} at {lowest_reading['Time (GMT)']}")
print(f"Highest water level: {highest_level} ft on {highest_reading['Date']} at {highest_reading['Time (GMT)']}")
print(f"Average water level: {average_level:.2f} ft")

