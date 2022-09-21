from PyQt5 import QtCore, QtGui, QtWidgets
from samtat_ui import Ui_SamtatReport
import sys

class ui_events(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SamtatReport()
        self.ui.setupUi(self)
        self.ui.search_taradod.clicked.connect(self.search_taradod)
        self.ui.image_downloder.clicked.connect(self.search_tasvir)

    def search_taradod(self):
        try:
            start_time = self.ui.start_time.dateTime()
            end_time = self.ui.end_time.dateTime()
            ostan = self.ui.comboBox_ostan.currentIndex()
            control_station = self.ui.comboBox_istgah.currentIndex()
            class_name = self.ui.vehicle_class.currentIndex()
            pelak_p1 = self.ui.pelak_p1.text()
            pelak_p2 = self.ui.pelak_p2.text()
            pelak_p3 = self.ui.pelak_p3.text()
            pelak_combo = self.ui.pelak_combo.currentIndex()
            takhalof = self.ui.takhalof_binary.checkState()
            self.oracle_query(self,start_time,end_time,ostan,control_station,class_name,takhalof,pelak_p1,pelak_p2,pelak_p3,pelak_combo)
        except:
            pass

    def search_tasvir(self):
        try:
            taradod_id = self.ui.textline_taradod.text()
            self.mongodb_query(self,taradod_id)
        except:
            pass

    def oracle_query(self,start_time,end_time,ostan,control_station,class_name,takhalof,pelak_p1,pelak_p2,pelak_p3,pelak_combo):
        try:
            import cx_Oracle
            connection = cx_Oracle.connect(user="root", password= 'userpwd', dsn="dbhost.example.com/orclpdb1")
            # Obtain a cursor
            cursor = connection.cursor()
            # Execute the query
            sql = """SELECT *
            FROM taradod
            WHERE start_time BETWEEN :start AND :end """
            cursor.execute(sql, start=start_time, end=end_time)
            # Loop over the result and set result tabel
            for row in cursor:
                self.ui.table_output.setItem(row, column, newItem)            
        except:
            pass
        
    def mongodb_query(self,taradod_id):
        import pymongo
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["taradod_database"]
        mycol = mydb["tasvir_table"]
        myquery = { "taradod_id": taradod_id }
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ui_events()
    ui.show()
    sys.exit(app.exec_())