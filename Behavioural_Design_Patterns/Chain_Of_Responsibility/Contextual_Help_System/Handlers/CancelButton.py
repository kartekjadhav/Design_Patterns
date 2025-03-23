from .Component import Component

class CancelButton(Component):
    def __init__(self, tooTipText=None):
        super().__init__()
        self.toolTipText = tooTipText