from inventory import Inventory
from product import Product
from category import Category

# Inventory Management Application

# Description:
# Develop a tool for inventory management.
# You can add products with details such as name, price, stock quantity, and category.
# Add features to edit products, restock or reduce inventory, and generate reports for products with low stock.

# Challenge:
# Implement bulk actions via a CSV file.
# Add a feature that allows users to upload a CSV file to add or update multiple products at once.
# This requires working with the CSV module and implementing validation to catch incorrect data.


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Restock Product")
        print("4. Reduce Stock")
        print("5. Generate Low Stock Report")
        print("6. List Products")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter stock quantity: "))
            print("Choose a category from the following:")
            for c in Category:
                print(f"- {c.value.capitalize()}")
            category = input("Enter product category: ").lower()
            inventory.add_product(name, price, stock, category)
        elif choice == "2":
            name = input("Enter the name of the product to edit: ")
            inventory.edit_product(name)
        elif choice == "3":
            name = input("Enter the name of the product to restock: ")
            quantity = int(input("Enter quantity to add: "))
            inventory.restock_product(name, quantity)
        elif choice == "4":
            name = input("Enter the name of the product to reduce stock: ")
            quantity = int(input("Enter quantity to reduce: "))
            inventory.reduce_stock(name, quantity)
        elif choice == "5":
            threshold = int(input("Enter stock threshold: "))
            inventory.generate_low_stock_report(threshold)
        elif choice == "6":
            inventory.list_products()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
