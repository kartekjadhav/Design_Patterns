from abc import ABC, abstractmethod

class AnimalHandler(ABC):
    def __init__(self):
        self._next_handler = None
    @abstractmethod
    def handle():
        pass
    @abstractmethod
    def set_next():
        pass