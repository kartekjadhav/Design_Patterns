import coffees
import decorators
from inspect import isclass, isabstract, getmembers


if __name__ == "__main__":
    CM = getmembers(coffees, lambda c: isclass(c) and not isabstract(c) and issubclass(c, coffees.Coffee))
    DM = getmembers(decorators, lambda d: isclass(d) and not isabstract(d) and issubclass(d, decorators.CoffeeDecorator))
    coffee_members = {key:value for key, value in CM}
    decorator_members = {key:value for key, value in DM}

    # Usage
    print(f"Base Coffees available => {coffee_members.keys()}")
    type = input("Enter the base coffee you want: ").strip()
    coffee = coffee_members[type]()
    print(coffee.cost())
    milkadded = decorator_members["MilkDecorator"](coffee)
    print(milkadded.cost())
    creamadded = decorator_members["CreamDecorator"](milkadded)
    print(creamadded.cost())