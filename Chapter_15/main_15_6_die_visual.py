import plotly.express as px

from main_15_5_die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyse the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.write_html('Chapter_15/dice_visual_d6d10.html')