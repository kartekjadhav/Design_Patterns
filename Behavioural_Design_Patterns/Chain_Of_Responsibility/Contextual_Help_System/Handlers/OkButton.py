from .Component import Component

class OkButton(Component):
    def __init__(self, tooTipText=None):
        super().__init__()
        self.toolTipText = tooTipText