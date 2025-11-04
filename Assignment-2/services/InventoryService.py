from models.FoodProduct import FoodProduct
from models.Product import Product

LOW_STOCK = 5


class InventoryService:
    def __init__(self):
        # Preloaded products
        self.products = {
            "Apple": Product("Apple", 10, 50, "shelf-1", {"grocery"}),
            "Soap": Product("Soap", 3, 30, "shelf-2", {"clearance"}),
            "Milk": FoodProduct("Milk", 8, 60, "shelf-3", {"grocery"}, "2025-12-10"),
            "Chips": FoodProduct("Chips", 2, 20, "shelf-4", {"clearance", "snacks"}, "2025-11-20"),
            "Rice": Product("Rice", 15, 500, "shelf-5", {"grocery"})
        }

    # ---------- 1. Add new product ----------
    def add_product(self):
        name = input("Enter product name: ")
        if name in self.products:
            print(f"{name} already exists!")
            return

        stock = int(input("Enter stock quantity: "))
        price = float(input("Enter price: "))
        location = input("Enter location: ")
        tags = set(input("Enter tags (comma separated): ").split(","))

        # Ask if it is a FoodProduct (with expiry)
        is_food = input("Is it a FoodProduct (y/n)? ").lower()
        if is_food == "y":
            expiry = input("Enter expiry date (YYYY-MM-DD): ")
            product = FoodProduct(name, stock, price, location, tags, expiry)
        else:
            product = Product(name, stock, price, location, tags)

        self.products[name] = product
        print(f"{name} added successfully!")

    # ---------- 2. List all products ----------
    def list_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("\n--- Product List ---")
            for p in self.products.values():
                print(p.describe())

    # ---------- 3. Low stock warning ----------
    def low_stock_warning(self):
        print("\n--- Low Stock Products ---")
        found = False
        for p in self.products.values():
            if p.stock < LOW_STOCK:
                print(p.describe())
                found = True
        if not found:
            print("All products have sufficient stock.")

    # ---------- 4. Delete product ----------
    def delete_product(self):
        name = input("Enter the product name to delete: ")
        if name in self.products:
            del self.products[name]
            print(f"{name} deleted successfully.")
        else:
            print("Product not found!")

    # ---------- 5. Update stock ----------
    def update_stock(self):
        name = input("Enter product name to update stock: ")
        if name not in self.products:
            print("Product not found!")
            return
        new_stock = int(input("Enter new stock value: "))
        self.products[name].stock = new_stock
        print(f"{name}'s stock updated successfully!")

    # ---------- 6. Total inventory value ----------
    def total_inventory_value(self):
        total = 0
        for p in self.products.values():
            total += p.value()
        print(f"\nTotal Inventory Value = ₹{total}")

    # ---------- 7. Apply discount by tag ----------
    def apply_discount_by_tag(self):
        tag = input("Enter tag to apply discount (e.g., 'clearance'): ")
        print(f"\n--- Discounted Products for tag: {tag} ---")
        found = False
        for p in self.products.values():
            if tag in p.tags:
                discounted_price = p.price * 0.5
                print(f"{p.name}: Old Price = ₹{p.price}, New Price = ₹{discounted_price}")
                found = True
        if not found:
            print("No products found with that tag.")
