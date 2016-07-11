from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys

class myLineEdit(QtGui.QLineEdit):
  @pyqtSlot(QtCore.QString)
  def textChanged(self, string):
    QtGui.QMessageBox.information(self,"Hello!","Current String is:\n"+string)  

def main():    
    app 	 = QtGui.QApplication(sys.argv)
    lineEdit	 = myLineEdit()

    #Resize width and height
    lineEdit.resize(250,250)    
    lineEdit.setWindowTitle('PyQt QLineEdit Text Changed Example')  
    
    lineEdit.connect(lineEdit,SIGNAL("textChanged(QString)"),
					lineEdit,SLOT("textChanged(QString)"))
    lineEdit.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
