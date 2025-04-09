from Vehicle import Vehicle
from .parkingSpot import ParkingSpot

class BikeParkingSpot(ParkingSpot):
    def __init__(self, spotNumber:int):
        super().__init__(spotNumber, 'bike')
    
    def canPark(self, vehcile:Vehicle):
        return self.spotType.lower() == vehcile.__class__.__name__.lower()