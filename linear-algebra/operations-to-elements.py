import numpy as np
from numba import vectorize

# Create a 2D numpy array (matrix) with 3 rows and 3 columns
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define a lambda function to add 100 to each element
add_100 = lambda i: i + 100

# Apply the lambda function to the entire matrix and print the result
print(add_100(matrix))

# Use Numba's vectorize decorator to create a vectorized version of the add_100 function
vectorize_add_100 = vectorize(add_100)

# Apply the vectorized function to the entire matrix and print the result
print(vectorize_add_100(matrix))