import logic
import inventory

def main ():

    #starting message
    print("Welcome to the vending machine!")
    #gets what the user state
    userWants = True
    #start of buisness logic
    while userWants = True:
        money = logic.get_money()

        if money > 0:
            inventory()
        elif money == 0:
            print("Please enter more money than 0")
            main()
        else:
            print("Please enter a valid input")
            main()
        
    userWants = logic.get_proceed()



    