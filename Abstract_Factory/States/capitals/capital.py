from abc import ABC, abstractmethod

class Capital(ABC):
    @abstractmethod
    def population(self) -> int:
        pass
    
    @abstractmethod
    def attarctions(self) -> list:
        pass
    