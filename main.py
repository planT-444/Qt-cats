import sys
from MainWindow import MainWindow
from PySide2.QtWidgets import QApplication

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()