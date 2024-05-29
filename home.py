from pages.homePage import Ui_Form
from PyQt5.QtWidgets import QWidget

class Home():
    def __init__(self):
        super(Home, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)