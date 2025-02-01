from laptop_director import Laptop_Director
import laptop_builders
from inspect import getmembers, isabstract, isclass 

if __name__ == "__main__":
    members = getmembers(laptop_builders, lambda m: isclass(m) and not isabstract(m) and issubclass(m, laptop_builders.Laptop_Builder))
    builders_map = {a:b for a,b in members}

    #Build Gaming Laptop
    gaming_laptop_builder = builders_map["Gaming_Laptop_Builder"]()
    director = Laptop_Director(gaming_laptop_builder)
    gaming_laptop = director.construct_gaming_laptop()
    print(gaming_laptop)

    print("---------------------------------")

    #Building Office Laptop
    office_laptop_builder = builders_map["Office_Laptop_Builder"]()
    director = Laptop_Director(office_laptop_builder)
    office_laptop = director.construct_office_laptop()
    print(office_laptop)