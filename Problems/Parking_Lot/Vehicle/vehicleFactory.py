from .car import Car
from .bike import Bike
from .truck import Truck

class VehicleFactory:
    @staticmethod
    def createVehicle(licensePlate:str, vehicleType:str):
        match vehicleType.lower():
            case 'car':
                return Car(licensePlate)
            case 'bike':
                return Bike(licensePlate)
            case 'truck':
                return Truck(licensePlate)
            case _:
                print("Invalid vehicle type")
                return None