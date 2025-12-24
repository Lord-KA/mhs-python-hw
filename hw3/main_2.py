import numpy as np
from complex import Complex

if __name__ == "__main__":
    np.random.seed(0)
    a, b, c, d = np.random.randint(0, 10, 4)

    A = Complex((a, b))
    B = Complex((c, d))

    C = A + B
    C.save("complex+.txt")
    C = A * B
    C.save("complex*.txt")
    C = A @ B
    C.save("complex@.txt")
