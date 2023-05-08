import matplotlib.pyplot as plt

from main_15_3_random_walk import RandomWalk

# Make a random walks.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth=3)
ax.set_aspect('equal')

# Remove the the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()