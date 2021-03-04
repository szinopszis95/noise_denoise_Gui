import sys

from PySide2 import QtGui
from PySide2.QtWidgets import QApplication

from GUI.ui_main import MainWindow

app = QApplication(sys.argv)
QtGui.QFontDatabase.addApplicationFont('./GUI/fonts/segoeui.ttf')
QtGui.QFontDatabase.addApplicationFont('./GUI/fonts/segoeuib.ttf')
window = MainWindow()
sys.exit(app.exec_())
