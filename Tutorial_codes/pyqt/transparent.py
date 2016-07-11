import sys
from PyQt4 import QtGui, QtCore, Qt

class ZoomWidget(QtGui.QWidget):
    def __init__(self):  
        QtGui.QWidget.__init__(self)
        self.setAttribute(Qt.Qt.WA_NoSystemBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color:transparent;")
        self.setGeometry(100,100,100,100)


        



        self.show()        

    def paintEvent(self, e=None): 
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen( QtGui.QPen(QtCore.Qt.gray,3,QtCore.Qt.DashDotLine ) )
        qp.drawRect(0,0,self.rect().width()-1, self.rect().height()-1)  
        qp.end()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ZoomWidget()
    sys.exit(app.exec_())