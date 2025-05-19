import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_name_valid(self):
        c = Customer("Sam")
        self.assertEqual(c.name, "Sam")

    def test_name_invalid(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("x" * 16)

    def test_create_order(self):
        c = Customer("Max")
        coffee = Coffee("Mocha")
        c.create_order(coffee, 4.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertEqual(c.orders()[0].price, 4.5)

    def test_most_aficionado(self):
        coffee = Coffee("Espresso")
        alice = Customer("Alice")
        bob = Customer("Bob")

    
        alice.create_order(coffee, 3.0)
        alice.create_order(coffee, 4.0)

      
        bob.create_order(coffee, 6.0)

        
        self.assertEqual(Customer.most_aficionado(coffee), alice)

    def test_most_aficionado_no_orders(self):
        coffee = Coffee("Flat White")
        self.assertIsNone(Customer.most_aficionado(coffee))  # No orders made

if __name__ == '__main__':
    unittest.main()
