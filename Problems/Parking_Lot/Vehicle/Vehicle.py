from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, licensePlate, type):
        self.licensePlate = licensePlate
        self.type = type
    
    def getVehicleType(self):
        return self.type

    @abstractmethod
    def calculateFare(hoursParked: float):
        pass

    def getLicensePlate(self):
        return self.licensePlate