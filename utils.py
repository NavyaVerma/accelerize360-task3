class Item:
    def __init__(self, price, quantity, name):
        self.name = name
        self.price = price
        self.quantity = quantity


def printItem(item):
    print(item.name, "\n")


def printItems(GroceryList):
    """
    Print out items in a tabular manner.

    :param GroceryList: List of items
    :return:
    """
    print("Grocery List\n")
    print("name\tprice\tquantity\n\n")
    for i in GroceryList:
        print(i.name, "\t", i.price, "\t", i.quantity, "\n")


def addItem(budget):
    """

    :param budget: int, budget entered by user
    :return: Item, status [200, 406, 403], left budget

    """
    orig_budget = budget
    name = input("Enter Product: ")
    quantity = input("Enter Quantity: ")
    price = int(input("Enter Price: "))
    status, budget = checkBudget(price, budget)
    if status == 200:
        return Item(price, quantity, name), status, budget
    else:
        return Item(price, quantity, name), status, orig_budget


def checkBudget(price, budget):
    amount_left = budget - price
    if amount_left >= 0:
        return 200, amount_left  # StatusOK: If budget is left
    if amount_left == 0 and budget == 0:
        return 406, amount_left  # NotAcceptable: If budget is Zero
    if amount_left < 0:
        return 403, amount_left  # BadRequest: If OverBudget


def getWeight(weightString):
    """

    :param weightString:
    :return: Weight in integer, 0 if Grams and 1 if KiloGrams
    """
    weight_list = weightString.split(' ')
    if weight_list[1] == 'g' or weight_list[1] == 'G':
        return int(weight_list[0]), 0
    else:
        return int(weight_list[0]), 1


def addWeights(w1, w2):
    """

    :param w1 weight 1, type string
    :param w2 weight 2, type string
    :return: sum of w1 and w2, type string in Kg
    """
    w1, type1 = getWeight(w1)
    w2, type2 = getWeight(w2)
    if type1 == type2:
        w3 = w1 + w2
        return str(w3) + " kg"
    else:
        if type1 == 0 and type2 == 1:
            w3 = w1 / 1000 + w2
            return str(w3) + " kg"
        if type1 == 1 and type2 == 0:
            w3 = w1 + w2 / 1000
            return str(w3) + " kg"


def alreadyPresent(GroceryList, price, quantity, name):
    """
    Linear Search and updation

    :param GroceryList: List of Items
    :param price: Integer
    :param quantity: String
    :param name: Name Of Item
    :return: UpdatedList
    """
    found = False
    for i in range(0, len(GroceryList)):
        if GroceryList[i].name == name:
            found = True
            GroceryList[i].price += price
            GroceryList[i].quantity = addWeights(GroceryList[i].quantity, quantity)
            return GroceryList

    # This is running because the item was not found
    GroceryList.append(Item(price, quantity, name))
    return GroceryList


def endingBudget(budget, GroceryList):
    """
    According to budget, prints the items that can be bought

    :param budget: int, budget left
    :param GroceryList: Final List of items
    :return:
    """
    print('Amount left', budget, ', you can buy:')
    for i in range(0, len(GroceryList)):
        if GroceryList[i].price >= budget:
            printItem(GroceryList[i])
