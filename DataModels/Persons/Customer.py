from DataModels.Order import Order
from DataModels.Persons.Person import Person
from typing import List
from DataModels.Product import Product


class Customer(Person):
    def __init__(self, ID: str, full_name: str, phone_number: str, account_balance: float,
                 purchased_list: List[Product], shopping_list: List[Product], order_list: List[Order]):
        super().__init__(ID, full_name, phone_number)
        self._account_balance = account_balance
        self._purchased_list = purchased_list or []
        self._shopping_list = shopping_list or []
        self._order_list = order_list or []

    @property
    def subclass_identifier(self):
        return "Customer"

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, balance):
        self._account_balance = balance

    @property
    def purchased_list(self):
        return self._purchased_list

    @purchased_list.setter
    def purchased_list(self, purchased_list):
        self._purchased_list = purchased_list

    @property
    def shopping_list(self):
        return self._shopping_list

    @shopping_list.setter
    def shopping_list(self, shopping_list):
        self._shopping_list = shopping_list

    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, order_list: List[Order]):
        self._order_list = order_list

    # Extra methods
    def view_list_of_customer_grocery_list(self):
        for product in self._shopping_list:
            print(product)

    def view_list_of_customer_orders(self) -> None:
        for order in self._order_list:
            print(order)

    def view_total_price_of_grocery_list(self) -> None:
        print(f"The total price of the items in your grocery list is: {self.get_total_grocery_price()}")

    def get_total_grocery_price(self) -> float:
        return float(sum(item.get_price() for item in self._shopping_list))

    def clear_shopping_list(self):
        self._shopping_list.clear()

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, Customer):
            return super().__eq__(other) and self._account_balance == other._account_balance
        return False

    def __str__(self):
        person_str = super().__str__()  # Get the string representation from the parent class

        # Convert the shopping list to a string representation
        shopping_list_str = "\n".join(str(product) for product in self._shopping_list)
        purchased_list_str = "\n".join(str(product) for product in self._purchased_list)

        return f"{person_str}\nAccount Balance: {self._account_balance}\n" \
               f"Purchased List: {purchased_list_str} \nShopping List: \n{shopping_list_str}"
