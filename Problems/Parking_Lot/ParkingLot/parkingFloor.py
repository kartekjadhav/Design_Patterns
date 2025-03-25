from Vehicle import Vehicle, Bike, Car
from ParkingSpot import CarParkingSpot, BikeParkingSpot
class ParkingFloor():
    def __init__(self, floorNumber:int, noOfCarSpots:int, noOfBikeSpots:int):
        self.floorNumber = floorNumber
        self.noOfCarSpots = noOfCarSpots
        self.noOfBikeSpots = noOfBikeSpots
        self.spots = []

        #Fill Bike spots
        for i in range(self.noOfBikeSpots):
            self.spots.append(BikeParkingSpot(i+1))
        #Fill Car spots
        for i in range(self.noOfCarSpots):
            self.spots.append(CarParkingSpot(i+self.noOfBikeSpots+1))
    
    def getParkingSpots(self):
        return self.spots
    
    def findAvailableSpot(self, vehicle:Vehicle):
        for spot in self.spots:
            if spot.canPark(vehicle):
                return spot
        return None
    
    def getFloorNumber(self):
        return self.floorNumber