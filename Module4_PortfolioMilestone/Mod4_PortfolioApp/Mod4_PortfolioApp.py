from ItemToPurchase import ItemToPurchase

# Size of shopping cart
shoppingCartSize = 2

print("Welcome to Bretts Online Shopping Cart V1.0.\nPlease enter the information requested for " + str(shoppingCartSize) + " items.\n\n")

# Setup shopping cart size
ShoppingCart = []
for i in range(shoppingCartSize):
    ShoppingCart.append(ItemToPurchase())
    i+=1

# Setup vars for later use
index = 0;
totalCost = 0.0

# perform user input
while index < shoppingCartSize:        
    print("Item" + str((index + 1)))
        
    print("Enter the item Name: ")
    ShoppingCart[index].item_name = input()

    print("Enter the item price: ")
    ShoppingCart[index].item_price = float(input())
    
    print("Enter the item quantity: ") 
    ShoppingCart[index].item_quantity = int(input())
        
    totalCost += ShoppingCart[index].item_price * ShoppingCart[index].item_quantity
    index += 1

# Finally print the results
print("TOTAL COST")
for item in ShoppingCart:
    item.print_item_cost()
print("$" + str(totalCost))
