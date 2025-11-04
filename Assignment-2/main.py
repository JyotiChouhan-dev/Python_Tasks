from services.InventoryService import InventoryService


def main():
    inventory = InventoryService()

    # inventory.add_product(Product("Soap", 10, 30, "Shelf-1", {"grocery"}))
    # inventory.add_product(Product("Rice", 20, 50, "Shelf-2", {"grocery"}))
    # inventory.add_product(Product("Chips", 5, 20, "Shelf-3", {"snacks"}))
    # inventory.add_product(FoodProduct("Milk", 8, 40, "Shelf-4", {"grocery"}, "2025-11-15"))
    # inventory.add_product(FoodProduct("Yogurt", 6, 25, "Shelf-5", {"dairy"}, "2025-12-05"))

    while True:
        print("\n========= INVENTORY MENU =========")
        print("1. List all products")
        print("2. Low stock warnings")
        print("3. Add new product")
        print("4. Delete product")
        print("5. Show total inventory value")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            inventory.list_products()
        elif choice == '2':
            inventory.low_stock_warning()
        elif choice == '3':
            inventory.add_product()
        elif choice == '4':
            inventory.delete_product()
        elif choice == '5':
            inventory.total_inventory_value()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()