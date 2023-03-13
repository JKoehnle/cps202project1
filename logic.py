def get_money():
  money = float(input("How much money do you have? "))
  while money <= 0:
     print("You can't use the vending machine without money.")
     money = float(input("Please re-enter the amount of money you have: "))
     print()
  return money

def get_proceed():
    proceed = input("Do you wish to buy more from the vending machine? (Enter 'true' or 'false'): ")
    if (proceed == 'true'):
       print()
       return True
    elif (proceed == 'false'):
       print()
       return False
    else:
       print("You did not enter a valid option")
       return get_proceed()

def itemSelection(items_can_buy):
  item_number = int(input("Enter the number of the item you want to buy: ")) - 1
  while (item_number < 0 or item_number >= len(items_can_buy)):
    print("You did not enter the correct number.")
    item_number = int(input("Please try again: ")) - 1
  print()
  item = items_can_buy[item_number]
  return item

def quantSelection(curr_inventory, price, money):
  num_item = int(input("How many do you want to buy? : "))
  updated_inventory = curr_inventory - num_item
  while updated_inventory  < 0 :
      print("You cannot buy that many. There are only", curr_inventory, "left." )
      num_item = int(input("How many do you want to buy? : "))
      updated_inventory = curr_inventory - num_item
  total_cost = num_item * price
  while total_cost > money :
    print(f'You do not have enough money to buy that many. The total cost is ${total_cost}0.')
    num_item = int(input("How many do you want to buy? : "))
    total_cost = num_item * price
  print()
  return num_item

def summary(item, quant, money, total_price):
  if quant == 1:
    print(f'You have bought a {item} for ${total_price}0.')
  else:
    print(f'You have bought {quant} {item}s for a total of ${total_price}0.')
  print(f'You inserted ${money}0. Your change is ${money - total_price}0')