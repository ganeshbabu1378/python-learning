#Library(s) needed
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import datetime

#UI Imports
from UI_addMoney import Ui_addMoney


class recharge_page(QtWidgets.QMainWindow, Ui_addMoney):

    switch_window = QtCore.pyqtSignal( str, name='page_to_load')

    def __init__(self, *args, obj=None, **kwargs):
        super(recharge_page, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.header_names = ["ID", "Date", "Product","EC Price","Added Money","Comment"]
        
    def toggle_pages(self , controlText ):
            self.switch_window.emit( controlText )



class Controller:
    def __init__(self):
        self.recharge_page = recharge_page()
        self.current_page = ''
        self.current_geometry = QtCore.QRect(50, 50, 800, 800)
        
        self.toggle_pages ( 'recharge page')
        
    
    def get_geometry ( self ):
        if self.current_page == 'recharge page':
            self.current_geometry = self.recharge_page.geometry()
        


    def toggle_pages (self , controlText ):
        self.get_geometry()
        self.recharge_page.close()

        if controlText == 'recharge page':
            self.recharge_page = recharge_page()
            self.recharge_page.switch_window.connect( self.toggle_pages )
            if self.current_page != '' or self.current_page != 'login page' :
                self.recharge_page.setGeometry(self.current_geometry)
            self.recharge_page.show()

        self.current_page = controlText


def main():
    app = QtWidgets.QApplication(sys.argv)
    lControl = Controller()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()