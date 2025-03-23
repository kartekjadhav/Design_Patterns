from .Vehicle import Vehicle
from .Car import Car
from .Bike import Bike

class VehicleFactory():
    def getVehicle(self, type:str, licensePlate:str):
        type = type.lower()
        if type == 'car':
            return Car(licensePlate)
        elif type == 'bike':
            return Bike(licensePlate)
        else:
            return None