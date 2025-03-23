from .ComponentWithContextualHelp import ComponentWithContextualHelp

class Component(ComponentWithContextualHelp):
    def __init__(self):
        self.container = None
        self.toolTipText = None
        
    def help(self):
        if self.toolTipText:
            return self.toolTipText
        elif self.container:
            return self.container.help()
        else:
            return "No help text found"

    def set_container(self, container):
        self.container = container
        return self.container