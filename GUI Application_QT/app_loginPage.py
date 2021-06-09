import sys
from PyQt5 import QtWidgets, QtCore, uic 

from ui_files.ui_loginPage import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.say_hello)

    def say_hello(self): 
        pass


class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = MainWindow()
        #self.login.switch_window.connect(self.show_main)
        self.login.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    lControl = Controller()
    lControl.show_login()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()