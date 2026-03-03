# Perform the following operations using Numpy:
# a) Construct a Python program using NumPy to generate a 4x4 identity matrix.
import numpy as np
I = np.zeros((4,4))
for i in range(4):
    I[i][i] = 1
print(I)


# Develop a Python program to generate two 3x3 matrices filled with random integers (1 to 9), then perform matrix addition and matrix multiplication.
import numpy as np
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

print("A: ", A)
print("B: ", B)

print("Addition: ", A + B)

print("Multiplication: ", A@B)
