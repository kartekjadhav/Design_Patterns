from abc import ABC, abstractmethod
from Vehicle import Vehicle
class ParkingSpot(ABC):
    def __init__(self, spotNumber:int, spotType:str):
        self.spotNumber = spotNumber
        self.spotType = spotType
        self.isOccupied = False
        self.vehicle = None
    
    def getSpotNumber(self):
        return self.spotNumber

    def getVehicle(self):
        if self.vehicle:
            return self.vehicle
        print(f"No vehicle is parked at {self.spotNumber}.")
        return None
    
    def getSpotType(self):
        return self.spotType.lower()
    
    @abstractmethod
    def canPark(self, vehcile:Vehicle):
        pass

    def parkVehicle(self, vehicle:Vehicle):
        if not self.isOccupied:
            if self.canPark(vehicle):
                self.vehicle = vehicle
                self.isOccupied = True
                print(f"Your vehicle has been parked at {self.spotNumber}.")
            else:
                print(f"Can't park {self.vehicle.__class__.__name__} on {self.spotType} parking spot.")
        else:
            print("Cant park on occupied spot.")
    
    def vacate(self):
        if self.isOccupied:
            self.isOccupied = False
            self.vehicle = None
        else:
            print("THis parking spot is already empty.")
