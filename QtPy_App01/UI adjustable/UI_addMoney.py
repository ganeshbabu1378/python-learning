# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_addMoney.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addMoney(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.wid1_topSection = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wid1_topSection.sizePolicy().hasHeightForWidth())
        self.wid1_topSection.setSizePolicy(sizePolicy)
        self.wid1_topSection.setMinimumSize(QtCore.QSize(0, 300))
        self.wid1_topSection.setMaximumSize(QtCore.QSize(16777215, 300))
        self.wid1_topSection.setAutoFillBackground(False)
        self.wid1_topSection.setObjectName("wid1_topSection")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wid1_topSection)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame1_left = QtWidgets.QFrame(self.wid1_topSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1_left.sizePolicy().hasHeightForWidth())
        self.frame1_left.setSizePolicy(sizePolicy)
        self.frame1_left.setMinimumSize(QtCore.QSize(300, 0))
        self.frame1_left.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame1_left.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame1_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_left.setObjectName("frame1_left")
        self.qf1_ID = QtWidgets.QFrame(self.frame1_left)
        self.qf1_ID.setGeometry(QtCore.QRect(0, 0, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qf1_ID.sizePolicy().hasHeightForWidth())
        self.qf1_ID.setSizePolicy(sizePolicy)
        self.qf1_ID.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf1_ID.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf1_ID.setObjectName("qf1_ID")
        self.label_ID = QtWidgets.QLabel(self.qf1_ID)
        self.label_ID.setGeometry(QtCore.QRect(30, 3, 120, 45))
        self.label_ID.setObjectName("label_ID")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.qf1_ID)
        self.lineEdit_ID.setGeometry(QtCore.QRect(155, 10, 135, 30))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.qf2_Date = QtWidgets.QFrame(self.frame1_left)
        self.qf2_Date.setGeometry(QtCore.QRect(0, 50, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qf2_Date.sizePolicy().hasHeightForWidth())
        self.qf2_Date.setSizePolicy(sizePolicy)
        self.qf2_Date.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf2_Date.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf2_Date.setObjectName("qf2_Date")
        self.label_Date = QtWidgets.QLabel(self.qf2_Date)
        self.label_Date.setGeometry(QtCore.QRect(30, 3, 120, 45))
        self.label_Date.setObjectName("label_Date")
        self.lineEdit_ID_2 = QtWidgets.QLineEdit(self.qf2_Date)
        self.lineEdit_ID_2.setGeometry(QtCore.QRect(155, 10, 135, 30))
        self.lineEdit_ID_2.setObjectName("lineEdit_ID_2")
        self.qf3_Product = QtWidgets.QFrame(self.frame1_left)
        self.qf3_Product.setGeometry(QtCore.QRect(0, 100, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qf3_Product.sizePolicy().hasHeightForWidth())
        self.qf3_Product.setSizePolicy(sizePolicy)
        self.qf3_Product.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf3_Product.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf3_Product.setObjectName("qf3_Product")
        self.label_Product = QtWidgets.QLabel(self.qf3_Product)
        self.label_Product.setGeometry(QtCore.QRect(30, 3, 120, 45))
        self.label_Product.setObjectName("label_Product")
        self.lineEdit_Product = QtWidgets.QLineEdit(self.qf3_Product)
        self.lineEdit_Product.setGeometry(QtCore.QRect(155, 10, 135, 30))
        self.lineEdit_Product.setObjectName("lineEdit_Product")
        self.qf4_EcPrice = QtWidgets.QFrame(self.frame1_left)
        self.qf4_EcPrice.setGeometry(QtCore.QRect(0, 150, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qf4_EcPrice.sizePolicy().hasHeightForWidth())
        self.qf4_EcPrice.setSizePolicy(sizePolicy)
        self.qf4_EcPrice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf4_EcPrice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf4_EcPrice.setObjectName("qf4_EcPrice")
        self.label_EcPrice = QtWidgets.QLabel(self.qf4_EcPrice)
        self.label_EcPrice.setGeometry(QtCore.QRect(30, 3, 120, 45))
        self.label_EcPrice.setObjectName("label_EcPrice")
        self.lineEdit_EcPrice = QtWidgets.QLineEdit(self.qf4_EcPrice)
        self.lineEdit_EcPrice.setGeometry(QtCore.QRect(155, 10, 135, 30))
        self.lineEdit_EcPrice.setObjectName("lineEdit_EcPrice")
        self.qf5_balAdded = QtWidgets.QFrame(self.frame1_left)
        self.qf5_balAdded.setGeometry(QtCore.QRect(0, 200, 300, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qf5_balAdded.sizePolicy().hasHeightForWidth())
        self.qf5_balAdded.setSizePolicy(sizePolicy)
        self.qf5_balAdded.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf5_balAdded.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf5_balAdded.setObjectName("qf5_balAdded")
        self.label_balAdded = QtWidgets.QLabel(self.qf5_balAdded)
        self.label_balAdded.setGeometry(QtCore.QRect(30, 3, 120, 45))
        self.label_balAdded.setObjectName("label_balAdded")
        self.lineEdit_balAdded = QtWidgets.QLineEdit(self.qf5_balAdded)
        self.lineEdit_balAdded.setGeometry(QtCore.QRect(155, 10, 135, 30))
        self.lineEdit_balAdded.setObjectName("lineEdit_balAdded")
        self.horizontalLayout_2.addWidget(self.frame1_left)
        self.frame2_right = QtWidgets.QFrame(self.wid1_topSection)
        self.frame2_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2_right.setObjectName("frame2_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame2_right)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame2_right)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame2_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn1_sav = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1_sav.sizePolicy().hasHeightForWidth())
        self.btn1_sav.setSizePolicy(sizePolicy)
        self.btn1_sav.setMinimumSize(QtCore.QSize(150, 0))
        self.btn1_sav.setObjectName("btn1_sav")
        self.horizontalLayout_4.addWidget(self.btn1_sav)
        self.btn2_fetch = QtWidgets.QPushButton(self.frame_2)
        self.btn2_fetch.setMinimumSize(QtCore.QSize(150, 0))
        self.btn2_fetch.setObjectName("btn2_fetch")
        self.horizontalLayout_4.addWidget(self.btn2_fetch)
        self.btn3_delete = QtWidgets.QPushButton(self.frame_2)
        self.btn3_delete.setMinimumSize(QtCore.QSize(150, 0))
        self.btn3_delete.setObjectName("btn3_delete")
        self.horizontalLayout_4.addWidget(self.btn3_delete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.frame2_right)
        self.verticalLayout.addWidget(self.wid1_topSection)
        self.wid2_bottomSection = QtWidgets.QWidget(self.centralwidget)
        self.wid2_bottomSection.setObjectName("wid2_bottomSection")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wid2_bottomSection)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.wid2_bottomSection)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(self.wid2_bottomSection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.wid2_bottomSection)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.tool_addMoney = QtWidgets.QAction(MainWindow)
        self.tool_addMoney.setCheckable(True)
        self.tool_addMoney.setChecked(True)
        self.tool_addMoney.setObjectName("tool_addMoney")
        self.tool_payment = QtWidgets.QAction(MainWindow)
        self.tool_payment.setCheckable(True)
        self.tool_payment.setObjectName("tool_payment")
        self.tool_updateBalance = QtWidgets.QAction(MainWindow)
        self.tool_updateBalance.setCheckable(True)
        self.tool_updateBalance.setObjectName("tool_updateBalance")
        self.tool_rebalanceInvestment = QtWidgets.QAction(MainWindow)
        self.tool_rebalanceInvestment.setCheckable(True)
        self.tool_rebalanceInvestment.setObjectName("tool_rebalanceInvestment")
        self.tool_summary = QtWidgets.QAction(MainWindow)
        self.tool_summary.setCheckable(True)
        self.tool_summary.setChecked(False)
        self.tool_summary.setObjectName("tool_summary")
        self.toolBar.addAction(self.tool_summary)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.tool_addMoney)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.tool_payment)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.tool_updateBalance)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.tool_rebalanceInvestment)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mobile Recharge Tracker"))
        self.label_ID.setText(_translate("MainWindow", "ID"))
        self.label_Date.setText(_translate("MainWindow", "Date"))
        self.label_Product.setText(_translate("MainWindow", "Product"))
        self.label_EcPrice.setText(_translate("MainWindow", "Ec Price"))
        self.label_balAdded.setText(_translate("MainWindow", "Bal. Added"))
        self.label.setText(_translate("MainWindow", "Comments"))
        self.btn1_sav.setText(_translate("MainWindow", "Save / Update"))
        self.btn2_fetch.setText(_translate("MainWindow", "Fetch"))
        self.btn3_delete.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "Recent Transactions"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.tool_addMoney.setText(_translate("MainWindow", "Add Money"))
        self.tool_payment.setText(_translate("MainWindow", "Payment"))
        self.tool_updateBalance.setText(_translate("MainWindow", "Update Balance"))
        self.tool_rebalanceInvestment.setText(_translate("MainWindow", "Rebalance Investment"))
        self.tool_summary.setText(_translate("MainWindow", "Summary"))