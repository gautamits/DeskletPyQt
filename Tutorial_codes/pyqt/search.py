import sys
from subprocess import call
from PyQt4 import QtGui, QtCore
from PyQt4 import Qt
import commands
class button(QtGui.QPushButton):
	 def __init__( self, parent=None):
		super(button, self).__init__(parent)

		self.pushButton = QtGui.QPushButton(self.i)
		self.pushButton.clicked.connect(lambda:call(["xdg-open",self.i]))
		#layout = QtGui.QHBoxLayout()
		#layout.addWidget(self.pushButton)
		#self.setLayout(layout)

class Window(QtGui.QMainWindow):
	def __init__(self):
		self.buttons=[]
		self.button_maps={}
		super(Window,self).__init__()
		self.setGeometry(50,50,1100,50)
		self.setWindowTitle("my second pyqt code")
		self.setWindowIcon(QtGui.QIcon('logo.png'))
		#self.show()
		# scroll area widget contents - layout
		

		# main layout
		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
		# add all main to the main vLayout
		#self.mainLayout.addWidget(self.addButton)
		self.entry = QtGui.QLineEdit(self)
		self.entry.editingFinished.connect(self.handleEditingFinished)
		self.mainLayout.addWidget(self.entry)
		self.secondaryLayout = QtGui.QVBoxLayout()
		self.secondaryLayout.setAlignment(QtCore.Qt.AlignTop)
		self.secondaryLayout.setMargin(0)
		self.secondaryLayout.setSpacing(0)
		self.mainLayout.setMargin(0)
		self.mainLayout.setSpacing(0)
		#self.secondaryLayout.setStretch(1,0)
		self.mainLayout.addLayout(self.secondaryLayout)

		self.b = QtGui.QPushButton("hello",self)
		self.mainLayout.addWidget(self.b)
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
		self.centralWidget = QtGui.QWidget()
		self.centralWidget.setLayout(self.mainLayout)

		# set central widget
		self.setCentralWidget(self.centralWidget)
		
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
				#btn.clicked.connect(lambda i:call(["xdg-open",i]))
				btn.clicked.connect(self.create_connect(self.button_maps[i]))
				self.buttons.append(btn)
				#self.scrollLayout.addRow(btn)
				#self.mainLayout.addWidget(btn)
				self.secondaryLayout.addWidget(btn)
		self.secondaryLayout.update()
		self.mainLayout.update()
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
