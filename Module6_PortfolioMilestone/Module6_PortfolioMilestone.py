from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart


def print_menu(myShoppingCart):
    # print message screen
    print("")
    print("")
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")    

def main():
    shoppingCart = ShoppingCart()
    print_menu(shoppingCart)
    
    # Get user input
    userInput = input("Choose an option:")

  # Perform user input validation
    while userInput != 'q':
        if userInput == "a":
            name = input("Enter the name of the item: ")
            description = input("Enter the description of the item: ")
            price = float(input("Enter the price of the item: "))
            quantity = int(input("Enter the quantity of the item: "))
            item = ItemToPurchase(name, description, price, quantity)
            shoppingCart.add_item(item)
        elif userInput == "r":
            name = input("Enter the name of the item to be removed:")
            shoppingCart.remove_item(name)
        elif userInput == "c":
            name = input("Enter the name of the item you wish to change the quantity of: ")
            quantity = int(input("Enter a new quantity: "))
            item = ItemToPurchase(name, "none", 0, quantity)
            shoppingCart.modify_item(item)            
        elif userInput == "i":
            shoppingCart.print_descriptions()
        elif userInput == "o":
            shoppingCart.print_descriptions()
            shoppingCart.print_total()
        
        else:
            print("Invalid input detected. Please try again.")        
        print_menu(shoppingCart)
        userInput = input("Choose an option:")
    
    print("User has shut down the shopping cart program. Now exiting...")


if __name__ == "__main__":
    main()