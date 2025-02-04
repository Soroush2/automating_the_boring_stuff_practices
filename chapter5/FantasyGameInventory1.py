def displayInventory(inventory):
    total = 0
    for key,val in inventory.items():
        print(key+': '+str(val))
        total+=val
    print(f'Total items : {str(total)}')
def addToInventory(inventory, addedItems):
    newItems={}
    for i in addedItems:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)
displayInventory(inv)