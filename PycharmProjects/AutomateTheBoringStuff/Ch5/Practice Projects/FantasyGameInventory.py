def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, addeditems):

    for item in addeditems:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1


if __name__ == "__main__":
    #stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold chain', 'dagger', 'gold chain', 'gold coin', 'ruby']
    inv = {'gold coin': 42, 'rope': 1}
    #display_inventory(stuff)
    add_to_inventory(inv, dragonLoot)
    display_inventory(inv)

