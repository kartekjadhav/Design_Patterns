from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def renderCircle(self):
        pass
    
    @abstractmethod
    def renderSquare(self):
        pass

    @abstractmethod
    def renderTriangle(self):
        pass