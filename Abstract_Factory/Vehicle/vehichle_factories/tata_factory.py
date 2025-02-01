from .vehicle_factory import VehicleFactory
from Cars.tata_car import Tata_Car

class Tata_Factory(VehicleFactory):
    def createBike(self):
        print(f"Tata does not manufacture bikes yet")
    def createCar(self):
        return Tata_Car()