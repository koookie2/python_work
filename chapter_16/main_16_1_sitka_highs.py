from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('chapter_16/csv_data_sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extact dates and high temperatures.
dates, highs = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(date)
    highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format the plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
# ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()