from abc import ABC, abstractmethod
from laptop import Laptop

class Laptop_Builder(ABC):
    def __init__(self):
        self.laptop = Laptop()

    @abstractmethod
    def build_CPU(self, cpu):
        pass

    @abstractmethod
    def build_GPU(self, gpu):
        pass

    @abstractmethod
    def build_Screen(self, screen_size):
        pass

    @abstractmethod
    def build_RAM(self, ram):
        pass

    @abstractmethod
    def build_Storage(self, storage):
        pass

    def get_Laptop(self):
        return self.laptop
        