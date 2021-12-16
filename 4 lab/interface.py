# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
from polinom import TPolinom
from numberh import number


class TInterface(QWidget):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(720, 515)
        font = QtGui.QFont()
        font.setPointSize(14)
        Application.setFont(font)
        self.bracket1 = QtWidgets.QLabel(Application)
        self.bracket1.setGeometry(QtCore.QRect(20, 90, 20, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bracket1.setFont(font)
        self.bracket1.setTextFormat(QtCore.Qt.PlainText)
        self.bracket1.setScaledContents(False)
        self.bracket1.setObjectName("bracket1")
        self.ar = QtWidgets.QLineEdit(Application)  # вещественная часть коэффициента a
        self.ar.setGeometry(QtCore.QRect(30, 100, 61, 41))
        self.ar.setObjectName("ar")
        self.plus1 = QtWidgets.QLabel(Application)
        self.plus1.setGeometry(QtCore.QRect(100, 100, 21, 31))
        self.plus1.setObjectName("plus1")
        self.ai = QtWidgets.QLineEdit(Application)  # мнимая часть коэффициента a
        self.ai.setGeometry(QtCore.QRect(120, 100, 61, 41))
        self.ai.setObjectName("ai")
        self.a_coefficient = QtWidgets.QLabel(Application)
        self.a_coefficient.setGeometry(QtCore.QRect(190, 100, 81, 31))
        self.a_coefficient.setObjectName("a_coefficient")
        self.br = QtWidgets.QLineEdit(Application)  # вещественная часть коэффициента b
        self.br.setGeometry(QtCore.QRect(270, 100, 61, 41))
        self.br.setObjectName("br")
        self.plus2 = QtWidgets.QLabel(Application)
        self.plus2.setGeometry(QtCore.QRect(340, 100, 21, 31))
        self.plus2.setObjectName("plus2")
        self.bi = QtWidgets.QLineEdit(Application)  # мнимая часть коэффициента b
        self.bi.setGeometry(QtCore.QRect(360, 100, 61, 41))
        self.bi.setObjectName("bi")
        self.b_coefficient = QtWidgets.QLabel(Application)
        self.b_coefficient.setGeometry(QtCore.QRect(430, 100, 71, 31))
        self.b_coefficient.setObjectName("b_coefficient")
        self.cr = QtWidgets.QLineEdit(Application)
        self.cr.setGeometry(QtCore.QRect(500, 100, 61, 41))
        self.cr.setObjectName("cr")  # вещественная часть коэффициента c
        self.ci = QtWidgets.QLineEdit(Application)
        self.ci.setGeometry(QtCore.QRect(590, 100, 61, 41))
        self.ci.setObjectName("ci")  # мнимая часть коэффициента c
        self.c_coefficient = QtWidgets.QLabel(Application)
        self.c_coefficient.setGeometry(QtCore.QRect(660, 100, 51, 31))
        self.c_coefficient.setObjectName("c_coefficient")
        self.equal = QtWidgets.QLabel(Application)
        self.equal.setGeometry(QtCore.QRect(20, 160, 51, 31))
        self.equal.setObjectName("equal")
        self.x_label = QtWidgets.QLabel(Application)
        self.x_label.setGeometry(QtCore.QRect(20, 190, 55, 51))
        self.x_label.setObjectName("x_label")
        self.xr = QtWidgets.QLineEdit(Application)
        self.xr.setGeometry(QtCore.QRect(70, 200, 61, 41))
        self.xr.setObjectName("xr")  # вещественная часть параметра x
        self.xi = QtWidgets.QLineEdit(Application)
        self.xi.setGeometry(QtCore.QRect(160, 200, 61, 41))
        self.xi.setObjectName("xi")  # мнимая часть парамметра x
        self.bracket2 = QtWidgets.QLabel(Application)
        self.bracket2.setGeometry(QtCore.QRect(230, 200, 21, 31))
        self.bracket2.setObjectName("bracket2")
        self.solve_btn = QtWidgets.QPushButton(Application)
        self.solve_btn.setGeometry(QtCore.QRect(260, 390, 201, 51))
        self.solve_btn.setObjectName("solve_btn")  # кнопка решения уравнения
        self.calculate_btn = QtWidgets.QPushButton(Application)
        self.calculate_btn.setGeometry(QtCore.QRect(260, 450, 201, 51))
        self.calculate_btn.setObjectName("calculate_btn")  # кнопка вычисления значения многочлена
        self.roots = QtWidgets.QLabel(Application)
        self.roots.setGeometry(QtCore.QRect(20, 250, 91, 41))
        self.roots.setObjectName("roots")
        self.x1_label = QtWidgets.QLabel(Application)
        self.x1_label.setGeometry(QtCore.QRect(20, 290, 55, 51))
        self.x1_label.setObjectName("x1_label")
        self.x2_label = QtWidgets.QLabel(Application)
        self.x2_label.setGeometry(QtCore.QRect(20, 350, 55, 31))
        self.x2_label.setObjectName("x2_label")
        self.value = QtWidgets.QLabel(Application)  # поле вывода значения многочлена
        self.value.setGeometry(QtCore.QRect(40, 150, 661, 51))
        self.value.setText("")
        self.value.setObjectName("value")
        self.plus3 = QtWidgets.QLabel(Application)
        self.plus3.setGeometry(QtCore.QRect(570, 100, 21, 31))
        self.plus3.setObjectName("plus3")
        self.plus4 = QtWidgets.QLabel(Application)
        self.plus4.setGeometry(QtCore.QRect(140, 200, 21, 31))
        self.plus4.setObjectName("plus4")
        self.x1 = QtWidgets.QLabel(Application)  # поле вывода первого корня
        self.x1.setGeometry(QtCore.QRect(80, 290, 621, 51))
        self.x1.setText("")
        self.x1.setObjectName("x1")
        self.x2 = QtWidgets.QLabel(Application)  # поле вывода второго корня
        self.x2.setGeometry(QtCore.QRect(80, 340, 621, 51))
        self.x2.setText("")
        self.x2.setObjectName("x2")
        self.mode_box = QtWidgets.QGroupBox(Application)
        self.mode_box.setGeometry(QtCore.QRect(10, 10, 681, 80))
        self.mode_box.setObjectName("mode_box")
        self.real_btn = QtWidgets.QRadioButton(self.mode_box)  # кнопка выбора режима вещественных чисел
        self.real_btn.setGeometry(QtCore.QRect(70, 30, 171, 31))
        self.real_btn.setChecked(True)
        self.real_btn.setObjectName("real_btn")
        self.complex_btn = QtWidgets.QRadioButton(self.mode_box)  # кнопка выбора режима комплексных чисел
        self.complex_btn.setGeometry(QtCore.QRect(420, 30, 211, 31))
        self.complex_btn.setChecked(False)
        self.complex_btn.setObjectName("complex_btn")
        self.bracket1.raise_()
        self.ar.raise_()
        self.plus1.raise_()
        self.ai.raise_()
        self.a_coefficient.raise_()
        self.br.raise_()
        self.plus2.raise_()
        self.bi.raise_()
        self.b_coefficient.raise_()
        self.cr.raise_()
        self.ci.raise_()
        self.c_coefficient.raise_()
        self.equal.raise_()
        self.x_label.raise_()
        self.xr.raise_()
        self.xi.raise_()
        self.bracket2.raise_()
        self.solve_btn.raise_()
        self.calculate_btn.raise_()
        self.roots.raise_()
        self.x1_label.raise_()
        self.x2_label.raise_()
        self.plus3.raise_()
        self.value.raise_()
        self.plus4.raise_()
        self.x1.raise_()
        self.x2.raise_()
        self.mode_box.raise_()

        self.retranslateUi(Application)
        QtCore.QMetaObject.connectSlotsByName(Application)

        self.run()

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "Polinom application"))
        self.bracket1.setText(_translate("Application", "("))
        self.plus1.setText(_translate("Application", "+"))
        self.a_coefficient.setText(_translate("Application", "i)x² + ("))
        self.plus2.setText(_translate("Application", "+"))
        self.b_coefficient.setText(_translate("Application", "i)x + ("))
        self.c_coefficient.setText(_translate("Application", "i) ="))
        self.equal.setText(_translate("Application", "="))
        self.x_label.setText(_translate("Application", "x = ("))
        self.bracket2.setText(_translate("Application", "i)"))
        self.solve_btn.setText(_translate("Application", "solve equation"))
        self.calculate_btn.setText(_translate("Application", "calculate polinom"))
        self.x1_label.setText(_translate("Application", "x1 ="))
        self.x2_label.setText(_translate("Application", "x2 ="))
        self.plus3.setText(_translate("Application", "+"))
        self.plus4.setText(_translate("Application", "+"))
        self.roots.setText(_translate("Application", "Roots:"))
        self.mode_box.setTitle(_translate("Application", "Mode:"))
        self.real_btn.setText(_translate("Application", "real numbers"))
        self.complex_btn.setText(_translate("Application", "complex numbers"))

    # названия полей и кнопок:

    # real_btn - кнопка режима вещественных чисел
    # complex_btn - кнопка режима комплексных чисел
    # ar, ai - вещественная и мнимая часть a;
    # br, bi - вещественная и мнимая часть b;
    # cr, ci - вещественная и мнимая часть c;
    # xr, xi - вещественная и мнимая часть x;
    # solve_btn - кнопка решения уравнения;
    # calculate_btn - кнопка вычисления значения многочлена;
    # value - поле вывода значения многочлена;
    # x1, x2 - поля вывода корней.

    def run(self):
        self.solve_btn.clicked.connect(self.solve_equation)
        self.calculate_btn.clicked.connect(self.calculate_polinom)

    def solve_equation(self):
        try:
            r = self.ar.text()
            i = self.ai.text()
            a = number(float(r), float(i))
            r = self.br.text()
            i = self.bi.text()
            b = number(float(r), float(i))
            r = self.cr.text()
            i = self.ci.text()
            c = number(float(r), float(i))
            polinom = TPolinom(a, b, c)
            d = polinom.d()
            if d == 0:
                x, _ = polinom.get_roots()
                self.x1.setText(str(x))
                self.x2.setText("no root")
            else:
                x1, x2 = polinom.get_roots()
                self.x1.setText(str(x1))
                self.x2.setText(str(x2))
            self.value.clear()
        except Exception:
            QMessageBox.warning(self, "Error", "You need to enter coefficients first!")

    def calculate_polinom(self):
        try:
            r = self.ar.text()
            i = self.ai.text()
            a = number(float(r), float(i))
            r = self.br.text()
            i = self.bi.text()
            b = number(float(r), float(i))
            r = self.cr.text()
            i = self.ci.text()
            c = number(float(r), float(i))
            r = self.xr.text()
            i = self.xi.text()
            x = number(float(r), float(i))
            polinom = TPolinom(a, b, c)
            value = polinom.get_value(x)
            self.value.setText(str(value))
            self.x1.clear()
            self.x2.clear()
        except Exception:
            QMessageBox.warning(self, "Error", "You need to enter coefficients and x first!")
