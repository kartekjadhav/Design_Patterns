from .state import VendingMachineState

class SelectionState(VendingMachineState):
    def __init__(self, machine):
        super().__init__(machine)
    
    def on_entry(self):
        self.selectItem(self._machine.selected_item)

    def insertCoin(self, amount):
        self._machine += amount

    def cancel(self):
        if self._machine.amount > 0:
            print(f"Returing back money - {self._machine.amount}")
            self._machine.amount = 0

    def selectItem(self, item):
        if item in self._machine.items:
            if self._machine.items[item].quantity > 0:
                item_price = self._machine.items[item].price
                curr_amount = self._machine.amount
                if item_price <= curr_amount:
                    self._machine.selected_items = item
                    change = curr_amount - item_price
                    print(f"Here is   you change of {change} rupees, proceeding to despense!")
                    self._machine.amount = item_price
                    self._machine.items[item].quantity -= 1
                    self.despenseItem()
                else:
                    print(f'Please enter {item_price - curr_amount} rupees more, and select your item')
            else:
                print(f"Sorry, {item} is currently sold out!")
        else:
            print(f"Sorry, {item} is currently not available")

    def despenseItem(self):
        if self._machine.selected_item:
            self._machine.set_state(self._machine.despense_state)
        else:
            print("Select an items before proceeding to despense.")