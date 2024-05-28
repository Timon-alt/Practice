from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from entryWindow import Ui_Form
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
     super(MyWindow, self).__init__()
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
