import sys
from subprocess import call
from PyQt4 import QtGui, QtCore
#from PySide import QtCore, QtGui

from PyQt4 import Qt
import commands
class ZoomWidget(QtGui.QWidget):
    def __init__(self):  
        QtGui.QWidget.__init__(self)
        self.setAttribute(Qt.Qt.WA_NoSystemBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color:transparent;")
        #self.setGeometry(100,100,100,100)
        #self.show()        

    def paintEvent(self, e=None): 
        self.qp = QtGui.QPainter()
        self.qp.begin(self)
        self.qp.setPen( QtGui.QPen(QtCore.Qt.gray,3,QtCore.Qt.DashDotLine ) )
        self.qp.drawRect(0,0,self.rect().width()-1, self.rect().height()-1)  
        self.qp.end()



class Window(QtGui.QMainWindow):
	def __init__(self):
		
		super(Window,self).__init__()
		self.buttons=[]
		self.button_maps={}
		#self.setStyleSheet("background-color: rgba(255,255,255,50);")
		#self.setWindowOpacity(0.7)
		self.setGeometry(50,50,1100,50)
		self.setWindowTitle("my second pyqt code")
		self.setWindowIcon(QtGui.QIcon('logo.png'))
		#self.setAttribute(Qt.WA_TranslucentBackground)
		#self.show()
		# scroll area widget contents - layout
		

		# main layout
		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.setAlignment(QtCore.Qt.AlignTop)


		self.mainLayout.setMargin(5)
		self.mainLayout.setSpacing(5)

		self.secondaryLayout = QtGui.QVBoxLayout()
		self.secondaryLayout.setAlignment(QtCore.Qt.AlignTop)
		self.secondaryLayout.setMargin(5)
		self.secondaryLayout.setSpacing(5)
		

		self.entry = QtGui.QLineEdit(self)
		self.entry.editingFinished.connect(self.handleEditingFinished)
		#self.entry.setWindowOpacity(1)
		#self.entry.setStyleSheet("background-color: rgba(0,0,0,100%);")
		self.mainLayout.addWidget(self.entry)
		#self.secondaryLayout.setStretch(1,0)
		self.mainLayout.addLayout(self.secondaryLayout)
		# add all main to the main vLayout
		#self.mainLayout.addWidget(self.addButton)
		
		"""

		self.centralWidget = QtGui.QWidget(self)
		self.centralWidget.setLayout(self.mainLayout)
		self.centralWidget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.centralWidget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setCentralWidget(self.centralWidget)

		"""
		self.window = ZoomWidget()
		self.window.setLayout(self.mainLayout)
		self.setCentralWidget(self.window)


		
		"""
		self.scrollLayout = QtGui.QFormLayout()

		# scroll area widget contents
		self.scrollWidget = QtGui.QWidget()
		self.scrollWidget.setLayout(self.scrollLayout)

		# scroll area
		self.scrollArea = QtGui.QScrollArea()
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setWidget(self.scrollWidget)

		self.mainLayout.addWidget(self.scrollArea)

		"""
		# central widget
		
		#self.centralWidget.setWindowOpacity(0.5)
		#self.centralWidget.setStyleSheet("background-color: rgba(255, 255, 255, 20%);")
		#self.addWidget(self.centralWidget)
		#self.mainLayout.update()
		self.show()
	

	

	def handleEditingFinished(self):
		if self.entry.isModified():
			# do interesting stuff ...
			self.removeButtons()
			self.button_maps.clear()
			text=self.entry.text()
			text='"'+text+'"'
			command='locate -i '+str(text)+' | grep -e "/mnt" -e "/media" -e "/home" | grep -v "/\." | grep -v "android" | grep -v "Android" | grep -v "workspace"'
			#print 'Editing Finished'
			result=commands.getstatusoutput(command)
		
			a,result=result
			result=result.split('\n')
			result=result[:15]
			for i in result:
				self.button_maps[i]=i
			for i in result:
				print i
				top = i.split("/")
				top=top[len(top)-1]
				btn = QtGui.QPushButton(top,self)
				btn.resize(btn.minimumSizeHint())
				btn.clicked.connect(self.create_connect(self.button_maps[i]))
				self.secondaryLayout.addWidget(btn)
		self.secondaryLayout.update()
		self.mainLayout.update()
		self.window.paintEvent()
		self.show()
				
		#print self.buttons	
		self.entry.setModified(False)
	def create_connect(self,x):
		return lambda: call(["xdg-open",x])
	def close_application(self):
		print ("so custom")
		sys.exit()
	def removeButtons(self):
	    for cnt in reversed(range(self.secondaryLayout.count())):
	        # takeAt does both the jobs of itemAt and removeWidget
	        # namely it removes an item and returns it
	        widget = self.secondaryLayout.takeAt(cnt).widget()

	        if widget is not None: 
	            # widget will be None if the item is a layout
	            widget.deleteLater()
	    self.secondaryLayout.update()
	    self.mainLayout.update()



def run():
	app=QtGui.QApplication(sys.argv)
	GUI= Window()
	sys.exit(app.exec_())
run()
