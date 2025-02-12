from abc import ABC, abstractmethod
from Adaptee import (AnalyticModel3D)


class Adaptor(ABC):
    def __init__(self):
        self._analyticModel3d = AnalyticModel3D()
    @abstractmethod
    def createModel(self):
        pass
