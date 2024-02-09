from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewMrch(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_ViewMrch, self).__init__(parent)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(10, 10, 1200, 740)
        self.frame.setObjectName('frame')


class Ui_InputMrch(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_InputMrch, self).__init__(parent)
        self.setObjectName("InputMrchWindow")
        # self.resize(800, 600)
        self.setGeometry(250, 80, 1500, 900)
        self.setFixedSize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setStyleSheet("background-color: red;")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 710, 820))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame.setStyleSheet("background-color: black;")
        self.frame.setObjectName("frame")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 690, 800))
        # self.tableWidget.setStyleSheet("background-color: yellow;")
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        # self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(690, 800))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Merchant Number", "Reason"])
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 390)

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(1)

        self.addRow = QtWidgets.QPushButton(self.centralwidget)
        self.addRow.setGeometry(QtCore.QRect(20, 5, 160, 45))
        self.addRow.setObjectName("addRow")

        self.removeRow = QtWidgets.QPushButton(self.centralwidget)
        self.removeRow.setGeometry(QtCore.QRect(191, 5, 160, 45))
        self.removeRow.setObjectName("removeRow")

        self.viewDetails = QtWidgets.QPushButton(self.centralwidget)
        self.viewDetails.setGeometry(QtCore.QRect(540, 5, 160, 45))
        self.viewDetails.setObjectName("viewDetails")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.setStyleInputMrch()

        self.addRow.clicked.connect(self.onAddRowButtonClick)
        self.removeRow.clicked.connect(self.onRemoveButtonClick)
        self.viewDetails.clicked.connect(self.onViewDetailsButtonClick)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("InputMrchWindow", "MainWindow"))
        self.addRow.setText(_translate("InputMrchWindow", "Add Row"))
        self.removeRow.setText(_translate("InputMrchWindow", "Remove Row"))
        self.viewDetails.setText(_translate("InputMrchWindow", "View Details"))

    def setStyleInputMrch(self):
        self.setStyleSheet("background-color: #d8f6ff;")

        self.addRow.setStyleSheet("background-color: #2b5869;\n"
                                  "font-family: Arial;\n"
                                  "font-size: 18px;\n"
                                  "font-weight: bold;\n"
                                  "color: #a9f1f6;\n"
                                  "border-radius: 5px"
                                  "}")

        self.removeRow.setStyleSheet("background-color: #2b5869;\n"
                                     "font-family: Arial;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;\n"
                                     "color: #a9f1f6;\n"
                                     "border-radius: 5px"
                                     "}")

        self.viewDetails.setStyleSheet("background-color: #2b5869;\n"
                                       "font-family: Arial;\n"
                                       "font-size: 18px;\n"
                                       "font-weight: bold;\n"
                                       "color: #a9f1f6;\n"
                                       "border-radius: 5px"
                                       "}")

        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 150);")

        self.tableWidget.setStyleSheet("QTableWidget{\n"
                                       "background-color: white;\n"
                                       "alternate-background-color: white;\n"
                                       "border-style: none;\n"           
                                       "gridline-style: none;\n"
                                       "border:1px solid black"
                                       "\n"
                                       "}\n"

                                       "QTableWidget::item{\n"
                                       "font-family: Arial;\n"
                                       "font-size: 1px;\n"
                                       "background-color: #DDDDDD;\n"
                                       "border: 1px solid black;\n"
                                       "padding: 0px;\n"
                                       "color:black;\n"                            
                                       "}\n"

                                       "QTableWidget::item:selected{\n"
                                       "background-color: #EAEAEA;\n"
                                       "font-family: Arial;\n"
                                       "font-size: 15px;\n"
                                       "font-weight: bold;\n"
                                       "padding: 0px;\n"
                                       "color: black;\n"
                                       "}")

        self.tableWidget.horizontalHeader().setStyleSheet("""
                                        QHeaderView::section {
                                        background-color: #1b2027;  /*#1b2027*/
                                        color: white;  
                                        font-family: Arial;  
                                        font-weight: bold;  
                                        }""")

        self.tableWidget.verticalHeader().setStyleSheet("""
                                        QHeaderView::section {
                                        background-color: #1b2027;  
                                        color: white;  
                                        font-family: Arial;  
                                        font-weight: bold;  
                                        }""")


    def onAddRowButtonClick(self):
        # print("Test")
        current_row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(current_row_count)

    def onRemoveButtonClick(self):
        if self.tableWidget.rowCount() > 1:
            selected_row = self.tableWidget.currentRow()
            if selected_row >= 0:
                self.tableWidget.removeRow(selected_row)

    def onViewDetailsButtonClick(self):
        # print("Test")

        for row in range(self.tableWidget.rowCount()):
            item1 = self.tableWidget.item(row, 0)
            item2 = self.tableWidget.item(row, 1)
            if item1 is not None and item2 is not None:
                id = self.tableWidget.item(row, 0).text()
                reason = self.tableWidget.item(row, 1).text()
                print(id, reason)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        # self.resize(710, 233)
        self.setGeometry(250, 80, 1500, 900)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.topFrame = QtWidgets.QFrame(self.centralwidget)
        self.topFrame.setGeometry(10, 30, 1480, 55)
        self.topFrame.setObjectName('topFrame')
        # self.topFrame.setStyleSheet("border: 1px solid black;")

        self.bottomFrame = QtWidgets.QFrame(self.centralwidget)
        self.bottomFrame.setGeometry(10, 95, 1480, 760)
        self.topFrame.setObjectName('bottomFrame')
        # self.bottomFrame.setStyleSheet("border: 1px solid black;")

        self.addBtn = QtWidgets.QPushButton('Add', self.topFrame)
        self.addBtn.setGeometry(QtCore.QRect(10, 5, 180, 45))
        self.addBtn.setObjectName("addBtn")

        self.viewBtn = QtWidgets.QPushButton('View', self.topFrame)
        self.viewBtn.setGeometry(QtCore.QRect(250, 5, 180, 45))
        self.viewBtn.setObjectName("viewBtn")

        self.removeBtn = QtWidgets.QPushButton('Remove', self.topFrame)
        self.removeBtn.setGeometry(QtCore.QRect(500, 5, 180, 45))
        self.removeBtn.setObjectName("removeBtn")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.setStyle()
        self.pulldata()

        self.addBtn.clicked.connect(self.onAddButtonClick)
        self.viewBtn.clicked.connect(self.onViewButtonClick)
        self.removeBtn.clicked.connect(self.onRemoveButtonClick)
        QtCore.QMetaObject.connectSlotsByName(self)

    def pulldata(self):
        self.tableWidget = QtWidgets.QTableWidget(self.bottomFrame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1450, 740))

        self.tableWidget.setMaximumSize(QtCore.QSize(1450, 740))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setColumnCount(22)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setHorizontalHeaderLabels([str(i+1) for i in range(22)])
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.tableWidget.setStyleSheet(""" QTableWidget {
                                                background-color: white;
                                                alternate-background-color: lightgray;
                                                border: 1px solid black;
                                            }
                                            QHeaderView {
                                                background-color: red;
                                                border: 1px solid darkblue;
                                            }
                                            QTableWidget::item:selected  {
                                            background-color: lightgray;
                                            
                                            }


                """)

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
        # self.centralwidget("border")
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
    # ui = Ui_InputMrch()
    ui.show()
    sys.exit(app.exec_())
