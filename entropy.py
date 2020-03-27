import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from app import Ui_MainWindow
from entropia import entropy

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.run_button = self.ui.run_button
        self.entropy_line = self.ui.entropy_line
        self.entropy_line_2 = self.ui.entropy_line_2
        self.entropy_line_3 = self.ui.entropy_line_3
        self.class_spinbox = self.ui.class_spinbox
        self.run_button.clicked.connect(self.run)

    def run(self):
        self.ent = self.entropy_line.text()
        self.class_num = self.class_spinbox.value()
        self.x = self.entropy_line_2.text()
        self.y = self.entropy_line_3.text()
        self.entropia = entropy
        self.entropia.entropy(self,self.class_num,self.x,self.y,self.ent)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())