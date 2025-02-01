from .laptop_builder import Laptop_Builder

class Gaming_Laptop_Builder(Laptop_Builder):
    def __init__(self):
        super().__init__()
    def build_CPU(self, cpu):
        print(f"Building {cpu} CPU")
        self.laptop.cpu = cpu 

    def build_GPU(self, gpu):
        print(f"Building {gpu} GPU")
        self.laptop.gpu = gpu

    def build_Screen(self, screen_size):
        print(f"Building {screen_size} cm screen")
        self.laptop.screen_size = screen_size

    def build_RAM(self, ram):
        print(f"Building {ram} GB RAM")
        self.laptop.ram = ram

    def build_Storage(self, storage):
        print(f"Building {storage} GB storage")
        self.laptop.storage = storage
