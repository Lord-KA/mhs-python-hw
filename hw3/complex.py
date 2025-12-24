import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class ComplexFieldMixin:
    @property
    def z(self) -> complex:
        return self._z

    @z.setter
    def z(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            value = complex(value[0], value[1])

        self._z = complex(value)

    @property
    def re(self) -> float:
        return self._z.real

    @re.setter
    def re(self, value):
        self._z = complex(value, self._z.imag)

    @property
    def im(self) -> float:
        return self._z.imag

    @im.setter
    def im(self, value):
        self._z = complex(self._z.real, value)


class PrettyStrMixin:
    def __str__(self):
        sign = "+" if self.im >= 0 else "-"
        return f"{self.re:g} {sign} {abs(self.im):g}j"


class FileSaveMixin:
    def save(self, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(self) + "\n")


class MatmulAsMulMixin:
    def __matmul__(self, other):
        return self * other


class Complex(MatmulAsMulMixin, NDArrayOperatorsMixin, ComplexFieldMixin, PrettyStrMixin, FileSaveMixin):
    __array_priority__ = 1000

    def __init__(self, z):
        self.z = z

    def __array__(self, dtype=None):
        return np.asarray(self._z, dtype=dtype)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        in_vals = [x._z if isinstance(x, Complex) else x for x in inputs]

        if "out" in kwargs and kwargs["out"] is not None:
            return NotImplemented

        result = getattr(ufunc, method)(*in_vals, **kwargs)
        return Complex(result)
