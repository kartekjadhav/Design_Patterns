from Vehicle import Vehicle
from .parkingSpot import ParkingSpot

class CarParkingSpot(ParkingSpot):
    def __init__(self, spotNumber:int):
        super().__init__(spotNumber, 'car')
    
    def canPark(self, vehcile:Vehicle):
        return self.spotType.lower() == vehcile.__class__.__name__.lower()