#Library(s) needed
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import datetime


#UI Imports
from MIMEs.UI.ui_loginPage import ui_loginPage
from MIMEs.UI.ui_rechargePage import ui_rechargePage
from MIMEs.UI.ui_paymentPage import ui_paymentPage
from MIMEs.UI.ui_balancePage import ui_balancePage

#Script Imports
from MIMEs.Control.script_security import *
from MIMEs.Control.script_SQL import *
from MIMEs.Control.scripts_QTable import *

class login_page(QtWidgets.QMainWindow, ui_loginPage):

    switch_window = QtCore.pyqtSignal( str, name='page_to_load' )

    def __init__(self, *args, obj=None, **kwargs):
        super(login_page, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.validate_login)

    def validate_login(self):
        l_user_id = self.lineEdit.text() 
        l_user_cred = self.lineEdit_2.text()
        if  check_encrypted_password( l_user_cred , read_credentials(l_user_id) ) :
            self.switch_window.emit('recharge page')

class recharge_page(QtWidgets.QMainWindow, ui_rechargePage):

    switch_window = QtCore.pyqtSignal( str, name='page_to_load')

    def __init__(self, *args, obj=None, **kwargs):
        super(recharge_page, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.header_names = ["ID", "Date", "Product","EC Price","Added Money","Comment"]
        self.actionPayment.triggered.connect(lambda checked: self.toggle_pages('payment page') )
        self.actionUpdate_Balance.triggered.connect(lambda checked: self.toggle_pages('balance page') )
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.insert_data_in_recharge_table)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Abort).clicked.connect(self.fetch_data_from_recharge_table)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.insert_data_in_recharge_table)
        upsertTableContents(self.tableWidget , read_recharge_table() , self.header_names)
    
    def insert_data_in_recharge_table(self):
        l_id = self.lineEdit.text()
        l_txn_date = self.dateEdit.date().toPyDate()
        l_product = self.comboBox.currentText()
        l_ec_amt = self.lineEdit_2.text()
        l_added_amt =  self.lineEdit_3.text()
        l_comment =  self.textEdit.toPlainText()
        
        upsert_recharge_table( l_id , l_txn_date , l_product , l_ec_amt , l_added_amt  , l_comment )
        upsertTableContents(self.tableWidget , read_recharge_table() , self.header_names)

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
            self.switch_window.emit( controlText )


class payment_page(QtWidgets.QMainWindow, ui_paymentPage):

    switch_window = QtCore.pyqtSignal( str, name='page_to_load')

    def __init__(self, *args, obj=None, **kwargs):
        super(payment_page, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.header_names = ["ID", "Date", "Product","Pay Amount","Comment"]
        self.actionAdd_Money.triggered.connect(lambda checked: self.toggle_pages('recharge page') )
        self.actionUpdate_Balance.triggered.connect(lambda checked: self.toggle_pages('balance page') )
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.insert_data_in_payment_table)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Abort).clicked.connect(self.fetch_data_from_payment_table)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.insert_data_in_payment_table)
        upsertTableContents(self.tableWidget , read_payment_table() , self.header_names)
    
    def insert_data_in_payment_table(self):
        l_id = self.lineEdit.text()
        l_txn_date = self.dateEdit.date().toPyDate()
        l_product = self.comboBox.currentText()
        l_pay_amt = self.lineEdit_2.text()
        l_comment =  self.textEdit.toPlainText()
        
        upsert_payment_table( l_id , l_txn_date , l_product , l_pay_amt  , l_comment )
        upsertTableContents(self.tableWidget , read_payment_table() , self.header_names )

    def fetch_data_from_payment_table(self):
        l_id = self.lineEdit.text()
        result = read_payment_table_by_ID( l_id )
        if ( len(result) > 0 ) :
            ( l_id , l_txn_date , l_product , l_pay_amt  , l_comment ) = result
        else :  
            ( l_id , l_txn_date , l_product , l_pay_amt  , l_comment ) = ( l_id , '', '',0 , 0 ,'')
        
        self.lineEdit.setText(str(l_id) )
        l_txn_date = datetime.datetime.strptime( l_txn_date, "%Y-%m-%d")
        self.dateEdit.setDate( QtCore.QDate(l_txn_date.year, l_txn_date.month, l_txn_date.day)  ) 
        self.comboBox.setCurrentText(l_product)
        self.lineEdit_2.setText(str(l_pay_amt) )
        self.textEdit.setText(l_comment)

    def toggle_pages(self , controlText ):
            self.switch_window.emit( controlText )


class balance_page(QtWidgets.QMainWindow, ui_balancePage):

    switch_window = QtCore.pyqtSignal( str, name='page_to_load')

    def __init__(self, *args, obj=None, **kwargs):
        super(balance_page, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.header_names = ["ID", "Date", "Jio","Airtel","Vodafone","Multi","Sun-direct","Comment"]
        self.actionAdd_Money.triggered.connect(lambda checked: self.toggle_pages('recharge page') )
        self.actionPayment.triggered.connect(lambda checked: self.toggle_pages('payment page') )
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.insert_data_in_dailybalance_table)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.fetch_data_from_dailybalance_table)
        self.buttonBox_2.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.insert_data_in_dailybalance_table)
        upsertTableContents(self.tableWidget , read_dailybalance_table() , self.header_names)
    

    def insert_data_in_dailybalance_table(self):
        l_id = self.lineEdit_5.text()
        l_txn_date = self.dateEdit_2.date().toPyDate()
        l_p_jio = self.lineEdit_8.text()
        l_p_airtel = self.lineEdit_9.text()
        l_p_vodafone = self.lineEdit_7.text()
        l_p_multi = self.lineEdit_6.text()
        l_p_sundirect = self.lineEdit_10.text()
        l_comment =  self.textEdit_2.toPlainText()
        
        upsert_dailybalance_table( l_id , l_txn_date , l_p_jio , l_p_airtel , l_p_vodafone , l_p_multi , l_p_sundirect , l_comment )
        upsertTableContents(self.tableWidget , read_dailybalance_table() , self.header_names)

    def fetch_data_from_dailybalance_table(self):
        l_id = self.lineEdit_5.text()
        result = read_dailybalance_table_by_ID( l_id )
        if ( len(result) > 0 ) :
            ( l_id , l_txn_date , l_p_jio , l_p_airtel , l_p_vodafone , l_p_multi , l_p_sundirect , l_comment ) = result
        else :  
            ( l_id , l_txn_date , l_p_jio , l_p_airtel , l_p_vodafone , l_p_multi , l_p_sundirect , l_comment ) = ( l_id , "" , 0 , 0 , 0 , 0 , 0 , '' )
        
        self.lineEdit_5.setText(str(l_id) )
        l_txn_date = datetime.datetime.strptime( l_txn_date, "%Y-%m-%d")
        self.dateEdit_2.setDate( QtCore.QDate(l_txn_date.year, l_txn_date.month, l_txn_date.day)  )
        self.lineEdit_8.setText(str(l_p_jio) )
        self.lineEdit_9.setText(str(l_p_airtel) )
        self.lineEdit_7.setText(str(l_p_vodafone) )
        self.lineEdit_6.setText(str(l_p_multi) )
        self.lineEdit_10.setText(str(l_p_sundirect) )
        self.textEdit_2.setText(l_comment)


    def toggle_pages(self , controlText ):
            self.switch_window.emit( controlText )



class Controller:
    def __init__(self):
        self.login = login_page()
        self.recharge_page = recharge_page()
        self.payment_page = payment_page()
        self.balance_page = balance_page()
        self.current_page = ''
        self.current_geometry = QtCore.QRect(50, 50, 800, 400)
        self.toggle_pages ( 'login page')
    
    def get_geometry ( self ):
        if self.current_page == 'login page':
            self.current_geometry = self.login.geometry()
        elif self.current_page == 'recharge page':
            self.current_geometry = self.recharge_page.geometry()
        elif self.current_page == 'payment page':
            self.current_geometry = self.payment_page.geometry()
        elif self.current_page == 'balance page':
            self.current_geometry = self.balance_page.geometry()
        


    def toggle_pages (self , controlText ):
        self.get_geometry()
        self.login.close()
        self.recharge_page.close()
        self.payment_page.close()
        self.balance_page.close()

        if controlText =='login page':
            self.login = login_page()
            self.login.switch_window.connect( self.toggle_pages )
            if self.current_page != '' or self.current_page != 'login page' :
                self.login.setGeometry(self.current_geometry)
            self.login.show()

        elif controlText == 'recharge page':
            self.recharge_page = recharge_page()
            self.recharge_page.switch_window.connect( self.toggle_pages )
            if self.current_page != '' or self.current_page != 'login page' :
                self.recharge_page.setGeometry(self.current_geometry)
            self.recharge_page.show()

        elif controlText == 'payment page':
            self.payment_page = payment_page()
            self.payment_page.switch_window.connect( self.toggle_pages )
            if self.current_page != '' or self.current_page != 'login page' :
                self.payment_page.setGeometry(self.current_geometry)
            self.payment_page.show()
        
        elif controlText == 'balance page':
            self.balance_page = balance_page()
            self.balance_page.switch_window.connect( self.toggle_pages )
            if self.current_page != '' or self.current_page != 'login page' :
                self.balance_page.setGeometry(self.current_geometry)
            self.balance_page.show()

        self.current_page = controlText


def main():
    app = QtWidgets.QApplication(sys.argv)
    sql_initialize()
    lControl = Controller()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()