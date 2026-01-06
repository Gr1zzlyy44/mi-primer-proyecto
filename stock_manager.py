# stock_manager.py
# Simple stock management CLI (console app)
# Author: Matias Neira

def add_product(stock: dict, name: str, quantity: int) -> None:
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return
    stock[name] = stock.get(name, 0) + quantity
    print(f"Added {quantity} units of '{name}'.")

def remove_product(stock: dict, name: str, quantity: int) -> None:
    if name not in stock:
        print("That product does not exist.")
        return
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return
    if stock[name] < quantity:
        print(f"Not enough stock. Current: {stock[name]}")
        return

    stock[name] -= quantity
    print(f"Removed {quantity} units of '{name}'.")

    if stock[name] == 0:
        del stock[name]
        print(f"'{name}' is now out of stock and was removed from the list.")

def show_stock(stock: dict) -> None:
    if not stock:
        print("Stock is empty.")
        return

    print("\nCurrent stock:")
    for product, quantity in sorted(stock.items()):
        print(f"- {product}: {quantity}")
    print("")

def menu() -> None:
    print("=== Stock Manager ===")
    print("1) Add product")
    print("2) Remove product")
    print("3) Show stock")
    print("4) Exit")

def ask_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")

def main() -> None:
    stock = {}

    while True:
        menu()
        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            name = input("Product name: ").strip()
            qty = ask_int("Quantity to add: ")
            add_product(stock, name, qty)

        elif option == "2":
            name = input("Product name: ").strip()
            qty = ask_int("Quantity to remove: ")
            remove_product(stock, name, qty)

        elif option == "3":
            show_stock(stock)

        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
