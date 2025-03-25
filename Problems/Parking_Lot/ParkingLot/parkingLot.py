# ParkingLot
# floors: List<ParkingFloor>
# ---------------------------------
# ParkingLot(floors)
# findAvailableSpot(vehicle:Vehicle)
# getSpot(spotNumber, floor)
# parkVehicle(vehicle:Vehicle)
# vacateVehicle(vehicle: Vehicle)

from .parkingFloor import ParkingFloor
from ParkingSpot import ParkingSpot
from Vehicle import Vehicle

class ParkingLot():
    def __init__(self, noOfFloors=1, noOfBikeSpotsPerFloor=1, noOfCarSpotsPerFloor=1):
        self.floors = [ ParkingFloor(i, noOfCarSpotsPerFloor, noOfBikeSpotsPerFloor) for i in range(noOfFloors)]
    
    def findAvailableSpot(self, vehicle:Vehicle):
        for floor in self.floors:
            spot = floor.findAvailableSpot(vehicle)
            if spot:
                return [spot, floor]
        print(f"No empty spot for {vehicle.getVehicleType()}")
        return [None, None]

    def park(self, vehicle:Vehicle):
        spot, floor = self.findAvailableSpot(vehicle)
        if spot:
            spot.parkVehicle(vehicle)
            print(f"Parked {vehicle.getVehicleType()} at spot {spot.getSpotNumber()} on floor {floor.getFloorNumber()}")
    
    def vacate(self, spot:ParkingSpot):
        spot.vacate()
    
    def getSpotByNumber(self, floorNumber:int, spotNumber:int):
        if floorNumber > len(self.floors) or floorNumber < 0:
            print("Invalid floor")
        else: 
            floor = self.floors[floorNumber]
            spots = floor.getParkingSpots()
            if 1 <= spotNumber <= len(spots):
                return spots[spotNumber-1]
            else:
                print("Invalid spot.")