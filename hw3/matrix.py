import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        if self.data.ndim != 2:
            raise ValueError("Bad data dimentions")

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Bad matrix size")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Bad matrix size")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Bad matrix size")
        return Matrix(self.data @ other.data)

    def save(self, filename):
        with open(filename, "w") as f:
            for row in self.data:
                f.write(" ".join(map(str, row)) + "\n")
