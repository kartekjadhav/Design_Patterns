from .coffee_decorator import CoffeeDecorator

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def cost(self):
        return self._coffee.cost() + 10