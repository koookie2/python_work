from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

reader = csv.reader(Path('chapter_16/csv_data_sitka_weather_2021_full.csv').read_text().splitlines())
header_row = next(reader)

# Extact dates and precipitation values.
dates, rainfall = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        current_rainfall = float(row[5])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        rainfall.append(current_rainfall)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='red')

# Format the plot.
ax.set_title("Daily Rainfall in Death Valley, CA during 2021", fontsize=24)
fig.autofmt_xdate()
ax.set_xlabel("Date", fontsize=16)
ax.set_ylabel("Rainfall (cm)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()