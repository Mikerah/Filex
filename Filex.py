from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import FileSystem
import Directory
import File

class Filex(QtWidgets.QWidget):

    def __init__(self):
        super(Filex, self).__init__()
        
        self.init_ui()
        
    def init_ui(self):
    
        # Next Button
        self.next_button = QtWidgets.QPushButton('', self)
        self.next_button.setIcon(QtGui.QIcon('next_button_icon.png'))
        
        # Back Button
        self.back_button = QtWidgets.QPushButton('', self)
        self.back_button.setIcon(QtGui.QIcon('back_button_icon.png'))
        
        # Search Path Line Edit
        self.display_path = QtWidgets.QLineEdit()
        
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
        for i in range(5):
            dir = Directory.Directory()
            self.layout.addWidget(dir)
            
            file = File.File()
            self.layout.addWidget(file)
        self.scroll_area_widget.setLayout(self.layout)
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_area_widget)
        
        
        self.vertical_box_layout = QtWidgets.QVBoxLayout()
        self.vertical_box_layout.addWidget(self.inner_widget)
        self.vertical_box_layout.addWidget(self.scroll_area)
        
        self.setLayout(self.vertical_box_layout)
        
        
        
        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    filex = Filex()
    filex.show()
    sys.exit(app.exec_())