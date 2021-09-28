from polinom import TPolinom


class TApplication:

    @staticmethod
    def print_menu():
        print("1. Enter polinom coefficients.")
        print("2. Solve equation.")
        print("3. Input x and solve polinom.")
        print("4. Print polinom.")
        print("5. Quit.")

    @staticmethod
    def enter_polinom(poli: TPolinom):
        print("Polinom is a*x^2 + b*x + c")
        print("a = ")
        a = float(input())  # check if a =/= 0
        print("b = ")
        b = float(input())  # check if b =/=0
        print("c = ")
        c = float(input())  # check if c =/= 0
        poli.set_a(a)
        poli.set_b(b)
        poli.set_c(c)

    @staticmethod
    def get_unknowns(poli: TPolinom):
        x1 = poli.get_x1()
        x2 = poli.get_x2()
        s = "x1 = " + repr(x1)
        print(s)
        s = "x2 = " + repr(x2)
        print(s)

    @staticmethod
    def solve_polinom(poli: TPolinom):
        print("x = ")
        x = float(input())
        s = poli.solve(x)
        print(repr(s))

    @staticmethod
    def print_polinom(poli: TPolinom):
        pass
