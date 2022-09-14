import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from samtat_ui import Ui_SamtatReport

# Filename: signals_slots.py
"""Signals and slots."""

def show_msg():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("اتصال به دیتا بیس لطفا صبر کنید...")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('گزارش تردد سامانه سمتات')
layout = QVBoxLayout()

btn = QPushButton('گزارش گیری')
btn.clicked.connect(show_msg)  # Connect clicked to show_msg()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())