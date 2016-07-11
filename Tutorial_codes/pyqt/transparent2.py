import sys
from PyQt4 import QtGui, QtCore, Qt
import sys
from subprocess import call
import commands
class ZoomWidget(QtGui.QWidget):
    def __init__(self):  
        QtGui.QWidget.__init__(self)
        self.setAttribute(Qt.Qt.WA_NoSystemBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setStyleSheet("background-color: rgba(100,50,50,80%);")
        #self.setGeometry(100,100,100,100)

        self.button_maps={}
        self.setGeometry(50,50,1100,50)
        

        # main layout
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop)


        self.mainLayout.setMargin(5)
        self.mainLayout.setSpacing(5)


        ########################## exit button #############
        self.toolLayout = QtGui.QHBoxLayout()
        self.toolLayout.setAlignment(QtCore.Qt.AlignRight)
        self.quit = QtGui.QPushButton("quit",self)
        self.quit.resize(25,25)
        self.quit.setStyleSheet("background-color: rgba(100,50,50,100%);")
        #self.quit.move(1050,0)
        self.quit.clicked.connect(self.close_application)
        self.toolLayout.addWidget(self.quit)

        self.mainLayout.addLayout(self.toolLayout)


        ###############         secondary layout, contains dynamic buttons ##################


        self.secondaryLayout = QtGui.QVBoxLayout()
        self.secondaryLayout.setAlignment(QtCore.Qt.AlignTop)
        self.secondaryLayout.setMargin(5)
        self.secondaryLayout.setSpacing(5)
        

        self.entry = QtGui.QLineEdit(self)
        self.entry.editingFinished.connect(self.handleEditingFinished)
        self.entry.setWindowOpacity(1)
        self.entry.setStyleSheet("background-color: rgba(50,50,50,80%);")


        self.mainLayout.addWidget(self.entry)
        self.mainLayout.addLayout(self.secondaryLayout)

        self.setLayout(self.mainLayout)



        self.show()        

    def paintEvent(self, e=None): 
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen( QtGui.QPen(QtCore.Qt.gray,3,QtCore.Qt.DashDotLine ) )
        qp.drawRect(0,0,self.rect().width()-1, self.rect().height()-1)  
        qp.end()

    def close_application(self):
        #print ("so custom")
        
        ############ popup code #############
        choice = QtGui.QMessageBox.question(self,'extract', "Get into the chopper?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print "exiting now"
            sys.exit()
        else:
            pass
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
                btn.setStyleSheet("background-color: rgba(50,50,50,80%);")
                btn.clicked.connect(self.create_connect(self.button_maps[i]))
                self.secondaryLayout.addWidget(btn)
        self.secondaryLayout.update()
        self.mainLayout.update()
        #self.window.paintEvent()
        self.updateSize()
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
    
    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ZoomWidget()
    sys.exit(app.exec_())