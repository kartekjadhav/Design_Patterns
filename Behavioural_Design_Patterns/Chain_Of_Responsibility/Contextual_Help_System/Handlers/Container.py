from .Component import Component

class Container(Component):
    def __init__(self):
        super().__init__()
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return self.children