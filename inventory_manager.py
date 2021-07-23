# importation of modules and classes to be used in the program 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import sqlite3

import sys, os
from os import path
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

from PyQt5.sip import dump
from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(resource_path("roboto.ui"))

class Main(QMainWindow, FORM_CLASS):
    # creating class properties to handle database connection
    connection = sqlite3.connect(resource_path("parts.db"))  # establishing connection to the database
    #creating a controller object for managing database query
    controller = connection.cursor()
    
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
        self.delete_btn.clicked.connect(self.delete)
        self.update_btn.clicked.connect(self.update)
    
    
    # function to search for item in the inventory
    def search(self, id):
        nbr = int(self.count_level_filter.text())
       
        sql = 'SELECT * FROM parts_table WHERE count < %d'%(nbr)
        Main.controller.execute(sql)
        result = Main.controller.fetchall()
        
        #initialization of the number of rows in the table
        self.inventory_table.setRowCount(0)
        
        #looping through the returned data
        for row_count, row_data in enumerate(result):
            self.inventory_table.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.inventory_table.setItem(row_count, column_count, QTableWidgetItem(str(data)))
    def level(self):
        sql = 'SELECT reference, partname, count FROM parts_table order by count asc limit 3'
        Main.controller.execute(sql)
        result = Main.controller.fetchall()
        
        #initialization of the number of rows in the table
        self.inventory_stat_table.setRowCount(0)
        
        #looping through the returned dat
        for row_count, row_data in enumerate(result):
            self.inventory_stat_table.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.inventory_stat_table.setItem(row_count, column_count, QTableWidgetItem(str(data)))
        
    # function that pulls data from the database
    def getData(self):
        sql = '''SELECT * FROM parts_table'''
        Main.controller.execute(sql)
        result = Main.controller.fetchall()
        
        #initialization of the number of rows in the table
        self.inventory_table.setRowCount(0)
        
        #looping through the returned dat
        for row_count, row_data in enumerate(result):
            self.inventory_table.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.inventory_table.setItem(row_count, column_count, QTableWidgetItem(str(data)))
        #simple code to display reference number and parts nubmer
        controller2 = Main.connection.cursor()
        controller3 = Main.connection.cursor()
        controller4 = Main.connection.cursor()
        controller5 = Main.connection.cursor()
        
        parts_number = 'SELECT count(DISTINCT partname) from parts_table'
        reference_number = 'SELECT count(DISTINCT  reference) from parts_table'
        min_hole ='SELECT MIN(numberofholes),  reference from parts_table'
        max_hole ='SELECT MAX(numberofholes),  reference from parts_table'
       
        
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
        sql = 'SELECT * FROM parts_table'
        result = Main.controller.execute(sql)
        result = Main.controller.fetchone()
        
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
        #defining and the widget in the textbox interface
        reference_ = str(self.edit_inv_reference_linedit.text())
        part_name_ = str(self.edit_inv_partname_linedit.text())
        min_area_  = float(self.edit_inv_minarea_linedit.text())
        max_area_  = float(self.edit_inv_max_area_linedit.text())
        number_of_holes_ = int(self.edit_inv_numofholes_linedit.text())
        min_diameter_ = float(self.edit_inv_mindiameter_linedit.text())
        max_diameter_ = float(self.edit_inv_maxdiameter_linedit.text())
        count_ = int(self.edit_inv_count_linedit.value())
        
        row = (reference_,part_name_,min_area_,max_area_,number_of_holes_,min_diameter_,max_diameter_,count_)
        sql = '''INSERT INTO parts_table(reference, partname, minarea, maxarea, numberofholes, mindiameter, maxdiameter, count) VALUES(?,?,?,?,?,?,?,?)'''
        Main.controller.execute(sql,row)
        Main.connection.commit()
    def delete(self):
        d = int(self.edit_inv_idlabel_2.text())
        sql = 'DELETE FROM data where id=%d'%(d)
        Main.controller.execute(sql)
        Main.connection.commit()
        
    def update(self):
        #defining and the widget in the textbox interface
        id = int(self.edit_inv_idlabel_2.text())
        reference_ = str(self.edit_inv_reference_linedit.text())
        part_name_ = str(self.edit_inv_partname_linedit.text())
        min_area_  = float(self.edit_inv_minarea_linedit.text())
        max_area_  = float(self.edit_inv_max_area_linedit.text())
        number_of_holes_ = int(self.edit_inv_numofholes_linedit.text())
        min_diameter_ = float(self.edit_inv_mindiameter_linedit.text())
        max_diameter_ = float(self.edit_inv_maxdiameter_linedit.text())
        count_ = int(self.edit_inv_count_linedit.value())
        
        row = (reference_,part_name_,min_area_,max_area_,number_of_holes_,min_diameter_,max_diameter_,count_, id)
        sql = '''UPDATE parts_table SET reference=?, partname=?, minarea=?, maxarea=?, numberofholes=?, mindiameter=?, maxdiameter=?, count=? where id = ?'''
        Main.controller.execute(sql,row)
        Main.connection.commit()
        
    def delete(self):
        d = int(self.edit_inv_idlabel_2.text())
        sql = 'DELETE FROM parts_table where id=%d'%(d)
        Main.controller.execute(sql)
        Main.connection.commit()
        
#method main begins execution of python program 
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    
if __name__ =="__main__":
    main() 
    