import numpy as np

# Load only the 'LandAverageTemperature' column (index 1)
# we skip the header row (skip_header=1)
# we tell numpy to treat missing values as 'NaN'
temps = np.genfromtxt('GlobalTemperatures.csv', delimiter=',', skip_header=1, usecols=1)

# Let's also grab the dates as strings to keep track of time
dates = np.genfromtxt('GlobalTemperatures.csv', delimiter=',', skip_header=1, usecols=0, dtype=str)

print(f"Total records loaded: {len(temps)}")