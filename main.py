import sys
from CatWindow import CatWindow
from PySide2.QtWidgets import QApplication

app = QApplication(sys.argv)
window = CatWindow()
window.show()
app.exec_()