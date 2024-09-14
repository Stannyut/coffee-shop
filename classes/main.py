from coffee import Coffee
from customer import Customer
from order import Order

def main():
    cappussino = Coffee("Cappussino")
    latte = Coffee("Cold-Brew")

    stanley = Customer("Stanley")
    Joan = Customer("Joan")

    # Customers placing orders
    stanley.create_order(cappussino, 700.00)
    Joan.create_order(cappussino, 500.00)
    stanley.create_order(latte, 650.00)

    # Test Coffee class methods
    print(f"Orders for {cappussino.name}: {[order.price for order in cappussino.orders()]}")
    print(f"Customers who ordered {latte.name}: {[customer.name for customer in latte.customers()]}")
    print(f"Number of orders for {latte.name}: {latte.num_orders()}")
    print(f"Average price of {latte.name}: {latte.average_price()}")

    # Test Customer class methods
    print(f"{Joan.name} ordered: {[coffee.name for coffee in Joan.coffees()]}")
    print(f"{stanley.name} ordered: {[coffee.name for coffee in stanley.coffees()]}")

if __name__ == "__main__":
    main()
