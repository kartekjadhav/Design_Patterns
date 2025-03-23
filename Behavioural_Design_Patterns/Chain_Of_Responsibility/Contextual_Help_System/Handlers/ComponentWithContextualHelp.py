from abc import ABC, abstractmethod

class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def help(self):
        pass