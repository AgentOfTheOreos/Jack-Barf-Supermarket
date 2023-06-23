import pickle
from datetime import datetime
from typing import List

from DataModels.Product import Product


class Order:
    last_assigned_order_code = 0
    LAST_ASSIGNED_ORDER_CODE_FILE = 'ObjectFiles/last_assigned_order_code.pkl'  # File to store last assigned order code

    def __init__(self, status: str, products: List[Product], customer_id: str, customer_name: str,
                 cash_register_number: str, date: datetime = None):
        if date is None:
            self._datetime = datetime.now()
        else:
            self._datetime = date
        try:
            with open(Order.LAST_ASSIGNED_ORDER_CODE_FILE, 'rb') as file:
                self.last_assigned_order_code = pickle.load(file)
        except FileNotFoundError:
            self.last_assigned_order_code = 0

        self._order_code = self.generate_order_code()
        self._status = status
        self._products = products
        self._customer_id = customer_id
        self._customer_name = customer_name
        self._cash_register_number = cash_register_number
        self._total_price = self.calculate_total_price()

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, date_time: datetime):
        self._datetime = date_time

    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        self._order_code = order_code

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status not in ["Completed", "Standing"]:
            raise ValueError("Invalid status.")
        self._status = status

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        self._products = products
        self._total_price = self.calculate_total_price()

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def cash_register_number(self):
        return self._cash_register_number

    @cash_register_number.setter
    def cash_register_number(self, cash_register_number):
        self._cash_register_number = cash_register_number

    @property
    def total_price(self):
        return self._total_price

    def calculate_total_price(self) -> float:
        return float(sum(product.get_price() for product in self._products))

    def generate_order_code(self):
        self.last_assigned_order_code += 1
        self.save_last_assigned_order_code()  # Save the updated last assigned order code
        return self.last_assigned_order_code

    def save_last_assigned_order_code(self):
        with open(Order.LAST_ASSIGNED_ORDER_CODE_FILE, 'wb') as file:
            pickle.dump(self.last_assigned_order_code, file)

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, Order):
            return self._order_code == other._order_code
        return False

    # Overridden __str__ method
    def __str__(self):
        return f"Order Code: {self._order_code}\n" \
               f"Status: {self._status}\n" \
               f"Date and Time: {self._datetime}\n" \
               f"Customer ID: {self._customer_id}\n" \
               f"Customer Name: {self._customer_name}\n" \
               f"Total Price: {self._total_price}\n" \
               f"Products: {', '.join(str(product) for product in self._products)}"
