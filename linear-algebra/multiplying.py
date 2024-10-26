import numpy as np
from numpy.matrixlib.defmatrix import matrix

# Creating a 2-dimensional array (matrix) with 3 rows and 3 columns
matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

# Printing the original matrix to the console
print(matrix * 2)

# Attempting to perform element-wise XOR operation on the matrix
matrix_b = matrix ^ 2

# Printing the result of the XOR operation to the console
print(matrix_b)

# Attempting to perform element-wise multiplication of the original matrix and the XOR result
print(matrix * matrix_b)

# Performing matrix multiplication (dot product) of the original matrix and the XOR result
print(matrix @ matrix_b)