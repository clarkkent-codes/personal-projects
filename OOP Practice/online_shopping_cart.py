class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Successfully added to cart.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print("Successfully removed to cart.")
    
    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        print(f"Total Price: {total}")
    
    def show_cart(self):
        print("Shopping Cart")
        for product in self.products:
            print(f"{product.name} - {product.price}")

products = [
    ("Laptop", 50000),
    ("Mouse", 1000),
    ("Keyboard", 1500),
    ("Headset", 2000)
]

cart = ShoppingCart()

for name, price in products:
    product = Product(name, price)
    cart.add_product(product)

cart.show_cart()

cart.total_price()

cart.remove_product('Mouse')