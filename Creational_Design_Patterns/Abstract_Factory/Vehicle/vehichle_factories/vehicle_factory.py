from abc import ABC, abstractmethod

class VehicleFactory(ABC):
    @abstractmethod
    def createCar(self):
        pass
    @abstractmethod
    def createBike(self):
        pass