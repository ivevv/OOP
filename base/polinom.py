from math import sqrt
from numberh import number


class TPolinom:
    def __init__(self, a: number, b: number, c: number):
        self.a = a
        self.b = b
        self.c = c

    def d(self):
        return self.b**2-4*self.a*self.c

    def get_roots(self):
        d = sqrt(self.d())
        x1 = (-self.b + d)/2*self.a
        x2 = (-self.b - d)/2*self.a
        return x1, x2

    def get_value(self, x):
        value = self.a * x ** 2 + self.b * x + self.c
        return value

    def __str__(self):
        s = f'{self.a}x²'
        if self.b > 0:
            s += f' + {self.b}x '
        else:
            s += f' {self.b}x'
        if self.c > 0:
            s += f' + {self.c}'
        else:
            s += f' {self.c}'
        return s






