import matplotlib.pyplot as plt

from main_15_3_random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walks.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.plasma, edgecolors='none', s=50)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break