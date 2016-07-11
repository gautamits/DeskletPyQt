import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("my second pyqt code")
		self.setWindowIcon(QtGui.QIcon('logo.png'))
		#self.show()
		
		########## code fo main menu ###################
		extractAction = QtGui.QAction("&GEt to the choppah", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave the app')
		extractAction.triggered.connect(self.close_application)
		
		self.statusBar()
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		
		
		self.home()
	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		#btn.resize(100,100)
		#btn.resize(btn.sizeHint())
		btn.resize(btn.minimumSizeHint())
		btn.move(100,100)
		#btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(self.close_application)
		
		
		#################  toolbar code #############
		extractAction = QtGui.QAction(QtGui.QIcon("images.jpg"),"flee the scene",self)
		extractAction.triggered.connect(self.close_application)
		self.toolBar= self.addToolBar("Extraction")
		self.toolBar.addAction(extractAction)
		
		###########checkbox code ###########
		checkBox = QtGui.QCheckBox('Enlarge Window',self)
		checkBox.move(100,25)
		checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)
		
		self.show()
	def enlarge_window(self,state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,600)
		else:
			self.setGeometry(50,50,500,300)
	def close_application(self):
		#print ("so custom")
		
		############ popup code #############
		choice = QtGui.QMessageBox.question(self,'extract', "Get into the chopper?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print "exiting now"
			sys.exit()
		else:
			pass
		
def run():
	app=QtGui.QApplication(sys.argv)
	GUI= Window()
	sys.exit(app.exec_())
run()
