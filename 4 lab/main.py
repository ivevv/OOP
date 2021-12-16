from interface import TInterface
from PyQt5 import QtWidgets


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QWidget()
    ui = TInterface()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())
