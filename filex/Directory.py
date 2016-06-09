from PyQt5 import QtGui, QtCore, QtWidgets
import sys,os

class Directory(QtWidgets.QWidget):
    
    def __init__(self):
        super(Directory, self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
        self.directory_icon = QtWidgets.QLabel()
        icon_path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'folder_icon.png')
        self.directory_icon.setPixmap(QtGui.QPixmap(icon_path))
        
        self.directory_label = QtWidgets.QLabel()
        
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.directory_icon)
        self.horizontal_layout.addWidget(self.directory_label)
        
        self.setLayout(self.horizontal_layout)
        
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)
        
    
    def set_directory_name(self, dir_name):
        self.directory_label.setText(dir_name)
        self.directory_label.setAlignment(QtCore.Qt.AlignLeft)
        
    def openMenu(self,position):
        
        menu = QtWidgets.QMenu()
        rename_directory_action = menu.addAction("Rename Directory")
        delete_directory_action = menu.addAction("Delete Directory")
        action = menu.exec_(self.mapToGlobal(position))
    
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    directory = Directory()
    sys.exit(app.exec_())