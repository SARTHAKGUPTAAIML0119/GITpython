import numpy as np
filename='GlobalTemperatures.csv'
data=np.genfromtxt(filename,delimiter=',',skip_header=1,usecols=(0,1),dtype=None, encoding='utf-8',names=['date','temp'])
dates=data['date']
temps=data['temp']

mask = ~np.isnan(temps)
clean_temps = temps[mask]
clean_dates = temps[mask]

overall_mean=np.mean(clean_temps)
hottest_month_idx=np.argmax(clean_temps)
coldest_month_idx=np.argmin(clean_temps)

print("---Analysis Results---")
print(f"Total months analysed:{len(clean_temps)}")
print(f"Global Average Temp (1750-2015):{overall_mean:.2f}°C")
print(f"Hottest Month: {clean_temps[hottest_month_idx]}°C")
print(f"Coldest Month: {clean_temps[coldest_month_idx]}°C")
