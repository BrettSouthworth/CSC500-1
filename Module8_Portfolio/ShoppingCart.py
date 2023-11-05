from ItemToPurchase import ItemToPurchase

class ShoppingCart:    
    def __init__(this, customer_name="none", current_date="January 1, 2020"):
        this.customer_name = customer_name
        this.current_date = current_date
        this.cart_items = []

    def add_item(this, item_to_purchase):
        this.cart_items.append(item_to_purchase)

    def remove_item(this, item_name):
        isFound = False
        for item in this.cart_items:
            if item.item_name == item_name:
                this.cart_items.remove(item)
                isFound = True
                break
        if isFound is False:
            print("Item not found in cart. Nothing removed.")
        
    def modify_item(this, item_to_purchase):
        isfound = False
        for item in this.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                isfound = True
                break
        if not isfound:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(this):
        total_quantity = 0
        for item in this.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(this):
        total = 0.0
        for item in this.cart_items:
            total += item.item_price * item.item_quantity
        return total
    
    def print_total(this):  
        totalCost = this.get_cost_of_cart()
        if totalCost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Total cost of shopping cart: " + str(totalCost))
            
    def print_descriptions(this):
        for item in this.cart_items:
            print(str(item.item_name) + ": " + str(item.item_description))
