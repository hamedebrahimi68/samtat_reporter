from PyQt5 import QtCore, QtGui, QtWidgets
from samtat_ui import Ui_SamtatReport
import sys

class ui_events(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SamtatReport()
        self.ui.setupUi(self)
        self.ui.search_taradod.clicked.connect(self.search_taradod)
    
    def search_taradod(self):
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
        print(start_time,end_time,ostan,control_station,class_name,takhalof,pelak_p1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ui_events()
    ui.show()
    sys.exit(app.exec_())