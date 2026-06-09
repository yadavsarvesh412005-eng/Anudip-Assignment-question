# 5. Product class and inventory value

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def total_inventory(products):
    total = 0
    for p in products:
        total += p.price * p.quantity
    return total

p1 = Product("Pen", 10, 50)
p2 = Product("Book", 100, 20)

print("Inventory Value:", total_inventory([p1, p2]))