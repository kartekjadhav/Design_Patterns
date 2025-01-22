from .vehicle_factory import VehicleFactory
from Cars.bmw_car import BMW_Car
from Bikes.bmw_bike import BMW_Bike


class BMW_Factory(VehicleFactory):
    def createBike(self):
        return BMW_Bike()
    def createCar(self):
        return BMW_Car()