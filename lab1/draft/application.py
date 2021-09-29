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
        while a == 0:
            print("a =/= 0")
            print("a = ")
            a = float(input())
        print("b = ")
        b = float(input())  # check if b =/= 0
        while b == 0:
            print("b =/= 0")
            print("b = ")
            b = float(input())
        print("c = ")
        c = float(input())  # check if c =/= 0
        while c == 0:
            print("c =/= 0")
            print("c = ")
            c = float(input())
        poli.set_a(a)
        poli.set_b(b)
        poli.set_c(c)

    @staticmethod
    def get_unknowns(poli: TPolinom):
        check = poli.get_discriminant()
        if check:
            print("x1 = " + repr(poli.get_x1()))
            print("x2 = " + repr(poli.get_x2()))
        else:
            print("This equation doesn't have a solution!")

    @staticmethod
    def solve_polinom(poli: TPolinom):
        print("x = ")
        x = float(input())
        while x == 0:
            print("x =/= 0")
            print("x = ")
            x = float(input())
        print("Your result: " + repr(poli.solve(x)))

    @staticmethod
    def print_polinom(poli: TPolinom):
        s = repr(poli.a) + "x^2 "
        if poli.b > 0:
            s += "+" + repr(poli.b) + "x "
        else:
            s += repr(poli.b) + "x "
        if poli.c > 0:
            s += "+" + repr(poli.c)
        else:
            s += repr(poli.c)
        print(s)
