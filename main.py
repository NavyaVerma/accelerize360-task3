import ops
import utils

budget = int(input("Enter Your Budget: "))
choice = 0
GroceryList = []
while True:
    choice = ops.getChoice()
    if choice == 1:
        item, check, budget = utils.addItem(budget)
        if check == 200:
            GroceryList = utils.alreadyPresent(GroceryList, item.price, item.quantity, item.name)
        elif check == 406:
            print("No money left\n")
        elif check == 403:
            print("Over price, item not added\n")
    else:
        utils.printItems(GroceryList)
        utils.endingBudget(budget, GroceryList)
        break
