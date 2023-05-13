from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

sitka_path = Path('chapter_16/csv_data_sitka_weather_2021_full.csv')
dvalley_path = Path('chapter_16/csv_data_death_valley_2021_full.csv')

sitka_reader = csv.reader(sitka_path.read_text().splitlines())
dvalley_reader = csv.reader(dvalley_path.read_text().splitlines())
sitka_header_row, dvalley_header_row = next(sitka_reader), next(dvalley_reader)

# Extact dates, high temperatures, and low temperatures values in sitka.
sitka_dates, sitka_highs, sitka_lows = [], [], []
for row in sitka_reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[7])
        low = int(row[8])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        sitka_dates.append(date)
        sitka_highs.append(high)
        sitka_lows.append(low)

# Plot the high and low temperatures in Sitka.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, color='red')
ax.plot(sitka_dates, sitka_lows, color='blue')
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)

# Format that plot.
ax.set_title("Daily High and Low Temperatures in Sitka, AK, 2021", fontsize=24)
fig.autofmt_xdate()
ax.set_ybound(0, 150)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()


# Extact dates, high temperatures, and low temperatures values in Death Valley.
dvalley_dates, dvalley_highs, dvalley_lows = [], [], []
for row in dvalley_reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dvalley_dates.append(date)
        dvalley_highs.append(high)
        dvalley_lows.append(low)

# Plot the high and low temperatures in Death Valley.
fig, ax = plt.subplots()
ax.plot(dvalley_dates, dvalley_highs, color='red')
ax.plot(dvalley_dates, dvalley_lows, color='blue')
ax.fill_between(dvalley_dates, dvalley_highs, dvalley_lows, facecolor='blue', alpha=0.1)

# Format that plot.
ax.set_title("Daily High and Low Temperatures in Death Valley, CA, 2021", fontsize=24)
fig.autofmt_xdate()
ax.set_ybound(0, 150)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# Plot the high and low temperatures in both locations.
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, color='red')
ax.plot(sitka_dates, sitka_lows, color='blue')
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)
ax.plot(dvalley_dates, dvalley_highs, color='red')
ax.plot(dvalley_dates, dvalley_lows, color='blue')
ax.fill_between(dvalley_dates, dvalley_highs, dvalley_lows, facecolor='blue', alpha=0.1)

# Format that plot.
ax.set_title("Daily High and Low Temperatures in Both Locations", fontsize=24)
fig.autofmt_xdate()
ax.set_ybound(0, 150)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()