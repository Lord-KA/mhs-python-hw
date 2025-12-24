import numpy as np
import matrix

np.random.seed(0)

A = matrix.Matrix(np.random.randint(0, 10, (10, 10)))
B = matrix.Matrix(np.random.randint(0, 10, (10, 10)))

C = A * B
C.save("matrix*.txt")
C = A + B
C.save("matrix+.txt")
C = A @ B
C.save("matrix@.txt")
