import random
from math import floor
class CarModel:
    def __init__(self, name, color):
        self._name = name
        self._color = color
    
    def render(self, coords):
        print(f"Rendering {self._name} of color {self._color} at point {coords} - id {id(self)}")

class FactoryCarModel:
    def __init__(self):
        self.carmap = {}
    
    def getCarModel(self, name, color):
        if (name, color) not in self.carmap:
            self.carmap[(name, color)] = CarModel(name, color)
        return self.carmap[(name, color)]

#Client Code
factory = FactoryCarModel()
cars = []

for index in range(5):
    model = factory.getCarModel("Lamborghini", "Purple")
    cars.append(model)

for car in cars:
    car.render((floor(random.random()*10), floor(random.random()*10)))