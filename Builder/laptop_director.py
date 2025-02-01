from laptop_builders import Laptop_Builder, Gaming_Laptop_Builder, Office_Laptop_Builder

class Laptop_Director:
    def __init__(self, builder: Laptop_Builder):
        self.builder = builder
    
    def construct_gaming_laptop(self):
        self.builder.build_CPU("Intel i9")
        self.builder.build_GPU("NVIDIA RTX 3080")
        self.builder.build_RAM(32)
        self.builder.build_Screen(17)
        self.builder.build_Storage(1000)
        return self.builder.get_Laptop()
    
    def construct_office_laptop(self):
        self.builder.build_CPU("Intel i5")
        self.builder.build_GPU("Integrated Intel UHD Graphics")
        self.builder.build_RAM(16)
        self.builder.build_Screen(15)
        self.builder.build_Storage(512)
        return self.builder.get_Laptop()