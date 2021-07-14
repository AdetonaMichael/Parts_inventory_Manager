# importation of modules and classes to be used in the program 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys
from os import path
from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(path.join(path.dirname('__file__'),"roboto.ui"))
import pymysql 

class Main(QMainWindow, FORM_CLASS):
    
    #creting class constructor
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
    
    # function for managing click events
    def Handel_Buttons(self):
        self.refresh_btn.clicked.connect(self.getData())
        
    # function that pulls data from the database
    def getData(self):
        # establishing connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", dbname="inventory_manager", charset="utf8mb")
    
    # the specific code for the inventory manager project
    
#method main begins execution of python program 
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    
if __name__ =="__main__":
    main() 
    