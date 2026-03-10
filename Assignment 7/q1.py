# Using NumPy:
# (Note: At first, do it without NumPy. Then do it again with NumPy.)
# 1. Write a Python program to create a 3X3 Matrix randomly and calculate the sum of the
# diagonal elements.

matrix=[]
print("Enter the matrix element : ")
for i in range(3):
    rows=[]
    for j in range(3):
        x=int(input())
        rows.append(x)
    matrix.append(rows)

print("matrix")
for row in matrix:
    print(row)
diagonal=0
for i in range(3):
    diagonal=diagonal+matrix[i][i]
print("Sum of diagonal elements:", diagonal)
