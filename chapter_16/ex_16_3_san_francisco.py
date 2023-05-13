from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

reader = csv.reader(Path('chapter_16/csv_data_san_francisco.csv').read_text().splitlines())
header_row = next(reader)

# Extact dates, high temperatures, and low temperatures values in San Francisco.
dates, highs, lows = [], [], []
for row in reader:
    date = datetime.strptime(row[1], '%Y-%m-%d')
    try:
        high = int(row[2])
        low = int(row[3])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures in San Francisco.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format that plot.
ax.set_title("Daily High and Low Temperatures in San Francisco, CA, 2021", fontsize=24)
fig.autofmt_xdate()
ax.set_ybound(0, 150)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()