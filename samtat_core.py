from PyQt5 import QtCore, QtGui, QtWidgets
from samtat_ui import Ui_SamtatReport

class ui_events(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SamtatReport()
        self.ui.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SamtatReport = QtWidgets.QMainWindow()
    ui = Ui_SamtatReport()
    ui.setupUi(SamtatReport)
    SamtatReport.show()
    sys.exit(app.exec_())