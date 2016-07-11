import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("my second pyqt code")
		self.setWindowIcon(QtGui.QIcon('logo.png'))
		#self.show()
		self.home()
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.resize(100,100)
		btn.move(100,100)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.show()
		
def run():
	app=QtGui.QApplication(sys.argv)
	GUI= Window()
	sys.exit(app.exec_())
run()
