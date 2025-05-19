# Coffee Shop OOP Project

This is a Python object-oriented programming (OOP) project simulating a coffee shop system. It demonstrates object relationships between customers, coffees, and orders while practicing OOP concepts like encapsulation, validation, and class interactions.

---

## Project Structure
coffee-shop/

├── coffee.py

├── customer.py

├── order.py

├── debug.py

├── Pipfile

├── .gitignore

└── tests/

    ├── coffee_test.py

    ├── customer_test.py

    └── order_test.py



---

## Features

### `Customer`
- Name validation (1–15 characters)
- Tracks their own orders
- Can place new orders (`create_order`)
- Can return unique list of coffees ordered
- `most_aficionado(coffee)` class method returns the customer who spent the most on a specific coffee

### `Coffee`
- Name validation (minimum 3 characters)
- Returns all orders for that coffee
- Returns unique list of customers who ordered it
- Computes number of orders and average price

### `Order`
- Connects a customer with a coffee and price
- Validates:
  - `customer` is an instance of `Customer`
  - `coffee` is an instance of `Coffee`
  - `price` is a `float` between 1.0 and 10.0 (inclusive)

---

## Requirements

- Python 3.8+
- [Pipenv](https://pipenv.pypa.io/en/latest/)

To install Pipenv: 
pip3 install pipenv

## Setup

Clone the repo or download the project folder:


git clone https://github.com/BryOk-droid/coffee-shop.git

cd coffee-shop

## Install dependencies using Pipenv:

pipenv install

## Activate the environment:

pipenv shell

### If using venv instead of Pipenv:

source coffee/bin/activate

## Running the Tests
Make sure you're in the virtual environment (pipenv shell or source ...).

### Run all tests

python -m unittest discover -s tests -p "*_test.py"
### Run a specific test file

python tests/customer_test.py

python tests/coffee_test.py

python tests/order_test.py

## License
This project is intended for educational use in a software engineering class and is not licensed for commercial distribution.

## Acknowledgments
Thanks to the course instructor (Mr.Julius and Ms.Stella) and peers for guidance and review.

---

## Author

**Brian Omuga**  
Student Software Engineer  
Python OOP Project - Coffee Shop Challenge 

GitHub: (https://github.com/BryOk-droid)
