import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks as long as program is active
while True:
	# Make a random walk & plot points
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_values, rw.y_values, s=15)
	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break