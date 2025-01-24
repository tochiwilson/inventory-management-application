from category import Category
from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, stock, category):
        try:
            category_enum = Category(category)
            self.products.append(Product(name, price, stock, category_enum))
            print(f"Product '{name}' added successfully.")
        except ValueError:
            print(f"Invalid category. Choose from: {[c.value for c in Category]}.")

    def edit_product(self, name):
        for product in self.products:
            if product.name == name:
                product.name = input("Enter new name: ") or product.name
                product.price = float(input("Enter new price: ") or product.price)
                product.stock = int(input("Enter new stock quantity: ") or product.stock)
                try:
                    new_category = input("Enter new category: ")
                    product.category = Category(new_category) if new_category else product.category
                except ValueError:
                    print(f"Invalid category. Keeping the current category: {product.category}.")
                print("Product updated successfully.")
                return
        print("Product not found.")

    def restock_product(self, name, quantity):
        for product in self.products:
            if product.name == name:
                product.stock += quantity
                print(f"Stock updated. New stock for '{name}': {product.stock}")
                return
        print("Product not found.")

    def reduce_stock(self, name, quantity):
        for product in self.products:
            if product.name == name:
                if product.stock >= quantity:
                    product.stock -= quantity
                    print(f"Stock reduced. New stock for '{name}': {product.stock}")
                else:
                    print("Not enough stock.")
                return
        print("Product not found.")

    def generate_low_stock_report(self, threshold):
        print("\nLow Stock Report:")
        for product in self.products:
            if product.stock < threshold:
                print(product)

    def list_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            print("\nCurrent Inventory:")
            for idx, product in enumerate(self.products):
                print(f"{idx + 1}. {product}")
