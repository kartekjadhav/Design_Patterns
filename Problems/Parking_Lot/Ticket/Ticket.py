from Vehicle import Vehicle, Car
from datetime import datetime
class Ticket():
    def __init__(self, vehicle:Vehicle, parkingSpot):
        self.vehicle = vehicle
        self.parkingSpot = parkingSpot
        self.startTime =  datetime.now()
