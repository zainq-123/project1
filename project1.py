import random

class Menu:
    def __init__(self):
        self.menu = {
            "tea": 240,
            "coffee": 320,
            "cappuccino": 270,
            "black-coffee": 210
        }
        self.total = 0
        self.products = []

    def order_place(self, order):
        if order in self.menu:
            self.products.append(order)
            self.total += self.menu[order]  
            print(f"{order} added to your order.")
        else:
            print(f"Sorry, {order} is not available in the menu.")

    def after_order(self):
        if not self.products:
            print("No orders placed.")
            return

        cust_id = random.randint(100000, 999999)  #random customer ID
        print(f"Customer ID: {cust_id}")
        print("Your order summary:")
        
        for product in self.products:
            print(f"- {product}: {self.menu[product]} PKR")
        
        print(f"Total bill: {self.total} PKR")

# Example Usage
menu = Menu()
menu.order_place("tea")
menu.order_place("coffee")
menu.order_place("black-coffee") 
menu.order_place("burger") #will add nothing 
menu.after_order()
