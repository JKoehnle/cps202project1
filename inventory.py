inventory = {"Snickers" : [3.00, 5], "Cliffbar" : [5.00, 20], "Snapple" : [8.00, 7]}
#Dict Format = {Key : List}; List = [price, numItem]

def printInven():
    print("These are the items avaliable for purchase:")
    for key, value in inventory.items():
        print(f'{key}:   Price ${value[0]}0  Number Left: {value[1]}')

def getPrice(item):
    return inventory(item)[0]

def getNumLeft(item):
    return inventory(item)[1]

def changeNumLeft(item, numBought):
    currInv = inventory(item)[1] 
    if currInv - numBought < 0:
        print("BREAK STOP THIS DOESNT WORK")
    else:
        inventory(item)[1] - numBought