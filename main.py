import logic
import inventory

def main ():

    inventory.printInven()
    #starting message
    print("Welcome to the vending machine!")
    print()
    #gets what the user state
    buyMore = True
    #start of buisness logic

    while buyMore:
        money = logic.get_money()
        items_can_buy = inventory.canBuy(money) #checks what user can buy and returns all options as a list
        if len(items_can_buy) == 0:
            print(f'Change of ${money}0 has been returned.')
            print("Please come back when you have more money.")
            break #If they don't have money, there's nothing more to be done

        item_to_buy = logic.itemSelection(items_can_buy)#asks the user which item they want to buy out of the itemes they van afford

        curr_inventory = inventory.inventory[item_to_buy][1]
        price = inventory.inventory[item_to_buy][0]
        num_to_buy = logic.quantSelection(curr_inventory, price, money) #asks the user how many of the item they want to buy

        total_price = num_to_buy * price #determines the total price of the transaction
        change =- money- total_price #determines the change the user should get

        inventory.inventory[item_to_buy][1] = curr_inventory - num_to_buy #updates inventory

        logic.summary(item_to_buy, num_to_buy, money, total_price) #outputs the name and how many of the item(s) were bought, as well as the total money inserted and change due
    
        buyMore = logic.get_proceed() #checks with user to see if they want to continue using the vending machine


main()


    