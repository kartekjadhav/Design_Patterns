from .Container import Container

class Panel(Container):
    def __init__(self, modalText):
        super().__init__()
        self.modalText = modalText
    
    def help(self):
        if self.modalText:
            return self.modalText
        else:
            return super().help()