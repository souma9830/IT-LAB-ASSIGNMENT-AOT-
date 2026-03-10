# //diagonal sum using numpy

import numpy as np

matrix=np.random.randint(1,10,(3,3))
print("Matrix is :")
print(matrix)
diagonal_sum=np.trace(matrix)
print("The diagonal Sum of the matrix is : ",diagonal_sum)