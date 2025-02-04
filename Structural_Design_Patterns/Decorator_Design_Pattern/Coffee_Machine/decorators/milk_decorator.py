from .coffee_decorator import CoffeeDecorator

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def cost(self):
        return self._coffee.cost() + 5