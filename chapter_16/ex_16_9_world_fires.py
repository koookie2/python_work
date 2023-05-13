from pathlib import Path
import csv
import plotly.express as px

# Initailize the reader and header row
path = Path('chapter_16/csv_data_world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Determine what index corresponds with the given string.
indexes = ["latitude", "longitude", "brightness"]
locations, data = {}, {}
for index in indexes:
    try:
        locations[index] = header_row.index(index)
    except:
        print(f"The value, {index}, is not part of the file's header row.")
        continue
    data[index] = []

# Extract the data values.
for row in reader:
    for index in data:
        location = locations[index]
        value = float(row[location])
        data[index].append(value)

fig = px.scatter_geo(lat=data["latitude"], lon=data["longitude"],
                     title="Wildfires in the Past Day",
                     color=data["brightness"],
                     color_continuous_scale='viridis',
                     labels={'color': "Brightness"},
                     projection='natural earth',
                     )
fig.show()