from abc import ABC, abstractmethod

class Milkshake(ABC):
    @abstractmethod
    def createShake(self):
        pass