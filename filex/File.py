from PyQt5 import QtGui, QtCore, QtWidgets
import sys,os
from FileSystem import FileSystem

class File(QtWidgets.QWidget):

    def __init__(self):
        super(File,self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
        self.file_icon = QtWidgets.QLabel()
        icon_path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'file_icon.png')
        self.file_icon.setPixmap(QtGui.QPixmap(icon_path))
        
        self.file_label = QtWidgets.QLabel()
        
        self.file_line_edit = QtWidgets.QLineEdit()
        
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.addWidget(self.file_icon)
        self.horizontal_layout.addWidget(self.file_label)
        self.horizontal_layout.addWidget(self.file_line_edit)
        
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)
        
        self.file_line_edit.hide()
        
        self.setLayout(self.horizontal_layout)
        
    def set_file_name(self, file_name):
        self.file_label.setText(file_name)
        
    def openMenu(self,position):
        
        menu = QtWidgets.QMenu()
        rename_file_action = menu.addAction("Rename File")
        delete_file_action = menu.addAction("Delete File")
        action = menu.exec_(self.mapToGlobal(position))
        
        if action == rename_file_action:
            self.file_label.hide()
            self.file_line_edit.show()
            self.file_line_edit.returnPressed.connect(self.rename_file)
        if action == delete_file_action:
            self.hide()
            FileSystem.delete_file(self,self.file_label.text())
            
    def rename_file(self):
        i = self.file_label.text().rfind("\\")
        new_name = os.path.join(self.file_label.text()[0:i], self.file_line_edit.text())
        FileSystem.rename_file(self,self.file_label.text(), new_name)
        self.set_file_name(new_name)
        self.file_line_edit.hide()
        self.file_label.show()
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    file = File()
    sys.exit(app.exec_())