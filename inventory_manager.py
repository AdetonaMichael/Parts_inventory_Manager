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
from PyQt5.sip import dump
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
        self.refresh_btn.clicked.connect(self.getData)
        
    # function that pulls data from the database
    def getData(self):
        # establishing connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="inventory_manager", charset="utf8mb4")
        
        #creating a controller object for managing database query
        controller = connection.cursor()
        sql = '''SELECT * FROM data'''
        result = controller.execute(sql)
        
        #initialization of the number of rows in the table
        self.inventory_table.setRowCount(0)
        
        #looping through the returned dat
        for row_count, row_data in enumerate(result):
            self.inventory_table.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.inventory_table.setItem(row_count, column_count, QTableWidgetItem(str(data)))
    
# the specific code for the inventory manager project
    
#method main begins execution of python program 
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    
if __name__ =="__main__":
    main() 
    