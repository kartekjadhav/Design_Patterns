from abc import ABC, abstractmethod

class EmployeeInterface(ABC):
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def delete(self):
        pass