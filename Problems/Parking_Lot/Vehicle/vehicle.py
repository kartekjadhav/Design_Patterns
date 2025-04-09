from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, licensePlate, vehicleType):
        self.licensePlate = licensePlate
        self.vehicleType = vehicleType
    
    def getLicensePlate(self) -> str:
        return self.licensePlate
    
    def getVehicleType(self) -> str:
        return self.vehicleType
    
    @abstractmethod
    def calculateFare(hoursStayed:int) -> float:
        pass