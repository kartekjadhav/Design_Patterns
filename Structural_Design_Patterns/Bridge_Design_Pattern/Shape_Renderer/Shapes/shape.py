from abc import ABC, abstractmethod
from Renderers import Renderer

class Shape(ABC):
    def __init__(self, renderer:Renderer):
        self._renderer = renderer
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass