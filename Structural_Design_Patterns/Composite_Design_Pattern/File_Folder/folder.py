from fileSystemComponent import FileSystemComponent

class Folder(FileSystemComponent):
    def __init__(self, foldername):
        self._name = foldername
        self._childrens = []

    def showDetails(self):
        print(f"{__class__.__name__} : {self._name} -> ")
        for i in self._childrens:
            print(f"{i.__class__.__name__} : {i._name}")
    
    def add(self, item:FileSystemComponent):
        self._childrens.append(item)
    
    def remove(self, item:FileSystemComponent):
        self._childrens.remove(item)