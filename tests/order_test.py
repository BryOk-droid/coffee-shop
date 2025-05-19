import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_valid(self):
        c = Customer("Jill")
        coffee = Coffee("Flat White")
        o = Order(c, coffee, 5.5)
        self.assertEqual(o.price, 5.5)
        self.assertEqual(o.customer.name, "Jill")

    def test_price_invalid(self):
        c = Customer("Zoe")
        coffee = Coffee("Macchiato")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(c, coffee, 11.0)

if __name__ == '__main__':
    unittest.main()
