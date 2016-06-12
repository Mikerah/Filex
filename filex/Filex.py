from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from FileSystem import FileSystem
from Directory import Directory
from File import File

class Filex(QtWidgets.QWidget):

    def __init__(self):
        super(Filex, self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
        
        default_dir = FileSystem.get_default_directory(self)
    
        # Next Button
        self.next_button = QtWidgets.QPushButton('', self)
        self.next_button.setIcon(QtGui.QIcon('next_button_icon.png'))
        
        # Back Button
        self.back_button = QtWidgets.QPushButton('', self)
        self.back_button.setIcon(QtGui.QIcon('back_button_icon.png'))
        
        # Search Path Line Edit
        self.display_path = QtWidgets.QLineEdit()
        self.set_search_path(default_dir)
        
        # Adding back button, next button and line edit to inner container layout
        self.inner_horizontal_layout = QtWidgets.QHBoxLayout()
        self.inner_horizontal_layout.addWidget(self.back_button)
        self.inner_horizontal_layout.addWidget(self.next_button)
        self.inner_horizontal_layout.addWidget(self.display_path)
        
        # Add container layout to container widget
        self.inner_widget = QtWidgets.QWidget()
        self.inner_widget.setLayout(self.inner_horizontal_layout)
        
        self.scroll_area_widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        
        # Retrieve directory content and dynamically create Directory and File Widgets
        self.open_directory(default_dir)
            
        self.scroll_area_widget.setLayout(self.layout)
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.scroll_area.customContextMenuRequested.connect(self.open_menu)
        
        
        self.vertical_box_layout = QtWidgets.QVBoxLayout()
        self.vertical_box_layout.addWidget(self.inner_widget)
        self.vertical_box_layout.addWidget(self.scroll_area)
        
        self.setLayout(self.vertical_box_layout)
        
        self.setWindowTitle(FileSystem.get_current_working_directory(self))
        
    def open_directory(self, directory):
        dir_contents = FileSystem.list_directory_contents(self,directory)
        for i in range(len(dir_contents)):
            if os.path.isdir(dir_contents[i]):
                directory = Directory()
                directory.set_directory_name(dir_contents[i])
                directory.installEventFilter(self)
                self.layout.addWidget(directory)
            else:
                file = File()
                file.set_file_name(dir_contents[i])
                file.installEventFilter(self)
                self.layout.addWidget(file)
                
    def set_search_path(self,directory):
        FileSystem.change_current_working_directory(self,directory)
        self.display_path.setText(FileSystem.get_current_working_directory(self))
              
        
    def eventFilter(self, obj, event):
        if isinstance(obj, Directory) and (event.type() == QtCore.QEvent.MouseButtonDblClick):
            directory_to_retrieve = self.layout.itemAt(self.layout.indexOf(obj)).widget()
            self.set_search_path(directory_to_retrieve.get_directory_name())
            self.clear_layout()
            self.open_directory(directory_to_retrieve.get_directory_name())
        elif isinstance(obj, Directory) and (event.type() == QtCore.QEvent.ContextMenu):
            directory_to_retrieve.copy_dir_event.connect(self.copy_dir)
                
        elif isinstance(obj, File) and (event.type() == QtCore.QEvent.ContextMenu):
            file_to_retrieve = self.layout.itemAt(self.layout.indexOf(obj)).widget()
            if event.type() == QtCore.QEvent.ContextMenu:
                file_to_retrieve.copy_file_event.connect(self.copy_file)
            
                
        return super(Filex, self).eventFilter(obj,event)
        
    def copy_file(self, name):
        file = File()
        file.set_file_name(name)
        self.layout.addWidget(file)
        
    def copy_dir(self, name):
        directory = Directory()
        directory.set_directory_name(name)
        self.layout.addWidget(directory)
           
    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            child.widget().deleteLater()
        
    def open_menu(self, position):
        menu = QtWidgets.QMenu()
        create_directory_action = menu.addAction("Create New Directory")
        create_new_file_action = menu.addAction("Create New File")
        action = menu.exec_(self.scroll_area.mapToGlobal(position))
        if action == create_directory_action:
            new_directory = FileSystem.add_directory(self)
            self.layout.addWidget(new_directory)
        if action == create_new_file_action:
            new_file = FileSystem.add_file(self)
            self.layout.addWidget(new_file)
        
        
        
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    filex = Filex()
    filex.show()
    sys.exit(app.exec_())