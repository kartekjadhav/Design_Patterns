from .state import VendingMachineState

class DespenseState(VendingMachineState):
    def __init__(self, machine):
        super().__init__(machine)

    def on_entry(self): 
        self.despenseItem()
    
    def insertCoin(self, amount):
        print("Can't insert coins while despensing!")

    def cancel(self):
        print("Can't cancel while despensing!")

    def selectItem(self, item):
        print("Can't select item while despensing!")

    def despenseItem(self):
        if self._machine.selected_item:
            print(f"Enjoy your {self._machine.selected_item}")
            self._machine.set_state(self._machine.idle_state)