""" Python script for
   - Representing sparse matrix
   - Sparse matrix addition
   - Sparse matrix transpose  """

# Write your code from here

# Sparse Matrix contains large number of Zeros.
# They are common in scientific applications.


##numpy module - is a general-purpose array-processing package.
##It provides a high-performance multidimensional array object,
##and tools for working with these arrays.
##It is the fundamental package for scientific computing with Python


##SciPy is a scientific computation library that uses NumPy underneath.
##SciPy stands for Scientific Python. It provides more utility functions
##for optimization, stats and signal processing.

# Python program to create
# sparse matrix using csr_matrix() - Compressed Sparse Row matrix

# Import required package
import numpy as np
from scipy.sparse import csr_matrix

row_01 = np.array([0, 0, 1, 1, 2])
col_01 = np.array([0, 1, 2, 0, 2])
data_01 = np.array([1, 4, 5, 8, 9])
sparse_matrix_01 = csr_matrix((data_01, (row_01, col_01)),shape = (3, 3)).toarray()
print("First Sparse Matrix : ", sparse_matrix_01)


row_02 = np.array([0, 0, 1, 1, 2])
col_02 = np.array([2, 1, 1, 0, 2])
data_02 = np.array([3, 4, 7, 8, 9])
sparse_matrix_02 = csr_matrix((data_02, (row_02, col_02)),shape = (3, 3)).toarray()
print("Second Sparse Matrix : ", sparse_matrix_02)

##add_matrix = sparse_matrix_01 + sparse_matrix_02
##print("Addtion of the two matrices is : ", add_matrix)

subtract_matrix = sparse_matrix_01 - sparse_matrix_02
print("Addtion of the two matrices is : ", subtract_matrix)

print("Transpose of the given matrix is ", sparse_matrix_01.transpose())
        
