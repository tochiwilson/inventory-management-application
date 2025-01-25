from inventory import Inventory
from product import Product
from category import Category
import csv


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
        print("7. Bulk Upload via CSV")
        print("8. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                stock = int(input("Enter stock quantity: "))
                print("Choose a category from the following:")
                for c in Category:
                    print(f"- {c.value.capitalize()}")
                category = input("Enter product category: ").lower()
                inventory.add_product(name, price, stock, category)
            case "2":
                name = input("Enter the name of the product to edit: ")
                inventory.edit_product(name)
            case "3":
                name = input("Enter the name of the product to restock: ")
                quantity = int(input("Enter quantity to add: "))
                inventory.restock_product(name, quantity)
            case "4":
                name = input("Enter the name of the product to reduce stock: ")
                quantity = int(input("Enter quantity to reduce: "))
                inventory.reduce_stock(name, quantity)
            case "5":
                threshold = int(input("Enter stock threshold: "))
                inventory.generate_low_stock_report(threshold)
            case "6":
                inventory.list_products()
            case "7":
                file_name = input("Enter the filename (exclude .csv): ")
                read_file(filename=f"{file_name}.csv", inventory=inventory)
            case "8":
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


def read_file(filename, inventory):
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                # Validate the rows
                name = row.get("name")
                price = row.get("price")
                stock = row.get("stock")
                category = row.get("category")

                if not name or not price or not stock or not category:
                    print(f"Skipping row due to missing fields: {row}")
                    continue

                try:
                    price = float(price)
                    stock = int(stock)

                    if price <= 0:
                        print(f"Price must be greater than 0. Skipping")
                        continue

                    if stock <= 0:
                        print(f"Stock must be greater than 0. Skipping")
                        continue

                    if category not in Category._value2member_map_:
                        print(f"Invalid category '{category}' for product '{name}'. Skipping")
                        continue

                    # Add product to Inventory
                    inventory.add_product(name, price, stock, category)
                except ValueError as e:
                    print(f"Error processing row {row}: {e}")
                    continue
            print("Bulk upload complete!")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    main()
