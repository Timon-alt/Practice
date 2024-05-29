from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from entryWindow import Ui_Form
from home import Home
import sys



class MyWindow(QtWidgets.QWidget):
    def __init__(self):
     super(MyWindow, self).__init__()
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)

     # Get all object in windows
     self.home_btn = self.ui.pushButton_13

     # Create dict for menu buttons and tab windows
     self.menu_btns_dict = {
        self.home_btn: Home
     }

     # show home window when start app
     self.show_home_window()

     # connect signal and slot 
     #self.home_btn.clicked.connect(self.show)

    def show_home_window(self):
       """
       function for showing home window
       :return:
       """
       result = self.open_tab_flag(self.home_btn.text())
       self.set_btn_checked(self.home_btn)

       if result[0]:
          self.ui.tabWidget.setCurrentIndex(result[1])
       else:
          tab_title = self.home_btn.text()
          curIndex = self.ui.tabWidget.addTab(Home(), tab_title)
          self.ui.tabWidget.setCurrentIndex(curIndex)
          self.ui.tabWidget.setVisible(True)


    def set_btn_checked(self, btn):
       """
       Set the status of selected button checked and set other button's
       status unchecked
       :param btn: button object
       :return:
       """

       for button in self.menu_btns_dict.keys():
          if button != btn:
             button.setChecked(False)
          else:
             button.setChecked(True)

    def open_tab_flag(self, btn_text):
       """
       Check if selected window showed or not
       :param btn_text: button text
       :return: bool and index
       """
       open_tab_count = self.ui.tabWidget.count()

       for i in range(open_tab_count):
          tab_title = self.ui.tabWidget.tabText(i)
          if tab_title == btn_text:
             return True, i
          else:
             continue
          
       return False,
     

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
