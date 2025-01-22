from .vehicle_factory import VehicleFactory
from Cars.audi_car import Audi_Car
from Bikes.audi_bike import Audi_Bike

class Audi_Factory(VehicleFactory):
    def createBike(self):
        return Audi_Bike()
    def createCar(self):
        return Audi_Car()