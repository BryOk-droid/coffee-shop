import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        coffee = Coffee("Americano")
        self.assertEqual(coffee.name, "Americano")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("AB")

    def test_average_price(self):
        coffee = Coffee("Cappuccino")
        c = Customer("Jade")
        c.create_order(coffee, 4.0)
        c.create_order(coffee, 6.0)
        self.assertEqual(coffee.average_price(), 5.0)

if __name__ == '__main__':
    unittest.main()
