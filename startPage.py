from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputMrch(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_InputMrch, self).__init__(parent)
        self.setObjectName("InputMrchWindow")
        # self.resize(800, 600)
        # self.setGeometry(0, 0, 1500, 900)
        self.setGeometry(0, 0, 100, 100)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1150, 640))
        self.frame.setObjectName("frame")

        self.frameLeft = QtWidgets.QFrame(self.frame)
        self.frameLeft.setGeometry(QtCore.QRect(0, 0, 750, 640))
        self.frameLeft.setObjectName("frameLeft")

        self.frameRight = QtWidgets.QFrame(self.frame)
        self.frameRight.setGeometry(QtCore.QRect(750, 0, 400, 640))
        self.frameRight.setObjectName("frameRight")

        self.tableWidget = QtWidgets.QTableWidget(self.frameLeft)
        self.tableWidget.setGeometry(QtCore.QRect(100, 30, 580, 580))
        # self.tableWidget.setGeometry(QtCore.QRect(10, 10, 690, 800))

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

        self.addRow = QtWidgets.QPushButton(self.frameRight)
        self.addRow.setGeometry(QtCore.QRect(20, 20, 160, 45))
        self.addRow.setObjectName("addRow")

        self.removeRow = QtWidgets.QPushButton(self.frameRight)
        self.removeRow.setGeometry(QtCore.QRect(20, 85, 160, 45))
        self.removeRow.setObjectName("removeRow")

        self.viewDetails = QtWidgets.QPushButton(self.frameRight)
        self.viewDetails.setGeometry(QtCore.QRect(20, 145, 160, 45))
        self.viewDetails.setObjectName("viewDetails")

        # self.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)

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

    def onAddRowButtonClick(self):
        # print("Test")
        current_row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(current_row_count)

    def onRemoveButtonClick(self):
        if self.tableWidget.rowCount() > 1:
            selected_row = self.tableWidget.currentRow()
            if selected_row >= 0:
                self.tableWidget.removeRow(selected_row)
            else:
                self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)

    def onViewDetailsButtonClick(self):
        ipMrch = []
        ipCmt = []
        for row in range(self.tableWidget.rowCount()):
            item1 = self.tableWidget.item(row, 0)
            item2 = self.tableWidget.item(row, 1)
            if item1 is not None and item1.text() is not '':
                ipMrch.append(str(item1.text()))
            else:
                ipMrch.append('NULL')

            if item2 is not None and item1 is not '':
                ipCmt.append(str(item2.text()))
            else:
                ipCmt.append('NULL')

        print(ipMrch, ipCmt)
        if 'NULL' in ipMrch:
            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle("Warning")
            messageBox.setText("Please Enter All Details (Mrch)")
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
            x = messageBox.exec_()

        elif 'NULL' in ipCmt:
            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle("Warning")
            messageBox.setText("Please Enter All Details (Comment)")
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
            x = messageBox.exec_()

        else:
            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle("Success")
            messageBox.setText("Pulling Data")
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
            x = messageBox.exec_()

    def setStyleInputMrch(self):
        # self.setStyleSheet("background-color: #d8f6ff;")
        self.frameLeft.setStyleSheet("""QFrame#frameLeft
                                    {   
                                        background-color: #1f2437;

                                    }""")

        self.frameRight.setStyleSheet("border: 1px solid white;")

        self.addRow.setStyleSheet("background-color: #3d8cff;\n"
                                  "font-family: Arial;\n"
                                  "font-size: 16px;\n"
                                  "font-weight: bold;\n"
                                  "color: white;\n"
                                  "border-radius: 5px"
                                  "}")

        self.removeRow.setStyleSheet("background-color: #3d8cff;\n"
                                     "font-family: Arial;\n"
                                     "font-size: 16px;\n"
                                     "font-weight: bold;\n"
                                     "color: white;\n"
                                     "border-radius: 5px"
                                     "}")

        self.viewDetails.setStyleSheet("background-color: #3d8cff;\n"
                                       "font-family: Arial;\n"
                                       "font-size: 16px;\n"
                                       "font-weight: bold;\n"
                                       "color: white;\n"
                                       "border-radius: 5px"
                                       "}")

        # self.frame.setStyleSheet("""QFrame#frame{
        #                             background-color: red;
        #                             }
        #
        # """)

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
                                       "background-color: ;\n"
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


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        # self.resize(710, 233)
        self.setGeometry(250, 60, 1550, 940)
        # self.centralwidget = QtWidgets.QWidget(self)
        # self.centralwidget.setObjectName("centralwidget")

        self.leftFrame = QtWidgets.QFrame(self)
        self.leftFrame.setGeometry(0, 0, 300, 960)
        self.leftFrame.setObjectName("leftFrame")

        self.rightFrame = QtWidgets.QFrame(self)
        self.rightFrame.setGeometry(300, 0, 1350, 960)
        self.rightFrame.setObjectName("rightFrame")

        self.centralFrame = QtWidgets.QFrame(self)
        self.centralFrame.setGeometry(100, 150, 1350, 640)
        # self.opacity = QtWidgets.QGraphicsOpacityEffect()
        # self.opacity.setOpacity(0.2)
        # self.centralFrame.setGraphicsEffect(self.opacity)
        self.centralFrame.setObjectName('centralFrame')

        self.centralLeftFrame = QtWidgets.QFrame(self.centralFrame)
        self.centralLeftFrame.setGeometry(0, 0, 200, 640)
        self.centralLeftFrame.setObjectName('centralLeftFrame')

        self.homeBtn = QtWidgets.QPushButton('Home', self.centralLeftFrame)
        self.homeBtn.setGeometry(QtCore.QRect(0, 100, 200, 45))
        self.homeBtn.setObjectName("homeBtn")

        self.addBtn = QtWidgets.QPushButton('Add', self.centralLeftFrame)
        self.addBtn.setGeometry(QtCore.QRect(0, 170, 200, 45))
        self.addBtn.setObjectName("addBtn")

        self.viewBtn = QtWidgets.QPushButton('View', self.centralLeftFrame)
        self.viewBtn.setGeometry(QtCore.QRect(0, 240, 200, 45))
        self.viewBtn.setObjectName("viewBtn")

        self.removeBtn = QtWidgets.QPushButton('Remove', self.centralLeftFrame)
        self.removeBtn.setGeometry(QtCore.QRect(0, 310, 200, 45))
        self.removeBtn.setObjectName("removeBtn")

        self.centralRightFrame = QtWidgets.QFrame(self.centralFrame)
        self.centralRightFrame.setGeometry(200, 0, 1150, 640)
        self.centralRightFrame.setObjectName('centralRightFrame')
        # self.bottomFrame.setStyleSheet("border: 1px solid black;")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralRightFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(0, 0, 1150, 640)

        self.homeWidget = QtWidgets.QWidget()
        self.homeWidget.setObjectName("homeWidget")

        self.tableWidget = QtWidgets.QTableWidget(self.homeWidget)
        self.tableWidget.setGeometry(QtCore.QRect(15, 25, 1100, 580))  # 1150 640

        # self.tableWidget.setMaximumSize(QtCore.QSize(1450, 740))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setHorizontalHeaderLabels([str(i + 1) for i in range(8)])
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)

        self.emptyWidget = QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.emptyWidget)  # 0
        self.stackedWidget.addWidget(self.homeWidget)   # 1
        self.stackedWidget.addWidget(Ui_InputMrch())    # 2

        self.retranslateUi()
        self.mainWindowSetStyle()
        self.onHomeButtonClick()

        self.homeBtn.clicked.connect(self.onHomeButtonClick)
        self.addBtn.clicked.connect(self.onAddButtonClick)
        self.viewBtn.clicked.connect(self.onViewButtonClick)
        self.removeBtn.clicked.connect(self.onRemoveButtonClick)
        QtCore.QMetaObject.connectSlotsByName(self)

    def pulldata(self):
        pass

    def test(self):
        self.onHomeButtonClick()

    def onHomeButtonClick(self):
        self.homeBtn.setEnabled(False)
        self.addBtn.setEnabled(True)
        self.removeBtn.setEnabled(True)
        self.viewBtn.setEnabled(True)

        print("Home Clicked")
        self.stackedWidget.setCurrentIndex(1)

    def onAddButtonClick(self):

        self.homeBtn.setEnabled(True)
        self.addBtn.setEnabled(False)
        self.removeBtn.setEnabled(True)
        self.viewBtn.setEnabled(True)

        # print("Add Clicked")
        # self.hide()
        # self.window_InputMrch = QtWidgets.QMainWindow()
        # self.window_InputMrch = Ui_InputMrch()
        # self.window_InputMrch.show()
        self.stackedWidget.setCurrentIndex(2)

    def onViewButtonClick(self):
        self.homeBtn.setEnabled(True)
        self.addBtn.setEnabled(True)
        self.removeBtn.setEnabled(True)
        self.viewBtn.setEnabled(False)

        print("View Clicked")

    def onRemoveButtonClick(self):
        self.homeBtn.setEnabled(True)
        self.addBtn.setEnabled(True)
        self.removeBtn.setEnabled(False)
        self.viewBtn.setEnabled(True)
        print("Remove Clicked")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Select Option"))
        self.addBtn.setText(_translate("MainWindow", "Add Merchants"))
        self.viewBtn.setText(_translate("MainWindow", "View Merchants"))
        self.removeBtn.setText(_translate("MainWindow", "Remove Merchants"))

    def mainWindowSetStyle(self):
        # self.setStyleSheet("background-color: red;") 1f2437

        # self.centralFrame.setStyleSheet(""" QFrame#centralFrame{
        #                                         border-radius: 20px;
        #                                     }
        #                                 """)

        self.leftFrame.setStyleSheet("""background-color: #c4cee5;
                                    """)

        self.rightFrame.setStyleSheet("""background-color: #dbe2f4;
                                            """)

        self.centralLeftFrame.setStyleSheet("""QFrame#centralLeftFrame{
                                                background-color: #272d45;
                                                border-top-left-radius: 20px;
                                                border-bottom-left-radius: 20px;
                                            }""")  # border: 2px solid white;

        self.centralRightFrame.setStyleSheet("""QFrame#centralRightFrame{
                                                background-color: #1f2437;
                                                border-top-right-radius: 20px;
                                                border-bottom-right-radius: 20px;
                                            }""")

        self.homeBtn.setStyleSheet("QPushButton{\n"
                                   "background-color: #272d45;\n"
                                   "font-family: Arial;\n"
                                   "font-size: 18px;\n"
                                   "font-weight: bold;\n"
                                   "color: #a5a7af;\n"
                                   "border-radius: 15px;\n"
                                   "text-align: right;\n"
                                   "padding-right: 10px;"
                                   "}\n"
                                   "\n"

                                   "QPushButton:hover {\n"
                                   "background-color: #2a324f;\n"
                                   "color: white;\n"
                                   "}\n"
                                   "\n"
                                   )

        self.addBtn.setStyleSheet("QPushButton{\n"
                                  "background-color: #272d45;\n"
                                  "font-family: Arial;\n"
                                  "font-size: 18px;\n"
                                  "font-weight: bold;\n"
                                  "color: #a5a7af;\n"
                                  "border-radius: 5px;\n"
                                  "text-align: right;\n"
                                  "padding-right: 10px;"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "background-color: #2a324f;\n"
                                  "color: white"
                                  "}")

        self.viewBtn.setStyleSheet("QPushButton{\n"
                                   "background-color: #272d45;\n"
                                   "font-family: Arial;\n"
                                   "font-size: 18px;\n"
                                   "font-weight: bold;\n"
                                   "color: #a5a7af;\n"
                                   "border-radius: 5px;\n"
                                   "text-align: right;\n"
                                   "padding-right: 10px;\n"
                                   "}\n"

                                   "QPushButton:hover {\n"
                                   "background-color: #2a324f;\n"
                                   "color: white"
                                   "}"
                                   )

        self.removeBtn.setStyleSheet("background-color: #272d45;\n"
                                     "font-family: Arial;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;\n"
                                     "color: #a5a7af;\n"
                                     "border-radius: 5px;\n"
                                     "text-align: right;\n"
                                     "padding-right: 10px;"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background-color: #2a324f;\n"
                                     "color: white"
                                     "}")

        self.tableWidget.setStyleSheet(""" QTableWidget {
                                                    background-color: #2a324f;
                                                    border-radius: 5px;
                                                    border: 1px solid white;
                                                    gridline-color: #fffff8;
                                            }

                                            QTableWidget::item:selected  {
                                                    background-color: #fefefe;
                                            }

                                            QTableWidget::item{
                                                   font-family: Arial;
                                                   font-size: 1px;

                                                   padding: 0px;
                                                   color:black;                       
                                            }

                        """)
        # ededed headers # background-color: red; border: 1.5px solid #757a8d;

        # self.tableWidget.horizontalHeader().setStyleSheet("""   QHeaderView::section {
        #                                                         background-color: #ececec;
        #                                                         border: 1px solid black;
        #                                                 }
        # """)

        self.tableWidget.horizontalHeader().setStyleSheet("""
                                                QHeaderView::section {
                                                background-color: #40a3f3; 
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

        self.tableWidget.verticalScrollBar().setStyleSheet("background-color: #23283a;")
        self.tableWidget.horizontalScrollBar().setStyleSheet("background-color: #23283a;")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    # ui = Ui_InputMrch()
    ui.show()
    sys.exit(app.exec_())
