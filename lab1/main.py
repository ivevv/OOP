from application import TApplication
from polinom import TPolinom

poli = TPolinom()
app = TApplication()
app.print_menu()
opt = int(input("Enter option: "))

while opt != 0:
    if opt == 1:
        app.enter_polinom(poli)
    elif opt == 2:
        app.solve_equation(poli)
    elif opt == 3:
        app.calculate_polinom(poli)
    elif opt == 4:
        app.print_polinom(poli)
    else:
        print("Invalid option!")
    print()
    app.print_menu()
    opt = int(input("Enter option: "))
