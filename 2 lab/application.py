from polinom import TPolinom


class TApplication:
    def __init__(self):
        self.menu_text = (
            '1. Enter polinom coefficients.\n'
            '2. Solve equation.\n'
            '3. Input x and calculate polinom.\n'
            '4. Print polinom.\n'
            '0. Exit.\n'
        )
        self.option = ''
        self.polinom = None

    def run(self):
        while True:
            self.print_menu()
            self.get_input()
            if self.option == '0':
                break
            self.run_command()

    def print_menu(self):
        print(self.menu_text)

    def get_input(self):
        self.option = input('Input: ')

    def run_command(self):
        if self.polinom is None and self.option != '1':
            print('=====> You must input polinom coefficients first')
            return

        if self.option == '1':
            self.enter_polinom()
        elif self.option == '2':
            self.solve_equation()
        elif self.option == '3':
            x = int(input('x = '))
            self.calculate_polinom(x)
        elif self.option == '4':
            print(self.polinom)
        else:
            print('=====> Unknown option')

    def enter_polinom(self):
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))
        self.polinom = TPolinom(a, b, c)

    def solve_equation(self):
        d = self.polinom.d()
        if d < 0:
            print('Discriminant is less than zero, there is no solution')
        elif d == 0:
            x, _ = self.polinom.get_roots()
            print('x1 = x2 =', x)
        elif d > 0:
            x1, x2 = self.polinom.get_roots()
            print('x1 =', x1)
            print('x2 =', x2)

    def calculate_polinom(self, x):
        value = self.polinom.get_value(x)
        print(f'Value of polinom {self.polinom} with x={x} is {value}')

    def print_polinom(self):
        print(self.polinom)



