from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InputMrch(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_InputMrch, self).__init__(parent)

        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 30, 331, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 311, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reason"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(710, 233)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(40, 80, 180, 45))
        self.addBtn.setObjectName("addBtn")

        self.viewBtn = QtWidgets.QPushButton(self.centralwidget)
        self.viewBtn.setGeometry(QtCore.QRect(270, 80, 180, 45))
        self.viewBtn.setObjectName("viewBtn")

        self.removeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtn.setGeometry(QtCore.QRect(500, 80, 180, 45))
        self.removeBtn.setObjectName("removeBtn")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.setStyle()

        self.addBtn.clicked.connect(self.onAddButtonClick)
        self.viewBtn.clicked.connect(self.onViewButtonClick)
        self.removeBtn.clicked.connect(self.onRemoveButtonClick)
        QtCore.QMetaObject.connectSlotsByName(self)

    def onAddButtonClick(self):
        print("Add Clicked")
        self.hide()
        self.window_InputMrch = QtWidgets.QMainWindow()
        self.window_InputMrch = Ui_InputMrch()
        self.window_InputMrch.show()

    def onViewButtonClick(self):
        print("View Clicked")

    def onRemoveButtonClick(self):
        print("Remove Clicked")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Select Option"))
        self.addBtn.setText(_translate("MainWindow", "Add Merchants"))
        self.viewBtn.setText(_translate("MainWindow", "View Merchants"))
        self.removeBtn.setText(_translate("MainWindow", "Remove Merchants"))

    def setStyle(self):
        self.setStyleSheet("background-color: #d8f6ff;")

        self.addBtn.setStyleSheet("background-color: #2b5869;\n"
                                  "font-family: Arial;\n"
                                  "font-size: 18px;\n"
                                  "font-weight: bold;\n"
                                  "color: #a9f1f6;\n"
                                  "border-radius: 5px"
                                  "}")
        self.viewBtn.setStyleSheet("background-color: #2b5869;\n"
                                   "font-family: Arial;\n"
                                   "font-size: 18px;\n"
                                   "font-weight: bold;\n"
                                   "color: #a9f1f6;\n"
                                   "border-radius: 5px"
                                   "}")

        self.removeBtn.setStyleSheet("background-color: #2b5869;\n"
                                     "font-family: Arial;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;\n"
                                     "color: #a9f1f6;\n"
                                     "border-radius: 5px"
                                     "}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
