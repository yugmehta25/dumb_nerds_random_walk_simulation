import numpy as np
import matplotlib.pyplot as plt
import random

# Defining the number of steps
n = 100000

# Creating two arrays for containing x and y coordinates
# of size equals to the number of steps and filled up with 0's
x = np.zeros(n)
y = np.zeros(n)

# Filling the coordinates with random variables
for i in range(1, n):
    val = random.randint(1, 4)  # Randomly choose direction
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        y[i] = y[i - 1] - 1

# Plotting the random walk
plt.title(f"Random Walk ($n = {n}$ steps)")
plt.plot(x, y)
plt.savefig(f"rand_walk{n}.png", bbox_inches="tight", dpi=600)
plt.show()
