import sys
from PyQt4 import QtGui,QtCore
import numpy as np

class tabdemo(QtGui.QTabWidget):
	def __init__(self,parent=None):
		super(QtGui.QTabWidget, self).__init__(parent)
		self.tab1 = tab(self)
		self.tab2 = tab(self)
		tab1Name="addDirectories"
		tab2Name = "ignoreDirectories"
		self.tab1.name(tab1Name)
		self.tab2.name(tab2Name)
		self.addTab(self.tab1,"Add Paths")
		self.addTab(self.tab2,"Ignored Paths")
		
		try:
			addDirectories=np.load(tab1Name+".npy")
			for i in addDirectories:
				self.tab1.mylist.addItem(QtGui.QListWidgetItem(i))
		except:
			print "White Listed Directories data not found"
		try:
			ignoreDirectories=np.load(tab2Name+".npy")
			for i in ignoreDirectories:
					self.tab2.mylist.addItem(QtGui.QListWidgetItem(i))
		except:
			print "blacklisted directories data not found"
		self.setWindowTitle("tab demo")

class myListWidget(QtGui.QListWidget):
	def __init__(self,parent):
		super(QtGui.QListWidget, self).__init__(parent)

	def Clicked(self, item):
		#QtGui.QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
		print "clicked ",item.text()
	def current(self,item):
		try:
			return self.currentItem().text()
		except:
			return None
	def allItems(self,item):
		itemsTextList =  [str(self.item(i).text()) for i in range(self.count())]
		return itemsTextList


class tab(QtGui.QWidget):
	def __init__(self,parent):
		super(QtGui.QWidget, self).__init__(parent)
		layout = QtGui.QHBoxLayout()
		self.mylist = myListWidget(self)
		scroll = QtGui.QScrollArea()
		scroll.setWidget(self.mylist)
		scroll.setWidgetResizable(True)
		scroll.setFixedHeight(400)


		secondaryLayout = QtGui.QVBoxLayout()
		secondaryLayout.setAlignment(QtCore.Qt.AlignTop)
		self.add=QtGui.QPushButton("Add")
		self.delete=QtGui.QPushButton("Delete")
		self.save=QtGui.QPushButton("Save")
		
		self.delete.setEnabled(False)

		self.add.clicked.connect(self.addFunction)
		self.delete.clicked.connect(self.deleteFunction)
		self.save.clicked.connect(self.saveFunction)

		#self.mylist.itemClicked.connect(self.mylist.Clicked)
		self.mylist.itemClicked.connect(self.Clicked)

		secondaryLayout.addWidget(self.add)
		secondaryLayout.addWidget(self.delete)
		secondaryLayout.addWidget(self.save)
		layout.addWidget(scroll)
		layout.addLayout(secondaryLayout)
		self.setLayout(layout)
	def addFunction(self):
		print "add clicked"
		file = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory to add"))
		self.mylist.addItem(QtGui.QListWidgetItem(file))
	def  deleteFunction(self):
		obj=self.mylist.current(self.mylist)
		if obj is not None:
			print "deleting ",obj
			item = self.mylist.takeItem(self.mylist.currentRow())
			item = None
			self.delete.setEnabled(False)
		else:
			print "none selected"
	def saveFunction(self):
		print "saving in",self.name
		print "save clicked",self.mylist.allItems(self.mylist)
		np.save(self.name+".npy",np.array(self.mylist.allItems(self.mylist)))
	def name(self,string):
		self.name=string
	def Clicked(self):
		self.delete.setEnabled(True)

app=QtGui.QApplication(sys.argv)
GUI= tabdemo()
GUI.show()
sys.exit(app.exec_())