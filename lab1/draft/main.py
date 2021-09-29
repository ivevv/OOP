from application import TApplication
from polinom import TPolinom

poli_check = False  # to check if polinom was initialised, if not - run enter_polinom()
poli = TPolinom()

TApplication.print_menu()
opt = int(input("Enter option: "))

while opt != 0:
    if opt == 1:
        poli_check = TApplication.enter_polinom(poli)
    elif opt == 2:
        if poli_check:
            TApplication.solve_equation(poli)
        else:
            poli_check = TApplication.enter_polinom(poli)
            TApplication.solve_equation(poli)
    elif opt == 3:
        if poli_check:
            TApplication.calculate_polinom(poli)
        else:
            poli_check = TApplication.enter_polinom(poli)
            TApplication.calculate_polinom(poli)
    elif opt == 4:
        if poli_check:
            TApplication.print_polinom(poli)
        else:
            poli_check = TApplication.enter_polinom(poli)
            TApplication.print_polinom(poli)
    else:
        print("Invalid option!")
    print()
    TApplication.print_menu()
    opt = int(input("Enter option: "))
