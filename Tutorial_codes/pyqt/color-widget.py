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
		
		
		
		########### font code #########
		fontChoice = QtGui.QAction("Font",self)
		fontChoice.triggered.connect(self.font_choice)
		#self.toolBar= self.addToolBar("Font")
		self.toolBar.addAction(fontChoice)
		
		
		############ color widget ##########
		color = QtGui.QColor(0,0,0)
		fontColor = QtGui.QAction('Font bg color',self)
		fontColor.triggered.connect(self.color_picker)
		
		self.toolBar.addAction(fontColor)
		
		
		
		
		###########checkbox code ###########
		checkBox = QtGui.QCheckBox('Enlarge Window',self)
		checkBox.move(300,25)
		checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)
		
		
		############# progress bar code ################
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200, 80, 250, 20)
		
		self.btn = QtGui.QPushButton("Download",self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)
		
		
		############ changing style #######################
		print self.style().objectName()
		self.styleChoice = QtGui.QLabel("linux",self)
		
		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("windowsvista")
		
		comboBox.move(50,250)
		self.styleChoice.move(50,150)
		comboBox.activated[str].connect(self.style_choice)
		
		##########  calendar ##############
		
		cal = QtGui.QCalendarWidget(self)
		cal.move(500,200)
		cal.resize(200,200)
		
		self.show()
	def color_picker(self):
		color = QtGui.QColorDialog.getColor()
		self.styleChoice.setStyleSheet("QWidget { background-color : %s}" %color.name())
	def font_choice(self):
		font,valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)
	
	def style_choice(self,text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
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
	def download(self):
		self.completed=0
		while self.completed <100 :
			self.completed += 0.0001
			self.progress.setValue(self.completed)	
def run():
	app=QtGui.QApplication(sys.argv)
	GUI= Window()
	sys.exit(app.exec_())
run()
