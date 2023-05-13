from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def find_index(*indexes):
    """Find the indexes in a csv file."""
    locations = {}
    for index in indexes:
        for location in range(len(header_row)):
            if header_row[location] == index:
                locations[index] = location
    return locations

reader = csv.reader(Path('chapter_16/csv_data_my_area_code.csv').read_text().splitlines())
header_row = next(reader)

indexes = find_index("DATE", "PRCP")

# Extact dates, high temperature, and low temperature values.
dates, rainfall = [], []
for row in reader:
    date = datetime.strptime(row[indexes["DATE"]], '%Y-%m-%d')
    try:
        current_rainfall = float(row[indexes["PRCP"]])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        rainfall.append(current_rainfall)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='green')

# Format the plot.
ax.set_title("Daily Rainfall in Sitka, CA during 2021", fontsize=24)
fig.autofmt_xdate()
ax.set_xlabel("Date", fontsize=16)
ax.set_ylabel("Rainfall (cm)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()