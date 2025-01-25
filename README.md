# Inventory Management Application  
A Python application to manage inventory efficiently. Add, edit, restock, and track products with built-in bulk upload functionality for easier management.

## Features  
- Add, edit, and delete products  
- Restock and reduce stock levels  
- Generate low stock reports based on user-defined thresholds  
- Bulk upload products via CSV  
- Data validation to ensure all entries are correct (e.g., no negative stock or invalid categories)

## Requirements  
- Python 3.x  

## How to Run  
1. Clone or download this repository.  
2. Make sure you have Python 3.x installed.  
3. Run the application by executing:  
```bash  
python main.py  
```

## How It Works  
1. On startup, the application initializes an inventory management system.  
2. You can perform the following actions:  
   - **Add Products**: Enter product details including name, price, stock, and category.  
   - **Edit Products**: Modify the details of existing products.  
   - **Delete Products**: Remove a product from the inventory by specifying its name.  
   - **Restock or Reduce Stock**: Adjust inventory levels for individual products.  
   - **Generate Low Stock Reports**: Set a stock threshold to identify products that need restocking.  
   - **Bulk Upload Products**: Upload a CSV file with product data (name, price, stock, category) to add or update multiple products at once.  
3. All actions are validated to ensure data integrity (e.g., price must be greater than zero, stock cannot be negative).  

## File Structure  
```plaintext  
project-folder/  
├── main.py          # Main application logic  
├── inventory.py     # Inventory class definition  
├── product.py       # Product class definition  
├── category.py      # Category enum  
```

## CSV Bulk Upload  

The CSV bulk upload feature allows users to quickly add or update products. The uploaded file must follow this format:  
```plaintext  
name    price    stock    category  
Laptop  999.99   10       electronics  
T-Shirt 19.99    50       clothing  
Apple  0.99     100      food  
```

### Valid Categories:
- Electronics
- Clothing
- Food
- Books
- Toys

If the file contains invalid data (e.g., missing fields, invalid categories, or negative values), those rows will be skipped, and an error message will be displayed.

## Future Enhancements / Challenges  

Here are some ideas to extend the functionality of this project:

1. **Sort Products:**  
   Add a feature to sort products by price, stock, or category.

2. **Import/Export Products:**  
   Implement functionality to import/export product data in formats like JSON or XML.

3. **Advanced Validation:**  
   Enhance validation rules, such as ensuring categories match predefined options or enforcing proper price/stock formats.

4. **GUI Interface:**  
   Develop a graphical user interface using libraries like `Tkinter`, `PyQt`, or `Kivy`.

5. **Notifications:**  
   Implement alerts for low-stock products or critical updates.

6. **Cloud Storage Integration:**  
   Sync inventory data with cloud storage platforms like Google Drive or AWS.

7. **Detailed Reporting:**  
   Add analytics for inventory trends, sales forecasting, and stock turnover rates.

8. **REST API:**  
   Develop a REST API to allow external applications to interact with the inventory system.
