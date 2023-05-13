from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def find_index(*index):
    """Find the indexes in a csv file."""
    list = {}
    for i in index:
        for location in range(len(header_row)):
            if header_row[location] == i:
                list[i] = location
    return list

reader = csv.reader(Path('chapter_16/csv_data_sitka_weather_2021_full.csv').read_text().splitlines())
header_row = next(reader)

list = find_index("DATE", "TMIN", "TMAX")

# Extact dates, high temperature, and low temperature values.
dates, highs, lows = [], [], []
for row in reader:
    date = datetime.strptime(row[list["DATE"]], '%Y-%m-%d')
    try:
        high = float(row[list["TMAX"]])
        low = float(row[list["TMIN"]])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, lows, highs, color='blue', alpha=0.1)

# Format the plot.
ax.set_title("Daily Rainfall in Sitka, CA during 2021", fontsize=24)
fig.autofmt_xdate()
ax.set_xlabel("Date", fontsize=16)
ax.set_ybound(0, 150)
ax.set_ylabel("Rainfall (cm)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()