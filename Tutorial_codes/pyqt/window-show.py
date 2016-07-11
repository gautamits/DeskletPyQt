import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()

window.setGeometry(100,100,200,50)
window.setWindowTitle("my first pyqt code")
window.show()
sys.exit(app.exec_())
