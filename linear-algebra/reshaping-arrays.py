import numpy as np
from numpy.matrixlib.defmatrix import matrix

# Creating a 2-dimensional array (matrix) with 3 rows and 3 columns
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Reshape the matrix to a 1D array with 9 elements
reshaped_matrix = matrix.reshape(9)

# Printing the reshaped 1D array to the console
print(reshaped_matrix)

# Reshape the matrix back to a 2D array with 3 rows and 3 columns
reshaped_matrix = matrix.reshape(3, 3)

# Printing the reshaped 2D array to the console
print(reshaped_matrix)