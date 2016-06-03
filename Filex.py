from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import FileSystem

class Filex(QtWidgets.QMainWindow):

    def __init__(self):
        super(Filex, self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
        pass
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    filex = Filex()
    filex.show()
    sys.exit(app.exec_())