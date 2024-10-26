import numpy as np
from numpy.matrixlib.defmatrix import matrix

# Creating a 2-dimensional array (matrix) with 3 rows and 3 columns
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Printing the original matrix to the console
print(matrix)

# Flattening the matrix to a 1D array
flattened = matrix.flatten()

# Printing the flattened 1D array to the console
print(flattened)