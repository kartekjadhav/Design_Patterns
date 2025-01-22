from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def startCar(self):
        pass
    @abstractmethod
    def accelarateCar(self):
        pass