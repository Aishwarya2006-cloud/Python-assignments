"""Develop a NumPy program to multiply a 5X3 matrix by a 3X2 matrix and create a product matrix, also print the product matrix. Take input data from user."""

import numpy as np

print("Enter 15 elements for 5x3 matrix:")
A = np.zeros((5, 3), dtype=int)
for i in range(5):
    for j in range(3):
        A[i][j] = int(input("Enter element of [%d][%d] "%(i,j)))

print("Enter 6 elements for 3x2 matrix:")
B = np.zeros((3, 2), dtype=int)
for i in range(3):
    for j in range(2):
        B[i][j] = int(input("Enter element of [%d][%d] "%(i,j)))

C = A @ B
print("A:\n",A)
print()
print("B:\n",B)
print()
print("Product Matrix:")
print(C)