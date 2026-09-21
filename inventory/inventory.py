class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
       return f"{self.name} {self.price}"    
           

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)    

    def total(self):
        for all_items in self.items:
            total = all_items + self.price 
            return total  


item1 = Product("Bread", 5)
item2 = Product("Milk", 3)

cart = Cart()
cart.add_item(item1)
cart.add_item(item2)

print(cart.items)