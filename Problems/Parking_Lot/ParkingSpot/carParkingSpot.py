from .parkingSpot import ParkingSpot
from Vehicle import Vehicle, Car

class CarParkingSpot():
    def __init__(self, spotNumber:int):
        super().__init__(spotNumber, "Car")
    
    def canPark(self, vehicle:Vehicle):
        if self.occupied:
            return False
        return isinstance(vehicle, Car)