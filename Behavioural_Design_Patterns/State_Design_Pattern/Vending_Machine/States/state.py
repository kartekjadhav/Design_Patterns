from abc import ABC, abstractmethod

class VendingMachineState(ABC):
    
    def __init__(self, machine):
        self._machine = machine
    
    @abstractmethod
    def insertCoin(self, amount):
        pass
    
    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def selectItem(self):
        pass

    @abstractmethod
    def despenseItem(self):
        pass