inventory = {"Snickers Bar" : [3.00, 5], "Cliffbar" : [5.00, 20], "Snapple" : [8.00, 7]}
#Dict Format = {Key : List}; List = [price, numItem]

def printInven():
    print("These are the items avaliable for purchase:")
    for key, value in inventory.items():
        print(f'{key}:   Price ${value[0]}0  Number Left: {value[1]}')

def getPrice(item):
    return inventory[item][0]

def getNumLeft(item):
    return inventory[item][1]

def getItem(itemNumber):
    return inventory.keys[itemNumber - 1]

def canBuy(money):
    items_can_buy = []
    for key, value in inventory.items():
         if value[0] <= money:
              items_can_buy.append(key)
    if len(items_can_buy) == 0:
         print("You cannot afford anything")
    else:
        print("You can buy:")
        for item in items_can_buy:
            print(f'{items_can_buy.index(item) + 1}: {item} - Price ${inventory[item][0]}0  Number Left: {inventory[item][1]}')
    return items_can_buy
