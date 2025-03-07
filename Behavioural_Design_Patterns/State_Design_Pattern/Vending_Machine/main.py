from vending_machine import VendingMachine
def main():
    vm = VendingMachine()
    vm.selectItem('Coke')
    vm.insertCoin(100)
    vm.selectItem('Sprite')

main()