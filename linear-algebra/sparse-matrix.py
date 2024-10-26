# Importing the numpy library, which is used for numerical operations on arrays
import numpy as np

# Importing the sparse module from the scipy library, which is used for creating and working with sparse matrices
from scipy import sparse

# Creating a 1-dimensional array (vector) with elements 1, 2, 3, 4
vector_row = np.array([1, 2, 3, 4])

# Creating a 2-dimensional array (column vector) with elements 1, 2, 3
vector_column = np.array([[1], [2], [3]])

# Printing the row vector to the console
print(vector_row)

# Printing the column vector to the console
print(vector_column)

# Creating a 2-dimensional array (matrix) with 3 rows and 2 columns, each row containing elements 1, 2
matrix = np.array([[1, 2], [1, 2], [1, 2]])

# Printing the matrix to the console
print(matrix)

# Creating a 2-dimensional array (matrix) with 3 rows and 2 columns, with specific elements
matrix = np.array([[0, 0], [0, 1], [3, 0]])

# Creating a compressed sparse row (CSR) matrix from the dense matrix
matrix_sparse = sparse.csr_matrix(matrix)

# Creating a larger 2-dimensional array (matrix) with 3 rows and 10 columns, with specific elements
matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Creating a compressed sparse row (CSR) matrix from the larger dense matrix
matrix_large_sparse = sparse.csr_matrix(matrix_large)

# Printing the original sparse matrix to the console
print(matrix_sparse)

# Printing the larger sparse matrix to the console
print(matrix_large_sparse)