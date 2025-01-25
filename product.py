from category import Category

class Product:
    def __init__(self, name, price, stock, category):
        if not isinstance(category, Category):
            raise ValueError("Category must be an instance of the enum Category.")
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"{self.name} | " +  f"{self.category}".capitalize() + f" | €{self.price:.2f} | Stock: {self.stock}"
