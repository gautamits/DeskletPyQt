from PySide import QtCore, QtGui

app = QtGui.QApplication([])

window = QtGui.QWidget()
window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
window.show()

layout = QtGui.QVBoxLayout(window)
button = QtGui.QPushButton('Exit')
button.clicked.connect(app.quit)
layout.addWidget(button)

app.exec_()