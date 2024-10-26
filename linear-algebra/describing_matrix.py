import numpy as np
from numpy.matrixlib.defmatrix import matrix

# Creating a 2-dimensional array (matrix) with 3 rows and 3 columns
matrix = np.array(
    [
        [1, 2, 3],  # First row of the matrix
        [4, 5, 6],  # Second row of the matrix
        [7, 8, 9]   # Third row of the matrix
    ]
)

# Printing the entire matrix to the console
print(matrix)

# Printing the shape of the matrix (number of rows and columns)
print(matrix.shape)

# Printing the total number of elements in the matrix
print(matrix.size)

# Printing the number of dimensions of the matrix
print(matrix.ndim)