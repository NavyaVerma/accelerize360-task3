# Task 3 - Maintaining Groceries List

**Problem Statement:**

Make a Grocery List for super market shopping with name, price and quantity; if the list already contains an item, then only update the price and quantity it should not append the item name again. Ask user his/her budget initially

and minus the budget after adding a new item in the list. If budgets go zero/0 then no more item could be bought and if some money left and user add item greater than budget left then inform “over price” or any other message. After the list is made any money left in the budget it should show an item within the budget from the list made.

VALIDATION is a must.

Examples:

Enter Your budget : 500

1.Add an item

2.Exit

Enter your choice : 1

Enter product : corn flour

Enter quantity : 1.5 kg

Enter Price : 100

Amount left : 400

1.Add an item

2.Exit

Enter your choice : 1

 

Enter product: wheat

Enter quantity: 2 kg

Enter Price: 100

Amount left: 300

1.Add an item

2.Exit

Enter your choice : 1

Enter product : corn flour

Enter quantity : 2 kg

Enter Price : 250

Amount left : 150

1.Add an item

2.Exit

Enter your choice : 1

Enter product : rice

Enter quantity : 5 kg

Enter Price : 300

Can't Buy the product ###(because budget left is 150)

1.Add an item

2.Exit

Enter your choice : 1

Enter product : xyz

Enter quantity : 1 kg

Enter Price : 50

Amount left: 100

1.Add an item

2.Exit

Enter your choice: 2

Amount left can buy you wheat

GROCERY LIST is:

Product name   Quantity   Price

corn flour  	2 kg    	250

wheat       	2 kg    	100

xyz         	1 kg     	50
