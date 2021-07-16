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
        self.navigate()
    
    
    # function for managing click events
    def Handel_Buttons(self):
        self.refresh_btn.clicked.connect(self.getData)
        self.search_push_button.clicked.connect(self.search)
        self.check_btn.clicked.connect(self.level)
        self.add_btn.clicked.connect(self.add)
    
    
    # function to search for item in the inventory
    def search(self, id):
         # establishing connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="inventory_manager", charset="utf8mb4")
        nbr = int(self.count_level_filter.text())
        #creating a controller object for managing database query
        controller = connection.cursor()
        sql = 'SELECT * FROM data WHERE count < %d'%(nbr)
        controller.execute(sql)
        result = controller.fetchall()
        
        #initialization of the number of rows in the table
        self.inventory_table.setRowCount(0)
        
        #looping through the returned data
        for row_count, row_data in enumerate(result):
            self.inventory_table.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.inventory_table.setItem(row_count, column_count, QTableWidgetItem(str(data)))
    def level(self):
         # establishing connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="inventory_manager", charset="utf8mb4")
        
        #creating a controller object for managing database query
        controller = connection.cursor()
        sql = 'SELECT reference, partname, count FROM data order by count asc limit 3'
        controller.execute(sql)
        result = controller.fetchall()
        
        #initialization of the number of rows in the table
        self.inventory_stat_table.setRowCount(0)
        
        #looping through the returned dat
        for row_count, row_data in enumerate(result):
            self.inventory_stat_table.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.inventory_stat_table.setItem(row_count, column_count, QTableWidgetItem(str(data)))
        
    # function that pulls data from the database
    def getData(self):
        # establishing connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="inventory_manager", charset="utf8mb4")
        
        #creating a controller object for managing database query
        controller = connection.cursor()
        sql = '''SELECT * FROM data'''
        controller.execute(sql)
        result = controller.fetchall()
        
        #initialization of the number of rows in the table
        self.inventory_table.setRowCount(0)
        
        #looping through the returned dat
        for row_count, row_data in enumerate(result):
            self.inventory_table.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.inventory_table.setItem(row_count, column_count, QTableWidgetItem(str(data)))
        #simple code to display reference number and parts nubmer
        controller2 = connection.cursor()
        controller3 = connection.cursor()
        controller4 = connection.cursor()
        controller5 = connection.cursor()
        
        parts_number = 'SELECT count(DISTINCT partname) from data'
        reference_number = 'SELECT count(DISTINCT  reference) from data'
        min_hole ='SELECT MIN(number_of_holes),  reference from data'
        max_hole ='SELECT MAX(number_of_holes),  reference from data'
       
        
        controller2.execute(parts_number)
        controller3.execute(reference_number)
        controller4.execute(min_hole)
        controller5.execute(max_hole)
        

        
        reference_number_result = controller3.fetchone()
        parts_number_result = controller2.fetchone()
        min_hole_result= controller4.fetchone()
        max_hole_result=controller5.fetchone()
      
        
        self.num_of_ref_value.setText(str(reference_number_result[0]))
        self.num_parts_value.setText(str(parts_number_result[0]))
        self.min_num_hole_value.setText(str(min_hole_result[0]))
        self.max_num_hole_value.setText(str(max_hole_result[0]))
        self.min_num_holes_label_ref.setText(str(min_hole_result[1]))
        self.max_num_holes_label_ref.setText(str(max_hole_result[1]))
    
    def navigate(self):
        # establishing connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="inventory_manager", charset="utf8mb4")
        controller = connection.cursor()
        sql = 'SELECT * FROM data'
        result =controller.execute(sql)
        result = controller.fetchone()
        
        #defining and the widget in the textbox interface
        self.edit_inv_idlabel_2.setText(str(result[0]))
        self.edit_inv_reference_linedit.setText(str(result[1]))
        self.edit_inv_partname_linedit.setText(str(result[2]))
        self.edit_inv_minarea_linedit.setText(str(result[3]))
        self.edit_inv_max_area_linedit.setText(str(result[4]))
        self.edit_inv_numofholes_linedit.setText(str(result[5]))
        self.edit_inv_mindiameter_linedit.setText(str(result[6]))
        self.edit_inv_maxdiameter_linedit.setText(str(result[7]))
        self.edit_inv_count_linedit.setValue(result[8])
        
        
    # creating function to add data into the database
    def add(self):
         # establishing connection to the database
        connection = pymysql.connect(host="localhost", user="root", password="", database="inventory_manager", charset="utf8mb4")
        controller = connection.cursor()
        
        #defining and the widget in the textbox interface
        reference_ = str(self.edit_inv_reference_linedit.text())
        part_name_ = str(self.edit_inv_partname_linedit.text())
        min_area_  = float(self.edit_inv_minarea_linedit.text())
        max_area_  = float(self.edit_inv_max_area_linedit.text())
        number_of_holes_ = int(self.edit_inv_numofholes_linedit.text())
        min_diameter_ = float(self.edit_inv_mindiameter_linedit.text())
        max_diameter_ = float(self.edit_inv_maxdiameter_linedit.text())
        count_ = int(self.edit_inv_count_linedit.value())
        
        row = (reference_, part_name_, min_area_, max_area_, number_of_holes_, min_diameter_, max_diameter_, count_)
        # sql = 'UPDATE data SET reference = %s, partname=%s, minarea=%f,maxarea=%f, number_of_holes=%d, mindiameter=%f, maxdiameter=%f, count=%d'%(reference_, part_name_, min_area_, max_area_, number_of_holes_, min_diameter_, max_diameter_, count_)
        # sql = 'INSERT INTO data values("%s","%s","%f,%f,%d,%f,%f,%d) %(reference_, part_name_, min_area_, max_area_, number_of_holes_, min_diameter_, max_diameter_, count_)'
        # sql = 'INSERT INTO data(reference, partname, minarea, maxarea, number_of_holes, mindiameter, maxdiameter, count) VALUES(?,?,?,?,?,?,?,?)'
        sql = 'insert into data(reference, partname, minarea, maxarea, number_of_holes, mindiameter, maxdiameter, count) values("%s","%s","%f","%f", "%d","%f","%f","%d")' %(reference_, part_name_, min_area_, max_area_, number_of_holes_, min_diameter_, max_diameter_, count_)
        controller.execute(sql)
        connection.commit()

#method main begins execution of python program 
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    
if __name__ =="__main__":
    main() 
    