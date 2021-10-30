from math import sqrt as msqrt
from numberh import number


def sqrt(x):
    if isinstance(x, number):
        return x.sqrt
    return msqrt(x)


class TPolinom:
    def __init__(self, a: number, b: number, c: number):
        self.a = a
        self.b = b
        self.c = c

    def d(self):
        return number(self.b**2-self.a*4*self.c)

    def get_roots(self):
        d = sqrt(self.d())
        x1 = (-self.b+d)/(2*self.a)
        x2 = (-self.b-d)/(2*self.a)
        return x1, x2

    def get_value(self, x):
        value = self.a * x ** 2 + self.b * x + self.c
        return value

    def __str__(self):
        return f'{self.a}x² + {self.b}x + {self.c}'






