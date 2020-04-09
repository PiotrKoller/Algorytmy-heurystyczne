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
        self.entropia = entropy
        self.max_entropy_value()
        self.class_spinbox.valueChanged.connect(self.max_entropy_changed)
        self.run_button.clicked.connect(self.run)

    def run(self):
        self.ent = self.entropy_line.text()
        self.class_num = self.class_spinbox.value()
        self.x = self.entropy_line_2.text()
        self.y = self.entropy_line_3.text()
        self.error_dialog = self.ui.error_dialog
        try:
            self.entropia.entropy(self,self.class_num,self.x,self.y,self.ent)
        except:
            self.error_dialog.showMessage("Zbyt duża wartość.")

    def max_entropy_value(self):
        self.max = self.entropia.max_entropy(self,2,10,10)
        text = "Maksymalna entropia: " + str(round(self.max,2))
        self.entropy_line.setPlaceholderText(text)

    def max_entropy_changed(self):
        self.x = self.entropy_line_2.text()
        self.y = self.entropy_line_3.text()
        self.class_num = self.class_spinbox.value()
        try:
            self.max = self.entropia.max_entropy(self,self.class_num,self.x,self.y)
        except:
            self.error_dialog.showMessage("Ustaw rozmiar obrazu.")
        text = "Maksymalna entropia: " + str(round(self.max,2))
        self.entropy_line.setPlaceholderText(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())