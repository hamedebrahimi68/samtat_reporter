import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from samtat_ui import Ui_SamtatReport



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SamtatReport = QtWidgets.QMainWindow()
    ui = Ui_SamtatReport()
    ui.setupUi(SamtatReport)
    SamtatReport.show()
    sys.exit(app.exec_())