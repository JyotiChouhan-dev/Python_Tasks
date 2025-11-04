from models.Product import Product
from services.InventoryService import InventoryService
from services.StatsService import StatsService


def main():
    # Initialize inventory and stats services
    service = InventoryService()
    stats_service = StatsService(service.get_all_products())

    while True:
        print("\n=== Inventory Menu (with Stats) ===")
        print("1. List all products")
        print("2. Low stock warning")
        print("3. Add product")
        print("4. Update stock")
        print("5. Delete product")
        print("6. Total value of stock")
        print("7. Apply discount")
        print("8. Stats Report (NumPy)")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service.list_products()

        elif choice == "2":
            service.low_stock_warning()

        elif choice == "3":
            name = input("Enter name: ")
            stock = int(input("Enter stock: "))
            price = float(input("Enter price: "))
            location = input("Enter location: ")
            tags = set(input("Enter tags (comma separated): ").split(","))
            new_product = Product(name, stock, price, location, tags)
            service.add_product(new_product)

        elif choice == "4":
            service.update_stock()

        elif choice == "5":
            service.delete_product()

        elif choice == "6":
            service.total_inventory_value()

        elif choice == "7":
            service.apply_discount_by_tag()

        elif choice == "8":
            print("\n=== Statistics Report (NumPy) ===")
            print(f"Average price: ₹{stats_service.average_price():.2f}")

            most_exp = stats_service.most_expensive_item()
            if most_exp:
                print(f"Most expensive item: {most_exp[0]} (₹{most_exp[1]})")

            print(f"Total items in stock: {stats_service.total_stock_count()}")

            print("\nInventory Value by Product:")
            for name, value in stats_service.total_value_per_product().items():
                print(f" - {name}: ₹{value}")

            tag = input("\nEnter tag to filter stats (e.g. 'clearance'): ")
            tag_stats = stats_service.tag_based_stats(tag)
            if tag_stats:
                avg_price, total_value = tag_stats
                print(f"Avg price for '{tag}' items: ₹{avg_price:.2f}")
                print(f"Total value for '{tag}' items: ₹{total_value:.2f}")
            else:
                print(f"No products found with tag '{tag}'.")

        elif choice == "9":
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
