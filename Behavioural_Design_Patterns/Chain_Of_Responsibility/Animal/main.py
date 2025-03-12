from Handlers import MonkeyHandler, BearHandler, SquirrelHandler


def eatFood(handler):
    for food in ['Nuts', 'Banana', 'Cup Of Coffee', 'Fish']:
        eater = handler.handle(food) or 'No one'
        if eater:
            print(f'{eater} will have the {food}')
        else:
            print(f'{eater} will have the {food}')
    print()
def main():
    monkey = MonkeyHandler()
    bear = BearHandler()
    squirrel = SquirrelHandler()
    monkey.set_next(bear).set_next(squirrel)

    eatFood(monkey)
    eatFood(bear)
    eatFood(squirrel)

main()