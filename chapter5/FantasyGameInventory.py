inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    total = 0
    for key,val in inventory.items():
        print(key+': '+str(val))
        total+=val
    print(f'Total items : {str(total)}')
displayInventory(inventory)