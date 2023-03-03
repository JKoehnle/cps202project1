def userint():

  money = float(input("How much money do you have? ")) #gets amount of money and force conversion to float

  try: 
     money >= 0 #checks the amount of money is greater than 0
  except NoMoneyError:
     print("You have no money!")
    return userint() #recalls the function to correct error

def state():
    proceed = input("Do you wish to buy more from the vending machine enter true or false: ")
