# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pittb\Documents\algorytmy_heur\Algorytmy-heurystyczne\entropia.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(266, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.class_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.class_label_2.setGeometry(QtCore.QRect(20, 20, 239, 57))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.class_label_2.setFont(font)
        self.class_label_2.setObjectName("class_label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 90, 231, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.entropy_line_2 = QtWidgets.QLineEdit(self.widget)
        self.entropy_line_2.setObjectName("entropy_line_2")
        self.horizontalLayout.addWidget(self.entropy_line_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.entropy_line_3 = QtWidgets.QLineEdit(self.widget)
        self.entropy_line_3.setObjectName("entropy_line_3")
        self.horizontalLayout.addWidget(self.entropy_line_3)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(11, 141, 231, 211))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.class_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.class_label.setFont(font)
        self.class_label.setObjectName("class_label")
        self.verticalLayout.addWidget(self.class_label)
        self.class_spinbox = QtWidgets.QSpinBox(self.widget1)
        self.class_spinbox.setMinimum(2)
        self.class_spinbox.setObjectName("class_spinbox")
        self.verticalLayout.addWidget(self.class_spinbox)
        self.entropy_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entropy_label.setFont(font)
        self.entropy_label.setObjectName("entropy_label")
        self.verticalLayout.addWidget(self.entropy_label)
        self.entropy_line = QtWidgets.QLineEdit(self.widget1)
        self.entropy_line.setObjectName("entropy_line")
        self.verticalLayout.addWidget(self.entropy_line)
        self.run_button = QtWidgets.QPushButton(self.widget1)
        self.run_button.setObjectName("run_button")
        self.verticalLayout.addWidget(self.run_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 266, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.class_label_2.setText(_translate("MainWindow", "Wybierz rozmiar obrazu:"))
        self.label.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))
        self.class_label.setText(_translate("MainWindow", "Wybierz liczbę klas:"))
        self.entropy_label.setText(_translate("MainWindow", "Wpisz wartość entropii:"))
        self.run_button.setText(_translate("MainWindow", "Uruchom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
