import sys
from PyQt4 import QtGui,QtCore

class tabdemo(QtGui.QTabWidget):
	def __init__(self,parent=None):
		super(tabdemo, self).__init__(parent)
		self.tab1 = QtGui.QWidget()
		self.tab2 = QtGui.QWidget()
		self.tab3 = QtGui.QWidget()

		self.addTab(self.tab1,"Add Paths")
		self.addTab(self.tab2,"Ignored Paths")
		self.addTab(self.tab3,"Tab 3")
		self.tab1UI()
		self.tab2UI()
		self.tab3UI()
		self.setWindowTitle("tab demo")
		
	"""def tab1UI(self):
		layout = QtGui.QFormLayout()
		layout.addRow("Name",QtGui.QLineEdit())
		layout.addRow("Address",QtGui.QLineEdit())
		self.setTabText(0,"Contact Details")
		self.tab1.setLayout(layout)
	"""
	def tab1UI(self):
		layout = QtGui.QHBoxLayout()
		


		mygroupbox = QtGui.QGroupBox('this is my groupbox')
		myform = QtGui.QHBoxLayout()
		mygroupbox.setLayout(myform)
		mylist = myListWidget()
		mylist.addItem("item 1")


		scroll = QtGui.QScrollArea()
		#scroll.setWidget(mygroupbox)
		scroll.setWidget(mylist)
		scroll.setWidgetResizable(True)
		scroll.setFixedHeight(400)


		secondaryLayout = QtGui.QVBoxLayout()
		secondaryLayout.setAlignment(QtCore.Qt.AlignTop)
		add=QtGui.QPushButton("Add")
		delete=QtGui.QPushButton("Delete")
		save=QtGui.QPushButton("Save")
		secondaryLayout.addWidget(add)
		secondaryLayout.addWidget(delete)
		secondaryLayout.addWidget(save)
		layout.addWidget(scroll)
		layout.addLayout(secondaryLayout)
		self.tab1.setLayout(layout)


		
	"""def tab2UI(self):
		layout = QtGui.QFormLayout()
		sex = QtGui.QHBoxLayout()
		sex.addWidget(QtGui.QRadioButton("Male"))
		sex.addWidget(QtGui.QRadioButton("Female"))
		layout.addRow(QtGui.QLabel("Sex"),sex)
		layout.addRow("Date of Birth",QtGui.QLineEdit())
		self.setTabText(1,"Ignored Paths")
		self.tab2.setLayout(layout)
	"""
	def tab2UI(self):
		layout = QtGui.QHBoxLayout()
		


		#mygroupbox = QtGui.QGroupBox('this is my groupbox')
		#myform = QtGui.QHBoxLayout()
		#mygroupbox.setLayout(myform)
		mylist = myListWidget()
		mylist.addItem("item 2")
		mylist.itemClicked.connect(mylist.Clicked)


		scroll = QtGui.QScrollArea()
		#scroll.setWidget(mygroupbox)
		scroll.setWidget(mylist)
		scroll.setWidgetResizable(True)
		scroll.setFixedHeight(400)


		secondaryLayout = QtGui.QVBoxLayout()
		secondaryLayout.setAlignment(QtCore.Qt.AlignTop)
		add=QtGui.QPushButton("Add")
		delete=QtGui.QPushButton("Delete")
		save=QtGui.QPushButton("Save")
		secondaryLayout.addWidget(add)
		secondaryLayout.addWidget(delete)
		secondaryLayout.addWidget(save)
		layout.addWidget(scroll)
		layout.addLayout(secondaryLayout)
		self.tab2.setLayout(layout)
		
	def tab3UI(self):
		layout = QtGui.QHBoxLayout()
		layout.addWidget(QtGui.QLabel("subjects")) 
		layout.addWidget(QtGui.QCheckBox("Physics"))
		layout.addWidget(QtGui.QCheckBox("Maths"))
		self.setTabText(2,"Education Details")
		self.tab3.setLayout(layout)
		
class myListWidget(QtGui.QListWidget):

   def Clicked(self,item):
      QtGui.QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		#self.setGeometry(50,50,500,300)
		self.setWindowTitle("preferences")

		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.setAlignment(QtCore.Qt.AlignTop)
		self.tabWidget = tabdemo(self)
		#self.tabWidget.setMinimumHeight(500)
		#self.setMinimumWidth(500)
		self.tabWidget.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		#self.tabWidget.setGeometry(50,50,100,100)
		self.mainLayout.addWidget(self.tabWidget)
		self.setLayout(self.mainLayout)

		

		#self.setWindowIcon(QtGui.QIcon('logo.png'))
		self.show()
app=QtGui.QApplication(sys.argv)
GUI= tabdemo()
GUI.show()
sys.exit(app.exec_())