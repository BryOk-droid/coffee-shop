from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

c1.create_order(coffee1, 3.5)
c1.create_order(coffee2, 4.0)
c2.create_order(coffee1, 5.0)

# Debug outputs
print(f"{c1.name} has ordered: {[c.name for c in c1.coffees()]}")
print(f"{coffee1.name} has {coffee1.num_orders()} orders")
print(f"{coffee1.name} average price: {coffee1.average_price()}")
print(f"Most aficionado of {coffee1.name}: {Customer.most_aficionado(coffee1).name}")
