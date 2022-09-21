# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'samtat_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SamtatReport(object):
    def setupUi(self, SamtatReport):
        SamtatReport.setObjectName("SamtatReport")
        SamtatReport.resize(1064, 895)
        SamtatReport.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SamtatReport)
        self.centralwidget.setObjectName("centralwidget")
        self.vehicle_class = QtWidgets.QComboBox(self.centralwidget)
        self.vehicle_class.setGeometry(QtCore.QRect(70, 140, 151, 22))
        self.vehicle_class.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.vehicle_class.setObjectName("vehicle_class")
        self.vehicle_class.addItem("")
        self.vehicle_class.addItem("")
        self.vehicle_class.addItem("")
        self.search_taradod = QtWidgets.QPushButton(self.centralwidget)
        self.search_taradod.setGeometry(QtCore.QRect(380, 220, 261, 41))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.search_taradod.setFont(font)
        self.search_taradod.setStyleSheet("")
        self.search_taradod.setObjectName("search_taradod")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dastgah_name = QtWidgets.QLineEdit(self.centralwidget)
        self.dastgah_name.setGeometry(QtCore.QRect(70, 90, 151, 31))
        self.dastgah_name.setObjectName("dastgah_name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_ostan = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ostan.setGeometry(QtCore.QRect(660, 90, 151, 22))
        self.comboBox_ostan.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_ostan.setObjectName("comboBox_ostan")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.comboBox_ostan.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(820, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_istgah = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_istgah.setGeometry(QtCore.QRect(660, 130, 151, 22))
        self.comboBox_istgah.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_istgah.setAutoFillBackground(False)
        self.comboBox_istgah.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_istgah.setObjectName("comboBox_istgah")
        self.comboBox_istgah.addItem("")
        self.comboBox_istgah.addItem("")
        self.comboBox_istgah.addItem("")
        self.takhalof_binary = QtWidgets.QCheckBox(self.centralwidget)
        self.takhalof_binary.setGeometry(QtCore.QRect(210, 180, 16, 17))
        self.takhalof_binary.setText("")
        self.takhalof_binary.setObjectName("takhalof_binary")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(750, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pelak_p1 = QtWidgets.QLineEdit(self.centralwidget)
        self.pelak_p1.setGeometry(QtCore.QRect(780, 180, 41, 31))
        self.pelak_p1.setObjectName("pelak_p1")
        self.pelak_p2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pelak_p2.setGeometry(QtCore.QRect(730, 180, 41, 31))
        self.pelak_p2.setObjectName("pelak_p2")
        self.pelak_p3 = QtWidgets.QLineEdit(self.centralwidget)
        self.pelak_p3.setGeometry(QtCore.QRect(630, 180, 41, 31))
        self.pelak_p3.setObjectName("pelak_p3")
        self.pelak_combo = QtWidgets.QComboBox(self.centralwidget)
        self.pelak_combo.setGeometry(QtCore.QRect(680, 190, 41, 22))
        self.pelak_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pelak_combo.setObjectName("pelak_combo")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.pelak_combo.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 270, 1041, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.image_downloder = QtWidgets.QPushButton(self.centralwidget)
        self.image_downloder.setGeometry(QtCore.QRect(280, 830, 261, 41))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.image_downloder.setFont(font)
        self.image_downloder.setStyleSheet("")
        self.image_downloder.setObjectName("image_downloder")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 840, 71, 21))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textline_taradod = QtWidgets.QLineEdit(self.centralwidget)
        self.textline_taradod.setGeometry(QtCore.QRect(560, 830, 151, 40))
        self.textline_taradod.setObjectName("textline_taradod")
        self.table_output = QtWidgets.QTableWidget(self.centralwidget)
        self.table_output.setGeometry(QtCore.QRect(20, 310, 1021, 491))
        self.table_output.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.table_output.setObjectName("table_output")
        self.table_output.setColumnCount(10)
        self.table_output.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(183, 188, 189))
        self.table_output.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_output.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_output.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_output.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_output.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_output.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_output.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_output.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_output.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_output.setHorizontalHeaderItem(9, item)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 800, 1041, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.end_time = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.end_time.setGeometry(QtCore.QRect(153, 20, 151, 22))
        self.end_time.setObjectName("end_time")
        self.start_time = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.start_time.setGeometry(QtCore.QRect(580, 20, 151, 22))
        self.start_time.setObjectName("start_time")
        SamtatReport.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(SamtatReport)
        self.statusBar.setObjectName("statusBar")
        SamtatReport.setStatusBar(self.statusBar)

        self.retranslateUi(SamtatReport)
        QtCore.QMetaObject.connectSlotsByName(SamtatReport)

    def retranslateUi(self, SamtatReport):
        _translate = QtCore.QCoreApplication.translate
        SamtatReport.setWindowTitle(_translate("SamtatReport", "MainWindow"))
        self.vehicle_class.setItemText(0, _translate("SamtatReport", "همه نوع"))
        self.vehicle_class.setItemText(1, _translate("SamtatReport", "سبک"))
        self.vehicle_class.setItemText(2, _translate("SamtatReport", "سنگین"))
        self.search_taradod.setText(_translate("SamtatReport", "جستجو"))
        self.label.setText(_translate("SamtatReport", "نام دستگاه"))
        self.label_2.setText(_translate("SamtatReport", "کلاس"))
        self.label_3.setText(_translate("SamtatReport", "متخلف"))
        self.comboBox_ostan.setItemText(0, _translate("SamtatReport", "همه استانها"))
        self.comboBox_ostan.setItemText(1, _translate("SamtatReport", "آذربایجان شرقی"))
        self.comboBox_ostan.setItemText(2, _translate("SamtatReport", "آذربایجان غربی    "))
        self.comboBox_ostan.setItemText(3, _translate("SamtatReport", "اردبیل    "))
        self.comboBox_ostan.setItemText(4, _translate("SamtatReport", "اصفهان    "))
        self.comboBox_ostan.setItemText(5, _translate("SamtatReport", "البرز"))
        self.comboBox_ostan.setItemText(6, _translate("SamtatReport", "ایلام"))
        self.comboBox_ostan.setItemText(7, _translate("SamtatReport", "بوشهر"))
        self.comboBox_ostan.setItemText(8, _translate("SamtatReport", "تهران"))
        self.comboBox_ostan.setItemText(9, _translate("SamtatReport", "چهارمحال و بختیاری"))
        self.comboBox_ostan.setItemText(10, _translate("SamtatReport", "خراسان جنوبی"))
        self.comboBox_ostan.setItemText(11, _translate("SamtatReport", "خراسان رضوی"))
        self.comboBox_ostan.setItemText(12, _translate("SamtatReport", "خراسان شمالی"))
        self.comboBox_ostan.setItemText(13, _translate("SamtatReport", "خوزستان"))
        self.comboBox_ostan.setItemText(14, _translate("SamtatReport", "زنجان"))
        self.comboBox_ostan.setItemText(15, _translate("SamtatReport", "سمنان"))
        self.comboBox_ostan.setItemText(16, _translate("SamtatReport", "سیستان و بلوچستان"))
        self.comboBox_ostan.setItemText(17, _translate("SamtatReport", "فارس"))
        self.comboBox_ostan.setItemText(18, _translate("SamtatReport", "قزوین"))
        self.comboBox_ostan.setItemText(19, _translate("SamtatReport", "قم"))
        self.comboBox_ostan.setItemText(20, _translate("SamtatReport", "کردستان"))
        self.comboBox_ostan.setItemText(21, _translate("SamtatReport", "کرمان"))
        self.comboBox_ostan.setItemText(22, _translate("SamtatReport", "کرمانشاه"))
        self.comboBox_ostan.setItemText(23, _translate("SamtatReport", "کهکیلویه و بویر احمد"))
        self.comboBox_ostan.setItemText(24, _translate("SamtatReport", "گلستان"))
        self.comboBox_ostan.setItemText(25, _translate("SamtatReport", "گیلان"))
        self.comboBox_ostan.setItemText(26, _translate("SamtatReport", "لرستان"))
        self.comboBox_ostan.setItemText(27, _translate("SamtatReport", "مازندران"))
        self.comboBox_ostan.setItemText(28, _translate("SamtatReport", "مرکزی"))
        self.comboBox_ostan.setItemText(29, _translate("SamtatReport", "هرمزگان"))
        self.comboBox_ostan.setItemText(30, _translate("SamtatReport", "همدان"))
        self.comboBox_ostan.setItemText(31, _translate("SamtatReport", "یزد"))
        self.label_4.setText(_translate("SamtatReport", "استان مبداء/مقصد"))
        self.label_5.setText(_translate("SamtatReport", "نوع ایستگاه کنترل"))
        self.comboBox_istgah.setItemText(0, _translate("SamtatReport", "همه"))
        self.comboBox_istgah.setItemText(1, _translate("SamtatReport", "دوربین"))
        self.comboBox_istgah.setItemText(2, _translate("SamtatReport", "WIM"))
        self.label_7.setText(_translate("SamtatReport", "تاریخ/ساعت شروع"))
        self.label_8.setText(_translate("SamtatReport", "تاریخ/ساعت پایان"))
        self.label_6.setText(_translate("SamtatReport", "پلاک"))
        self.pelak_combo.setItemText(0, _translate("SamtatReport", "الف"))
        self.pelak_combo.setItemText(1, _translate("SamtatReport", "ب"))
        self.pelak_combo.setItemText(2, _translate("SamtatReport", "پ"))
        self.pelak_combo.setItemText(3, _translate("SamtatReport", "ت"))
        self.pelak_combo.setItemText(4, _translate("SamtatReport", "ث"))
        self.pelak_combo.setItemText(5, _translate("SamtatReport", "ج"))
        self.pelak_combo.setItemText(6, _translate("SamtatReport", "چ"))
        self.pelak_combo.setItemText(7, _translate("SamtatReport", "ح"))
        self.pelak_combo.setItemText(8, _translate("SamtatReport", "خ"))
        self.pelak_combo.setItemText(9, _translate("SamtatReport", "د"))
        self.pelak_combo.setItemText(10, _translate("SamtatReport", "ذ"))
        self.pelak_combo.setItemText(11, _translate("SamtatReport", "ر"))
        self.pelak_combo.setItemText(12, _translate("SamtatReport", "ز"))
        self.pelak_combo.setItemText(13, _translate("SamtatReport", "ژ"))
        self.pelak_combo.setItemText(14, _translate("SamtatReport", "س"))
        self.pelak_combo.setItemText(15, _translate("SamtatReport", "ش"))
        self.pelak_combo.setItemText(16, _translate("SamtatReport", "ص"))
        self.pelak_combo.setItemText(17, _translate("SamtatReport", "ض"))
        self.pelak_combo.setItemText(18, _translate("SamtatReport", "ط"))
        self.pelak_combo.setItemText(19, _translate("SamtatReport", "ظ"))
        self.pelak_combo.setItemText(20, _translate("SamtatReport", "ع"))
        self.pelak_combo.setItemText(21, _translate("SamtatReport", "غ"))
        self.pelak_combo.setItemText(22, _translate("SamtatReport", "ف"))
        self.pelak_combo.setItemText(23, _translate("SamtatReport", "ق"))
        self.pelak_combo.setItemText(24, _translate("SamtatReport", "ک"))
        self.pelak_combo.setItemText(25, _translate("SamtatReport", "گ"))
        self.pelak_combo.setItemText(26, _translate("SamtatReport", "ل"))
        self.pelak_combo.setItemText(27, _translate("SamtatReport", "م"))
        self.pelak_combo.setItemText(28, _translate("SamtatReport", "ن"))
        self.pelak_combo.setItemText(29, _translate("SamtatReport", "و"))
        self.pelak_combo.setItemText(30, _translate("SamtatReport", "ه"))
        self.pelak_combo.setItemText(31, _translate("SamtatReport", "ی"))
        self.image_downloder.setText(_translate("SamtatReport", "دانلود عکس"))
        self.label_9.setText(_translate("SamtatReport", "شماره تردد"))
        item = self.table_output.horizontalHeaderItem(0)
        item.setText(_translate("SamtatReport", "ردیف"))
        item = self.table_output.horizontalHeaderItem(1)
        item.setText(_translate("SamtatReport", "شماره تردد"))
        item = self.table_output.horizontalHeaderItem(2)
        item.setText(_translate("SamtatReport", "زمان تردد"))
        item = self.table_output.horizontalHeaderItem(3)
        item.setText(_translate("SamtatReport", "شماره پلاک"))
        item = self.table_output.horizontalHeaderItem(4)
        item.setText(_translate("SamtatReport", "سرعت"))
        item = self.table_output.horizontalHeaderItem(5)
        item.setText(_translate("SamtatReport", "دستگاه"))
        item = self.table_output.horizontalHeaderItem(6)
        item.setText(_translate("SamtatReport", "کلاس"))
        item = self.table_output.horizontalHeaderItem(7)
        item.setText(_translate("SamtatReport", "سیستم"))
        item = self.table_output.horizontalHeaderItem(8)
        item.setText(_translate("SamtatReport", "DEV_LATITUDE"))
        item = self.table_output.horizontalHeaderItem(9)
        item.setText(_translate("SamtatReport", "DEV_LONGITUDE"))
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SamtatReport = QtWidgets.QMainWindow()
    ui = Ui_SamtatReport()
    ui.setupUi(SamtatReport)
    SamtatReport.show()
    sys.exit(app.exec_())
