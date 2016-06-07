from PyQt5 import QtGui, QtCore, QtWidgets
import sys

class File(QtWidgets.QWidget):

    def __init__(self):
        super(File,self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
        self.file_icon = QtWidgets.QLabel()
        self.file_icon.setPixmap(QtGui.QPixmap('file_icon.png'))
        self.file_label = QtWidgets.QLabel()
        
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.file_icon)
        self.horizontal_layout.addWidget(self.file_label)
        
        self.setLayout(self.horizontal_layout)
        
    def set_file_name(self, file_name):
        self.file_label.setText(file_name)
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    file = File()
    sys.exit(app.exec_())