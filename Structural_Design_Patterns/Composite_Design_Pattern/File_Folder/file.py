from fileSystemComponent import FileSystemComponent

class File(FileSystemComponent):
    def __init__(self, filename):
        self._name = filename
    
    def showDetails(self):
        print(f"{__class__.__name__} : {self._name}")