from abc import ABC, abstractmethod

class Bike(ABC):
    @abstractmethod
    def startBike(self):
        pass
    @abstractmethod
    def accelarateBike(self):
        pass