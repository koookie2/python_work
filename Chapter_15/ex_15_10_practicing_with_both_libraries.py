import matplotlib.pyplot as plt
import plotly.express as px

from ex_15_5_refactoring import RandomWalk
from main_15_5_die import Die

# Create two D6 dice.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for i in range(1000)]

# Analyse the results.
frequencies = [results.count(value) for value in range(1,7)]

# Set the x and y values.
x_values = [1, 2, 3, 4, 5, 6]
y_values = frequencies

# Initialize the plot.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes.
ax.set_title("Results of Rolling Two D6 1,000 Times", fontsize=14)
ax.set_xlabel("Results", fontsize=14)
ax.set_ylabel("Frequencies of Results", fontsize=14)

# Set the range for each axis.
ax.axis([x_values[0]-0.1, x_values[-1]+0.1, 0, sorted(y_values)[-1]+20])

plt.show()


rw = RandomWalk(10)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()

# Visualize the results.
title = "A Random Walk"
labels = {'x': 'X-Values', 'y': 'Y-Values'}
fig = px.bar(x=rw.x_values, y=rw.y_values, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()