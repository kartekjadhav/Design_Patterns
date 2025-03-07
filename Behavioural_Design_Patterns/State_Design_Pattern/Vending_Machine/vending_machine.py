from item import Item
from States import IdleState, SelectionState, DespenseState

class VendingMachine():
    items = {
        'Coke': Item('Coke', 10, 10),
        'Frooti': Item('Frooti', 20, 9),
        'Pepsi': Item('Pepsi', 15, 7),
        'Mountain Dew': Item('Mountain Dew', 20, 5),
        'Mazaa': Item('Mazaa', 10, 10),
        'Sprite': Item('Sprite', 8, 2)
    }
    def __init__(self):
        self.amount = 0
        self.idle_state = IdleState(self)
        self.selection_state = SelectionState(self)
        self.despense_state = DespenseState(self)
        self.selected_item = None
        self.state = None
        self.set_state(self.idle_state)
    
    def insertCoin(self, amount):
        self.state.insertCoin(amount)
    
    def cancel(self):
        self.state.cancel()
    
    def selectItem(self, item):
        self.state.selectItem(item)

    def despenseItem(self):
        self.state.despenseItem()
    
    def set_state(self, new_state):
        self.state = new_state
        self.state.on_entry()