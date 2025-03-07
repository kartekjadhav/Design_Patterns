from .state import VendingMachineState

class IdleState(VendingMachineState):
    def __init__(self, machine):
        super().__init__(machine)
        

    def on_entry(self):
        self._machine.selected_item = None
        print('Inventory -> ')
        for key in self._machine.items.keys():
            print(f"{key} : price - {self._machine.items[key].price} : quantity - {self._machine.items[key].quantity}")

    def insertCoin(self, amount):
        self._machine.amount += amount

    def cancel(self):
        if self._machine.amount > 0:
            print(f"Returing back money - {self._machine.amount}")
            self._machine.amount = 0

    def selectItem(self, item):
        if self._machine.amount > 0:
            if item:
                self._machine.selected_item = item
                self._machine.set_state(self._machine.selection_state)
            else:
                print("Enter valid item")
        else:
            print('Please enter some coins before selecting an item')

    def despenseItem(self):
        print("Please select some item before proceeding to despense.")