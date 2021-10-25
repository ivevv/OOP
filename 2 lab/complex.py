class TComplex(object):
    def __init__(self, real=0, imag=0):  # можно использовать real: int, imag: int (или float)?
        """
        :param real: вещественная часть
        :param imag: мнимая часть компл числа (imaginary part)
        """
        self.real = real
        self.imag = imag

    def __sub__(self, other):
        return TComplex(self.real - other.real, self.imag - other.imag)
    
    # нужно ещё перегрузить pow, добавить метод sqrt

    def __add__(self, other):
        return TComplex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return TComplex(self.real * other.real - self.imag * other.imag,
                        self.imag * other.real + self.real * other.imag)

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)

    # т.к. интересуют только знаки перед всем числом
    def __gt__(self, other):
        return self.real > other.real

    def __lt__(self, other):
        return self.real < other.real

    def __str__(self):
        s = f'({self.real}'
        if self.imag > 0:
            s += f' + {self.imag}i)'
        else:
            s += f' {self.imag}i)'
        return s

