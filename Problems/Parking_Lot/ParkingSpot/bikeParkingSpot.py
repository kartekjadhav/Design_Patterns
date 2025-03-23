from .parkingSpot import ParkingSpot
from Vehicle import Vehicle, Bike

class CarParkingSpot():
    def __init__(self, spotNumber:int):
        super().__init__(spotNumber, "Bike")
    
    def canPark(self, vehicle:Vehicle):
        if self.occupied:
            return False
        return isinstance(vehicle, Bike)