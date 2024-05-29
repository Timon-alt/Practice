# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.resize(800, 450)
        MainWindow.setStyleSheet("QWidget {\n"
"   background-color: #70a932\n"
"}\n"
"\n"
"QPushButton {\n"
"   background-color: #25221d;\n"
"   color: #fff;\n"
"   font-weight: 600\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:pressed {\n"
"   background-color: #fff;\n"
"   color: #70a932\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #fff\n"
"}\n"
"\n"
"QLabel {\n"
"   font-weight: 600\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu_widget.setGeometry(QtCore.QRect(0, 0, 211, 451))
        self.menu_widget.setStyleSheet("QWidget {\n"
"    background-color: #25221d\n"
"}\n"
"\n"
"QPushButton {\n"
"    \n"
"}\n"
"\n"
"")
        self.menu_widget.setObjectName("menu_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        self.toolBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet("toolBox {\n"
"}\n"
"\n"
"toolBox QPushButton {\n"
"    color: #fff\n"
"}\n"
"\n"
"toolBox:::QPushButton:hover {\n"
"    background-color: #0b5ed7;\n"
"    \n"
"}\n"
"\n"
"toolBox:::QPushButton: checked {\n"
"    background-color: #fff;\n"
"    color: #70a932\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 193, 379))
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, -5, 201, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    \n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 193, 379))
        self.page_2.setObjectName("page_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 191, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_16 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_2.addWidget(self.pushButton_16)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_2.addWidget(self.pushButton_15)
        self.pushButton_20 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_20.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_2.addWidget(self.pushButton_20)
        self.pushButton_18 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_2.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_19.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_2.addWidget(self.pushButton_19)
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.central_widget = QtWidgets.QWidget(self.centralwidget)
        self.central_widget.setGeometry(QtCore.QRect(210, 0, 591, 451))
        self.central_widget.setObjectName("central_widget")
        self.tabWidget = QtWidgets.QTabWidget(self.central_widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_13.setText(_translate("MainWindow", "Главная"))
        self.pushButton.setText(_translate("MainWindow", "Посмотреть все onu"))
        self.pushButton_2.setText(_translate("MainWindow", "Посмотреть onu на №SFP"))
        self.pushButton_3.setText(_translate("MainWindow", "Состояние SFP"))
        self.pushButton_4.setText(_translate("MainWindow", "Не привязанные ONU"))
        self.pushButton_5.setText(_translate("MainWindow", "Информация по порту"))
        self.pushButton_6.setText(_translate("MainWindow", "Оптический сигнал ONU"))
        self.pushButton_7.setText(_translate("MainWindow", "Оптический сигнал ONU..."))
        self.pushButton_8.setText(_translate("MainWindow", "Обратный уровень ..."))
        self.pushButton_9.setText(_translate("MainWindow", "Обратный уровень..."))
        self.pushButton_10.setText(_translate("MainWindow", "Время работы ONU"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Страница 1"))
        self.pushButton_11.setText(_translate("MainWindow", "Время работы ONU на всей SFP"))
        self.pushButton_12.setText(_translate("MainWindow", "Вкл/выкл CATV"))
        self.pushButton_14.setText(_translate("MainWindow", "Настроенные/онлайн"))
        self.pushButton_16.setText(_translate("MainWindow", "Активность медных портов..."))
        self.pushButton_15.setText(_translate("MainWindow", "Мас с 1 порта ONU"))
        self.pushButton_20.setText(_translate("MainWindow", "ip на ONU"))
        self.pushButton_18.setText(_translate("MainWindow", "Перезагрузка"))
        self.pushButton_19.setText(_translate("MainWindow", "Вкл/выкл медный порт"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Страница 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
