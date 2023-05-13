from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('chapter_16/json_data_eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
mags, lons, lats, eq_titles = [], [], [], []
for eq_data in all_eq_data['features']:    
    mags.append(eq_data['properties']['mag'])
    lons.append(eq_data['geometry']['coordinates'][0])
    lats.append(eq_data['geometry']['coordinates'][1])
    eq_titles.append(eq_data['properties']['title'])

fig = px.scatter_geo(lat=lats, lon=lons, size=mags,
                     title=all_eq_data['metadata']['title'],
                     color=mags,
                     color_continuous_scale='viridis',
                     labels={'color': "Magnitude"},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()