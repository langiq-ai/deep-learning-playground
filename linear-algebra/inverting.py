import numpy as np
from numpy.matrixlib.defmatrix import matrix

matrix = np.array(
    [
        [1, 2],
        [4, 5]

    ]
)

print(matrix)

# Inverting the matrix
inverse_matrix = np.linalg.inv(matrix)

print(inverse_matrix)