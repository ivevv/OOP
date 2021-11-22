from math import sqrt as msqrt, atan, pi, cos, sin
from typing import Union


def sqrt(x):
    if isinstance(x, TComplex):
        return x.sqrt
    return msqrt(x)


class TComplex(object):

    def __init__(
        self,
        real: Union[int, float] = 0,
        imag: Union[int, float] = 0
    ):
        """
        :param real: вещественная часть
        :param imag: мнимая часть компл числа (imaginary part)
        """
        self.real = real
        self.imag = imag

    @property
    def phi(self):  # получение угла fi от компл. числа
        a = self.real
        b = self.imag
        if a > 0 and b > 0:
            return atan(b / a)
        elif a > 0 and b < 0:
            return -atan(b / a)
        elif a < 0 and b > 0:
            return pi-atan(b / a)
        elif a < 0 and b < 0:
            return -pi+atan(b/a)
        elif a == 0 and b > 0:
            return pi/2
        elif a == 0 and b < 0:
            return -pi/2
        elif a > 0 and b == 0:
            return 0
        elif a < 0 and b == 0:
            return pi/2

    @property
    def sqrt(self):
        r = abs(self)
        phi = self.phi
        sr = sqrt(r)
        phi2 = phi/2
        a = sr * cos(phi2)
        b = sr * sin(phi2)
        return TComplex(a, b)

    def __sub__(self, other):
        other = self.check_other(other)
        return TComplex(self.real - other.real, self.imag - other.imag)

    def __neg__(self):
        return TComplex(-self.real, -self.imag)

    def __pow__(self, other: int):
        n = other
        r = abs(self)
        phi = self.phi
        rn = r**n
        nphi = n*phi
        a = rn * cos(nphi)
        b = rn * sin(nphi)
        return TComplex(a, b)

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def __truediv__(self, other):
        other = self.check_other(other)
        a1 = self.real
        b1 = self.imag
        a2 = other.real
        b2 = other.imag
        new_a = (a1*a2+b1*b2)/(a2**2+b2**2)
        new_b = (a2 * b1 - a1 * b2) / (a2 ** 2 + b2 ** 2)
        return TComplex(new_a, new_b)

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
        if self.imag > 0:
            return f'({self.real} + {self.imag}i)'
        elif self.imag < 0:
            return f'({self.real} - {-self.imag}i)'
        return f'{self.real}'

    def check_other(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = TComplex(other, 0)
        if not isinstance(other, TComplex):
            pass
        return other
