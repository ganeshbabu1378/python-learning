# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dataEntry.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class ui_rechargePage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 1050)
        MainWindow.setMinimumSize(QtCore.QSize(1450, 1050))
        MainWindow.setMaximumSize(QtCore.QSize(2048, 1280))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(350, 0))
        self.frame.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.qf_ID = QtWidgets.QFrame(self.frame)
        self.qf_ID.setGeometry(QtCore.QRect(0, 0, 350, 50))
        self.qf_ID.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf_ID.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf_ID.setObjectName("qf_ID")
        self.label = QtWidgets.QLabel(self.qf_ID)
        self.label.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.qf_ID)
        self.lineEdit.setGeometry(QtCore.QRect(132, 10, 200, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.qf_Added_Money = QtWidgets.QFrame(self.frame)
        self.qf_Added_Money.setGeometry(QtCore.QRect(0, 200, 350, 50))
        self.qf_Added_Money.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf_Added_Money.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf_Added_Money.setObjectName("qf_Added_Money")
        self.label_5 = QtWidgets.QLabel(self.qf_Added_Money)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.qf_Added_Money)
        self.lineEdit_3.setGeometry(QtCore.QRect(132, 10, 200, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.qf_Date = QtWidgets.QFrame(self.frame)
        self.qf_Date.setGeometry(QtCore.QRect(0, 50, 350, 50))
        self.qf_Date.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf_Date.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf_Date.setObjectName("qf_Date")
        self.label_2 = QtWidgets.QLabel(self.qf_Date)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.qf_Date)
        self.dateEdit.setGeometry(QtCore.QRect(132, 10, 200, 30))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 3, 12), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.qf_Product = QtWidgets.QFrame(self.frame)
        self.qf_Product.setGeometry(QtCore.QRect(0, 100, 350, 50))
        self.qf_Product.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf_Product.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf_Product.setObjectName("qf_Product")
        self.label_3 = QtWidgets.QLabel(self.qf_Product)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.qf_Product)
        self.comboBox.setGeometry(QtCore.QRect(132, 10, 200, 30))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.qf_EcPrice = QtWidgets.QFrame(self.frame)
        self.qf_EcPrice.setGeometry(QtCore.QRect(0, 150, 350, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qf_EcPrice.sizePolicy().hasHeightForWidth())
        self.qf_EcPrice.setSizePolicy(sizePolicy)
        self.qf_EcPrice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qf_EcPrice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qf_EcPrice.setObjectName("qf_EcPrice")
        self.label_4 = QtWidgets.QLabel(self.qf_EcPrice)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 100, 30))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.qf_EcPrice)
        self.lineEdit_2.setGeometry(QtCore.QRect(132, 10, 200, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_2)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd_Money = QtWidgets.QAction(MainWindow)
        self.actionAdd_Money.setCheckable(True)
        self.actionAdd_Money.setChecked(True)
        self.actionAdd_Money.setObjectName("actionAdd_Money")
        self.actionPayment = QtWidgets.QAction(MainWindow)
        self.actionPayment.setCheckable(True)
        self.actionPayment.setObjectName("actionPayment")
        self.actionUpdate_Balance = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Balance.setCheckable(True)
        self.actionUpdate_Balance.setChecked(False)
        self.actionUpdate_Balance.setObjectName("actionUpdate_Balance")
        self.toolBar.addAction(self.actionAdd_Money)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPayment)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUpdate_Balance)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tracking"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_5.setText(_translate("MainWindow", "Bal. Added"))
        self.label_2.setText(_translate("MainWindow", "Date"))
        self.label_3.setText(_translate("MainWindow", "Product"))
        self.label_4.setText(_translate("MainWindow", "EC Price"))
        self.label_6.setText(_translate("MainWindow", "Comments"))
        self.label_7.setText(_translate("MainWindow", "Last 45 Transactions"))
        self.tableWidget.setSortingEnabled(True)
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAdd_Money.setText(_translate("MainWindow", "Add Money"))
        self.actionPayment.setText(_translate("MainWindow", "Payment"))
        self.actionUpdate_Balance.setText(_translate("MainWindow", "Update Balance"))
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        #Combobox-additems
        list_products= ['','Vodafone','Airtel']
        self.comboBox.clear()
        self.comboBox.addItems(list_products)

        #Update Button text
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setText("Save")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Abort).setText("Fetch")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).setText("Update")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Help).setText("Delete")

        #Update date to today's date
        l_txn_date = datetime.date.today()
        self.dateEdit.setDate( QtCore.QDate(l_txn_date.year, l_txn_date.month, l_txn_date.day)  ) 