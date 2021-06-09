from PyQt5.QtWidgets import * 

#Create table 
def upsertTableContents( self , table_data , header_names): 

    #Row count 
    self.setRowCount(len(table_data))  

    #Column count 
    self.setColumnCount(len(header_names))   
    self.setHorizontalHeaderLabels(header_names)
    
    # Column width adjustments
    for n in range ( len(header_names)):
        if n == 0 :
            self.setColumnWidth(n, 75)
        elif n==len(header_names) -1 :
            header = self.horizontalHeader()
            header.setSectionResizeMode(n, QHeaderView.Stretch)
        else:
            self.setColumnWidth ( n , 150)
    # self.setColumnWidth(0, 75)
    # self.setColumnWidth(1, 150)
    # self.setColumnWidth(2, 150)
    # self.setColumnWidth(3, 150)
    # self.setColumnWidth(4, 150)
    
    
    
    for rowID, row_item in enumerate(table_data):
        for ColID, Col_item in enumerate ( row_item) :
            self.setItem(rowID,ColID, QTableWidgetItem(str(Col_item) )) 