import matrix
import numpy as np

np.random.seed(0)
A = np.random.randint(0, 10, (10, 10))
B = np.random.randint(0, 10, (10, 10))
CC = np.random.randint(0, 10, (10, 10))

CC[0, 0] = A[0, 0]
DD = B.copy()

A = matrix.Matrix(A)
B = matrix.Matrix(B)
C = matrix.Matrix(CC)
D = matrix.Matrix(DD)

AB = A @ B
CD = matrix.Matrix(CC @ DD)

A.save("A.txt")
B.save("B.txt")
C.save("C.txt")
D.save("D.txt")
AB.save("AB.txt")
CD.save("CD.txt")

with open("hash.txt", "w") as f:
    f.write(f"{hash(AB)}\n")
    f.write(f"{hash(CD)}\n")
