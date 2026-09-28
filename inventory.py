import json
import os

FILE = "inventory.json"


def load_inventory():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as file:
        return json.load(file)


def save_inventory(inventory):
    with open(FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def add_product():
    inventory = load_inventory()

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    product = {
        "id": len(inventory) + 1,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    inventory.append(product)
    save_inventory(inventory)

    print("Product added successfully.")


def view_inventory():
    inventory = load_inventory()

    if not inventory:
        print("Inventory is empty.")
        return

    print("\nInventory")
    print("-" * 55)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"{product['name']} | "
            f"Qty: {product['quantity']} | "
            f"Price: ₹{product['price']:.2f}"
        )


def search_product():
    inventory = load_inventory()

    keyword = input("Enter product name: ").lower()

    found = False

    for product in inventory:
        if keyword in product["name"].lower():
            print(
                f"ID: {product['id']} | "
                f"{product['name']} | "
                f"Qty: {product['quantity']} | "
                f"Price: ₹{product['price']:.2f}"
            )
            found = True

    if not found:
        print("Product not found.")


def update_stock():
    inventory = load_inventory()

    product_id = int(input("Enter product ID: "))
    new_quantity = int(input("Enter new quantity: "))

    for product in inventory:
        if product["id"] == product_id:
            product["quantity"] = new_quantity
            save_inventory(inventory)

            print("Stock updated successfully.")
            return

    print("Product not found.")


def delete_product():
    inventory = load_inventory()

    product_id = int(input("Enter product ID: "))

    new_inventory = [
        product for product in inventory
        if product["id"] != product_id
    ]

    if len(new_inventory) == len(inventory):
        print("Product not found.")
        return

    for index, product in enumerate(new_inventory, 1):
        product["id"] = index

    save_inventory(new_inventory)

    print("Product deleted successfully.")


def inventory_value():
    inventory = load_inventory()

    total = sum(
        product["quantity"] * product["price"]
        for product in inventory
    )

    print(f"Total inventory value: ₹{total:.2f}")


def main():
    while True:
        print("\n===== INVENTORY STOCK MANAGER =====")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Total Inventory Value")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            inventory_value()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
