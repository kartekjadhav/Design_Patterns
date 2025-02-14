from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def showDetails(self):
        pass