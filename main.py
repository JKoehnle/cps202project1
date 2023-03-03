import logic
import inventory

def main ():

    #starting message
    print("Welcome to the vending machine!")
    #gets what the user state
    userWants = True
    #start of buisness logic

    while userWants == True:
        money = logic.get_money()
        inventory.canBuy(money) #checks what user can buy 
        inventory.hasBought(money) #returns change and update privately the inventory

    userWants = logic.get_proceed() #checks with user to see if they want to continue using the vending machine




    