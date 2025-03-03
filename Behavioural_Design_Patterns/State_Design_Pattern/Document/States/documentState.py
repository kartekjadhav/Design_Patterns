from abc import ABC, abstractmethod

class DocumentState(ABC):
    @abstractmethod
    def edit(self):
        pass
    
    @abstractmethod
    def review(self):
        pass
    
    @abstractmethod
    def finalize(self):
        pass