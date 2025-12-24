import numpy as np

class HashMixin:
    """
    Hash is the first element of the matrix. It is not const :)
    I wanted to used md5, but the second part of the task makes
    it unreasonably hard.
    """
    def __hash__(self):
        return int(self.data[0, 0])

class CacheMatmulMixin:
    _cache = {}

    def matmul_cached(self, other):
        key = (hash(self), hash(other))
        if key in self._cache:
            return self._cache[key]
        res = Matrix(self.data @ other.data)
        self._cache[key] = res
        return res

class Matrix(HashMixin, CacheMatmulMixin):
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
        return self.matmul_cached(other)

    def save(self, filename):
        with open(filename, "w") as f:
            for row in self.data:
                f.write(" ".join(map(str, row)) + "\n")
