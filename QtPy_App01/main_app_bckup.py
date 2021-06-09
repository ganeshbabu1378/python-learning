#Library(s) needed
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import datetime

#UI Imports
from ui_loginPage import ui_loginPage
from ui_rechargePage import ui_rechargePage
from ui_paymentPage import ui_paymentPage

#Script Imports
from script_security import *
from script_SQL import *
from scripts_QTable import *

class login_page(QtWidgets.QMainWindow, ui_loginPage):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, obj=None, **kwargs):
        super(login_page, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.validate_login)

    def validate_login(self):
        l_user_id = self.lineEdit.text() 
        l_user_cred = self.lineEdit_2.text()
        if  check_encrypted_password( l_user_cred , read_credentials(l_user_id) ) :
            self.switch_window.emit()

class recharge_page(QtWidgets.QMainWindow, ui_rechargePage):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, obj=None, **kwargs):
        super(recharge_page, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionPayment.triggered.connect(lambda checked: self.toggle_pages('payment') )
        self.actionUpdate_Balance.triggered.connect(lambda checked: self.toggle_pages('update balance') )
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.insert_data_in_recharge_table)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Abort).clicked.connect(self.fetch_data_from_recharge_table)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.insert_data_in_recharge_table)
        upsertTableContents(self.tableWidget , read_recharge_table())
    
    def insert_data_in_recharge_table(self):
        l_id = self.lineEdit.text()
        l_txn_date = self.dateEdit.date().toPyDate()
        l_product = self.comboBox.currentText()
        l_ec_amt = self.lineEdit_2.text()
        l_added_amt =  self.lineEdit_3.text()
        l_comment =  self.textEdit.toPlainText()
        
        upsert_recharge_table( l_id , l_txn_date , l_product , l_ec_amt , l_added_amt  , l_comment )
        upsertTableContents(self.tableWidget , read_recharge_table())

    def fetch_data_from_recharge_table(self):
        l_id = self.lineEdit.text()
        result = read_recharge_table_by_ID( l_id )
        if ( len(result) > 0 ) :
            ( l_id , l_txn_date , l_product , l_ec_amt , l_added_amt  , l_comment ) = result
        else :  
            ( l_id , l_txn_date , l_product , l_ec_amt , l_added_amt  , l_comment ) = ( l_id , '', '',0 , 0 ,'')
        
        self.lineEdit.setText(str(l_id) )
        l_txn_date = datetime.datetime.strptime( l_txn_date, "%Y-%m-%d")
        self.dateEdit.setDate( QtCore.QDate(l_txn_date.year, l_txn_date.month, l_txn_date.day)  ) 
        self.comboBox.setCurrentText(l_product)
        self.lineEdit_2.setText(str(l_ec_amt) )
        self.lineEdit_3.setText(str(l_added_amt) )
        self.textEdit.setText(l_comment)
        
    def toggle_pages(self , controlText ):
        if controlText == 'payment':
            self.switch_window.emit()
        elif controlText == 'update balance':
            pass


class payment_page(QtWidgets.QMainWindow, ui_paymentPage):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, obj=None, **kwargs):
        super(login_page, self).__init__(*args, **kwargs)
        self.setupUi(self)

class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = login_page()
        self.login.switch_window.connect(self.show_recharge_page)
        self.login.show()
    
    def show_recharge_page(self):
        self.recharge_page = recharge_page()
        self.login.close()
        self.recharge_page.show()
    
    def show_payment_page(self):
        self.payment_page = payment_page()
        self.recharge_page.close()
        self.payment_page.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    sql_initialize()
    lControl = Controller()
    lControl.show_login()
    # lControl.recharge_page()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()