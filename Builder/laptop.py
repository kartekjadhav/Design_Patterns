class Laptop:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.screen_size = None
        self.ram = None
        self.storage = None

    def __repr__(self):
        return (f"Laptop Specs -> \n"
                f"CPU: {self.cpu}\n"
                f"GPU: {self.gpu}\n"
                f"Screen size: {self.screen_size}\n"
                f"RAM: {self.ram}\n"
                f"Storage: {self.storage}\n")