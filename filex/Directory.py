from PyQt5 import QtGui, QtCore, QtWidgets
import sys,os
from FileSystem import FileSystem

class Directory(QtWidgets.QWidget):
    copy_dir_event = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(Directory, self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
        self.directory_icon = QtWidgets.QLabel()
        icon_path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'folder_icon.png')
        self.directory_icon.setPixmap(QtGui.QPixmap(icon_path))
        
        self.directory_label = QtWidgets.QLabel()
        
        self.directory_line_edit = QtWidgets.QLineEdit()
        
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.directory_icon)
        self.horizontal_layout.addWidget(self.directory_label)
        self.horizontal_layout.addWidget(self.directory_line_edit)
        
        self.directory_line_edit.hide()
        
        self.setLayout(self.horizontal_layout)
        
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)
        
    def get_directory_name(self):
        return self.directory_label.text()
    
    def set_directory_name(self, dir_name):
        self.directory_label.setText(dir_name)
        self.directory_label.setAlignment(QtCore.Qt.AlignLeft)
        

    def openMenu(self,position):
        
        menu = QtWidgets.QMenu()
        rename_directory_action = menu.addAction("Rename Directory")
        delete_directory_action = menu.addAction("Delete Directory")
        copy_directory_action = menu.addAction("Copy Directory")
        action = menu.exec_(self.mapToGlobal(position))
        
        if action == rename_directory_action:
            self.directory_label.hide()
            self.directory_line_edit.show()
            self.directory_line_edit.returnPressed.connect(self.rename_dir)
            
        if action == delete_directory_action:
            self.hide()
            FileSystem.delete_directory(self,self.directory_label.text())
            
        if action == copy_directory_action:
            FileSystem.copy_directory(self,self.directory_label.text())
            self.copy_dir_event.emit(self.directory_label.text()+ " - Copy")
            self.raise_()

            
    def rename_dir(self):
        i = self.directory_label.text().rfind("\\")
        new_name = os.path.join(self.directory_label.text()[0:i],self.directory_line_edit.text())
        FileSystem.rename_directory(self,self.directory_label.text(), new_name)
        self.set_directory_name(new_name)
        self.directory_line_edit.hide()
        self.directory_label.show()
            
    
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    directory = Directory()
    sys.exit(app.exec_())