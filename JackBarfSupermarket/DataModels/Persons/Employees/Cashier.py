from typing import List

from DataModels.Order import Order
from DataModels.Persons.Employees.Employee import Employee


class Cashier(Employee):
    def __init__(self, ID: str, full_name: str, phone_number: str, employee_number: str, shift_type: str,
                 cash_register_number: str, total_transactions: int, orders: List[Order]):
        super().__init__(ID, full_name, phone_number, employee_number, shift_type)
        self._cash_register_number = cash_register_number
        self._total_transactions = total_transactions
        self._orders = orders or []

    @property
    def subclass_identifier(self):
        return "Cashier"

    # Getters
    def get_cash_register_number(self):
        return self._cash_register_number

    def get_total_transactions(self):
        return self._total_transactions

    def get_orders(self):
        return self._orders

    # Setters
    def set_cash_register_number(self, cash_register_number):
        self._cash_register_number = cash_register_number

    def set_total_transactions(self, total_transactions):
        self._total_transactions = total_transactions

    def set_orders(self, orders):
        self._orders = orders

    def view_list_of_cashier_orders(self) -> None:
        for order in self._orders:
            print(order)

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, Cashier):
            return super().__eq__(other) and self._cash_register_number == other._cash_register_number
        return False

    # Overridden __str__ method
    def __str__(self):
        employee_str = super().__str__()  # Get the string representation from the parent class
        return f"{employee_str}, Cash Register Number: {self._cash_register_number}, " \
               f"Total Transactions: {self._total_transactions}"
