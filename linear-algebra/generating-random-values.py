import numpy as np

# Set the random seed for reproducibility
np.random.seed(20)

# Generate a random number between 0 and 1
random = np.random.rand()
print(random)

# Generate a random integer between 0 and 100
random = np.random.randint(0, 100)
print(random)

# Generate an array of 5 random integers between 0 and 100
random = np.random.randint(0, 100, 5)
print(random)

# Generate a 5x5 array of random integers between 0 and 100
random = np.random.randint(0, 100, (5, 5))
print(random)