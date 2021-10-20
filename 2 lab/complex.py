class TComplex(object):
    def __init__(self, real=0, imag=0):
        """
        :param real: вещественная часть
        :param imag: мнимая часть компл числа (imaginary part)
        """
        self.real = real
        self.imag = imag

    def __sub__(self, other):
        return TComplex(self.real - other.real, self.imag - other.imag)

