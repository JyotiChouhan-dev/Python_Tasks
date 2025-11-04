class Product:
    def __init__(self, name, stock, price, location, tags=None):
        self.name = name
        self.stock = stock
        self.price = price
        self.location = location
        self.tags = tags

    def display(self):
        print(f"Name: {self.name}, Stock: {self.stock}, Price: {self.price}, Location: {self.location}, Tags: {self.tags}")

LOW_STOCK = 5

# List all products
def list_products():
    if not products:
        print("No products found.")
    else:
        print("\n--- Product List ---")
        for p in products.values():
            p.display()

# Show low stock warnings
def low_stock_warning():
    print("\n--- Low Stock Products ---")
    found = False
    for p in products.values():
        if p.stock < LOW_STOCK:
            p.display()
            found = True
    if not found:
        print("No low stock products!")

# Add product
def add_product():
    name = input("Enter product name: ")
    if name in products:
        print("Product already exists!")
        return
    stock = int(input("Enter stock: "))
    price = float(input("Enter price: "))
    location = input("Enter location: ")
    tags = set(input("Enter tags (comma separated): ").split(","))
    products[name] = Product(name, stock, price, location, tags)
    print("Product added successfully!")

# Update stock
def update_stock():
    name = input("Enter product name to update: ")
    if name not in products:
        print("Product not found!")
        return
    new_stock = int(input("Enter new stock value: "))
    products[name].stock = new_stock
    print("Stock updated successfully!")

# Delete product
def delete_product():
    name = input("Enter product name to delete: ")
    if name in products:
        del products[name]
        print("Product deleted!")
    else:
        print("Product not found!")

# Print total value of all products
def total_inventory_value():
    total = 0
    for p in products.values():
        total += p.stock * p.price
    print(f"Total inventory value = {total}")

# Apply discount by tag
def apply_discount():
    print("\n--- Discounted Products (50% off for 'clearance') ---")
    for p in products.values():
        if "clearance" in p.tags:
            discounted_price = p.price * 0.5
            print(f"{p.name}: Old Price = {p.price}, New Price = {discounted_price}")

products = {
    "Apple": Product("Apple", 10, 50, "shelf-1", {"grocery"}),
    "Soap": Product("Soap", 3, 30, "shelf-2", {"clearance"}),
    "Milk": Product("Milk", 8, 60, "shelf-3", {"grocery"}),
    "Chips": Product("Chips", 2, 20, "shelf-4", {"clearance", "snacks"}),
    "Rice": Product("Rice", 15, 500, "shelf-5", {"grocery"})
}

while True:
    print("\n========= INVENTORY MENU =========")
    print("1. List all products")
    print("2. Low stock warnings")
    print("3. Add product")
    print("4. Update stock")
    print("5. Delete product")
    print("6. Print total inventory value")
    print("7. Apply discount by tag")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        list_products()
    elif choice == '2':
        low_stock_warning()
    elif choice == '3':
        add_product()
    elif choice == '4':
        update_stock()
    elif choice == '5':
        delete_product()
    elif choice == '6':
        total_inventory_value()
    elif choice == '7':
        apply_discount()
    elif choice == '8':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")