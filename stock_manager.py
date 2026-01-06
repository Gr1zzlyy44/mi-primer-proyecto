# stock_manager.py
# Simple stock management script
# Author: Matias Neira

def add_product(stock, name, quantity):
    stock[name] = stock.get(name, 0) + quantity

def show_stock(stock):
    print("Current stock:")
    for product, quantity in stock.items():
        print(f"- {product}: {quantity}")

def main():
    stock = {}

    add_product(stock, "Keyboard", 10)
    add_product(stock, "Mouse", 15)
    add_product(stock, "Monitor", 5)

    show_stock(stock)

if __name__ == "__main__":
    main()
