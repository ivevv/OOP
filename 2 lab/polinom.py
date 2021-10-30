from complex import sqrt
from numberh import number


class TPolinom:
    def __init__(self, a: number, b: number, c: number):
        self.a = a
        self.b = b
        self.c = c

    def d(self):
        return self.b**2-self.a*4*self.c

    def get_roots(self):
        d = sqrt(self.d())
        x1 = (-self.b+d)/(self.a*2)
        x2 = (-self.b-d)/(self.a*2)
        return x1, x2

    def get_value(self, x):
        value = self.a * x ** 2 + self.b * x + self.c
        return value

    def __str__(self):
        return f'{self.a}x² + {self.b}x + {self.c}'






