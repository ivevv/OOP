import math


# polinom: ax^2 + bx + c = 0
class TPolinom:
    d = 0.0
    # a = 0.0
    # b = 0.0
    # c = 0.0

    def __init__(self, a, b, c):
        # might put these as class attributes instead, haven't decided yet
        self.a = a
        self.b = b
        self.c = c

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def get_discriminant(self):
        self.d = math.sqrt(self.b) + 4 * self.a * self.c
        if self.d < 0:
            return False
        else:
            return True

    def get_x1(self):
        x1 = (self.d - self.b) / (2 * self.a)
        return x1

    def get_x2(self):
        x2 = (0 - self.d - self.b) / (2 * self.a)
        return x2

    # temporary name
    def solve(self, x):
        s = self.a * math.pow(x, 2) + self.b * x + self.c
        return s
