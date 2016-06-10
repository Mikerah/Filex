import os, shutil, send2trash, subprocess,sys

class FileSystem():
        
    @staticmethod
    def get_default_directory(self):
        return os.path.expanduser("~")
        
    @staticmethod
    def list_directory_contents(self, directory):
        dir_contents = [os.path.join(directory, i) for i in os.listdir(directory)]
        return dir_contents
        
    @staticmethod
    def get_current_working_directory(self):
        return os.getcwd()
        
    @staticmethod
    def change_current_working_directory(self, directory):
        os.chdir(directory)
        
    def move_directory(self, source, destination):
        pass
        
    def move_file(self, source, destination):
        pass
        
    def copy_directory(self, source, destination):
        pass
        
    def copy_file(self, source, destination):
        pass
    
    @staticmethod
    def rename_directory(self,old_name, new_name):
        os.rename(old_name, new_name)
        
    @staticmethod
    def rename_file(self,old_name,new_name):
        os.rename(old_name,new_name)
        
    @staticmethod
    def delete_directory(self,directory_to_delete):
        send2trash.send2trash(directory_to_delete)
        
    def delete_file(self,file_to_delete):
        send2trash.send2trash(file_to_delete)
    
    @staticmethod
    def add_directory(self, new_directory="New Directory"):
        from Directory import Directory
        os.mkdir(os.path.join(FileSystem.get_current_working_directory(self), new_directory))
        directory = Directory()
        directory.set_directory_name(new_directory)
        return directory
    
    @staticmethod
    def add_file(self, new_file="New File"):
        from File import File
        f = open(os.path.join(FileSystem.get_current_working_directory(self), new_file), "w")
        file = File()
        file.set_file_name(new_file)
        return file
        
    @staticmethod
    def open_file(self, file_to_open):
        if sys.platform.startswith("win32"):
            os.startfile(file_to_open, "open")
        elif sys.platform.startswith("darwin"):
            os.startfile(file_to_open,"open")
        elif sys.platform.startswith("linux"):
            os.startfile(file_to_open,"xdg-open ")
        