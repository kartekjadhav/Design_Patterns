from datetime import datetime
from Vehicle import Car, Bike, Truck, Vehicle
class Ticket:
    def __init__(self, parkingSpot:ParkingSpot, vehicle:Vehicle):
        self.parkingSpot = parkingSpot
        self.vehicle = vehicle
        self.startTime = datetime.now()
        