from enum import Enum

class Category(Enum):
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    FOOD = "food"
    BOOKS = "books"
    TOYS = "toys"

    def __str__(self):
        return f"{self.value}"
