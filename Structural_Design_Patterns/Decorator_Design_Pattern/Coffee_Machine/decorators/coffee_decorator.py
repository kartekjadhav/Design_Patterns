from abc import ABC, abstractmethod
from coffees import (Coffee, BlackCoffee, SimpleCoffee)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee:Coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass