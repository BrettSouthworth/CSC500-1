class ItemToPurchase:
    def __init__(this):
        this.item_name = "none"    
        this.item_price = 0.0
        this.item_quantity = 0
        
    def __init__(this, item_name="none", item_description="none", item_price=0,item_quantity=0):
        this.item_name=item_name
        this.item_description=item_description
        this.item_price=item_price
        this.item_quantity=item_quantity
        
    def print_item_cost(this):
        total_cost = this.item_price * this.item_quantity
        msg = this.item_name + " " + str(this.item_quantity) + " " + "@ $" + str(this.item_price) + " = $" + str(total_cost)
        print(msg)
