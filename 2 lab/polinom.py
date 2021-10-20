from math import sqrt
from complex import TComplex


class TPolinom:
    def __init__(self, a, b, c):
        self.a = TComplex(a)
        self.b = TComplex(b)
        self.c = TComplex(c)

    def d(self):
        return self.b**2-4*self.a*self.c

    def get_roots(self):
        d = sqrt(self.d())
        x1 = (-self.b+d)/2*self.a
        x2 = (-self.b-d)/2*self.a
        return x1, x2

    def get_value(self, x):
        value = self.a * x ** 2 + self.b * x + self.c
        return value

    def __str__(self):
        return f'{self.a}x² + {self.b}x + {self.c}'






