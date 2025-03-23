from .Container import Container

class Dialog(Container):
    def __init__(self, url):
        super().__init__()
        self.url = url
    
    def help(self):
        if self.url:
            return self.url
        else:
            return super().help()