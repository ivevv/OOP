from math import sqrt
from typing import Union


class TComplex(object):
    def __new__(
        cls,
        real: Union[int, float] = 0,
        imag: Union[int, float] = 0,
    ):
        return complex(real, imag)

    def __init__(
        self,
        real: Union[int, float] = 0,
        imag: Union[int, float] = 0,
    ):
        """
        :param real: вещественная часть
        :param imag: мнимая часть компл числа (imaginary part)
        """
        self.real = real
        self.imag = imag

    def __sub__(self, other):
        other = self.check_other(other)
        return TComplex(self.real - other.real, self.imag - other.imag)

    # нужно ещё перегрузить pow, добавить метод sqrt

    def __pow__(self, other):
        other = self.check_other(other)

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def __add__(self, other):
        other = self.check_other(other)
        return TComplex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        other = self.check_other(other)
        return TComplex(self.real * other.real - self.imag * other.imag,
                        self.imag * other.real + self.real * other.imag)

    def __eq__(self, other):
        other = self.check_other(other)
        return (self.real == other.real) and (self.imag == other.imag)

    # т.к. интересуют только знаки перед всем числом
    def __gt__(self, other):
        other = self.check_other(other)
        return self.real > other.real

    def __lt__(self, other):
        other = self.check_other(other)
        return self.real < other.real

    def __str__(self):
        s = f'({self.real}'
        if self.imag > 0:
            s += f' + {self.imag}i)'
        else:
            s += f' {self.imag}i)'
        return s

    def check_other(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = TComplex(other)
        if not isinstance(other, TComplex):
            pass
        return other
