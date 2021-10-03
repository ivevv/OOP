from polinom import TPolinom
from numberh import number


class TApplication:

    check = False

    @staticmethod
    def print_menu():
        print("1. Enter polinom coefficients.")
        print("2. Solve equation.")
        print("3. Input x and calculate polinom.")
        print("4. Print polinom.")
        print("0. Quit.")

    def enter_polinom(self, poli: TPolinom):
        print("Polinom is ax^2 + bx + c")
        a = number(input("a = "))
        while a == 0:
            print("a =/= 0")
            a = number(input("a = "))
        b = number(input("b = "))
        while b == 0:
            print("b =/= 0")
            b = number(input("b = "))
        c = number(input("c = "))
        while c == 0:
            print("c =/= 0")
            c = number(input("c = "))
        poli.set_a(a)
        poli.set_b(b)
        poli.set_c(c)
        self.check = True

    def solve_equation(self, poli: TPolinom):
        if self.check:
            poli.get_discriminant()
            if poli.d >= 0:
                if poli.d != 0:
                    print("x1 = " + repr(poli.get_x1()))
                    print("x2 = " + repr(poli.get_x2()))
                else:
                    print("x = " + repr(poli.get_x1()))
            else:
                print("This equation doesn't have a solution!")
        else:
            print("You need to enter polinom coefficients first!")

    def calculate_polinom(self, poli: TPolinom):
        if self.check:
            x = number(input("x = "))
            while x == 0:
                print("x =/= 0")
                x = number(input("x = "))
            print("Your result: " + repr(poli.calculate_w_x(x)))
        else:
            print("You need to enter polinom coefficients first!")

    def print_polinom(self, poli: TPolinom):
        if self.check:
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
        else:
            print("You need to enter polinom coefficients first!")
