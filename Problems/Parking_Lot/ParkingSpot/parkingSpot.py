from abc import ABC, abstractmethod
from Vehicle import Vehicle

class ParkingSpot(ABC):
    def __init__(self, spotNumber:int, spotType:str):
        self.spotNumber = spotNumber
        self.spotType = spotType
        self.vehicle = None
        self.occupied = False
    
    def getSpotType(self):
        return self.spotType

    def getVehicle(self):
        return self.vehicle
    
    def getSpotNumber(self):
        return self.spotNumber
    
    def isOccupied(self):
        return self.occupied

    @abstractmethod
    def canPark(self, vehicleType:str):
        pass
    def parkVehicle(self, vehicle: Vehicle):
        if self.canPark(vehicle):
            self.vehicle = vehicle
            self.occupied = True
        else:
            print("Cannot park on occupied spot!")
    
    def vacate(self):
        if not self.occupied:
            print(f"Spot {self.spotNumber} is already empty.")
        else:
            self.vehicle = None
            self.occupied = False
            print(f"Spot {self.spotNumber} has been vacated.")
    
    def __str__(self):
        return (f"Parking Spot number - {self.spotNumber}\n"
                f"Parking Spot Type - {self.spotType}\n"
                f"Currently occupied - {self.occupied}\n"
                )