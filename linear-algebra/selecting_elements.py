import numpy as np
from numpy.matrixlib.defmatrix import matrix

# Creating a 1-dimensional array (vector) with elements 1 to 10
vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Creating a 2-dimensional array (matrix) with 3 rows and 3 columns
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Printing the third element of the vector (index 2)
print(vector[2])

# Printing the element at the second row and second column of the matrix (index 1, 1)
print(matrix[1, 1])

# Printing the first three elements of the vector (slicing from index 0 to 3, exclusive)
print(vector[:3])

# Printing the first two rows and first two columns of the matrix (slicing)
print(matrix[:2, :2])

# Printing elements from index 3 to 5 of the vector (slicing from index 3 to 6, exclusive)
print(vector[3:6])

# Printing the elements from the second row to the end and first two columns of the matrix (slicing)
print(matrix[1:, :2])

# Printing every second element of the vector (slicing with step 2)
print(vector[::2])