from typing import List

from DataModels.Exceptions.ItemNotFoundError import ItemNotFoundError
from DataModels.Exceptions.LowStockError import LowStockError
from DataModels.Persons.Employees.Employee import Employee
from DataModels.Product import Product
from DataModels.Persons.Employees.Organisers.IOrganiser import IOrganiser


class Organiser(Employee, IOrganiser):
    ALLOWED_ITEM_TYPES = [
        "Fruit", "Vegetable", "Canned", "Dairy", "Meat", "Seafood", "Deli",
        "Condiment", "Snack", "Baking", "Beverage", "Starch", "Frozen",
        "Hygiene", "Pharmaceutical", "Household", "Baby-care", "Pet-care",
        "Auto-Repair", "Hardware"
    ]

    def __init__(self, ID: str, full_name: str, phone_number: str,
                 employee_number: str, shift_type: str,
                 responsible_item_types: List[str]):
        super().__init__(ID, full_name, phone_number, employee_number, shift_type)
        self._responsible_item_types = responsible_item_types

    @property
    def responsible_item_types(self) -> List[str]:
        return self._responsible_item_types

    @responsible_item_types.setter
    def responsible_item_types(self, item_types: str):
        for item_type in item_types:
            if item_type not in self.ALLOWED_ITEM_TYPES:
                raise ValueError(f"Invalid item type: {item_type}")
        self._responsible_item_types = item_types

    def fill_shelves_with_low_stock_item(self, barcode: str, shelves: List[Product], storage_room: List[Product]) -> bool:
        """
        Fill the shelves with a low stock item from the storage room.

        Args:
            barcode (str): The barcode of the item to be filled on the shelves.
            shelves (List[Product]): The list of products on the shelves.
            storage_room (List[Product]): The list of products in the storage room.

        Returns:
            bool: True if the item was successfully filled on the shelves, False otherwise.

        Raises:
            ValueError: If no item with the specified barcode is found in low stock on the shelves.

        Note:
            The `low_stock_threshold` and `max_stock_per_shelf` values are assumed to be predefined.

        """
        try:
            low_stock_threshold = 100  # Minimum stock level considered as low stock
            max_stock_per_shelf = 400  # Maximum stock that can be added to a shelf

            # Find the item with the specified barcode in low stock
            low_stock_item = next((item for item in shelves if item.get_barcode() == barcode and item.get_stock() < low_stock_threshold), None)

            if low_stock_item is None:
                raise LowStockError(f"No item with barcode {barcode} found in low stock on the shelves.")

            if low_stock_item.get_item_type() not in self._responsible_item_types:
                print(f"Organiser is not responsible for items of type {low_stock_item.get_item_type()}.")
                return False

            storage_item = next((storage_item for storage_item in storage_room if storage_item.get_barcode() == barcode), None)

            if storage_item is None:
                print(f"No item with barcode {barcode} found in the storage room.")
                return False

            if storage_item.get_stock() == 0:
                print(f"No stock available for item {storage_item.get_name()} in the storage room.")
                return False

            available_space = max_stock_per_shelf - low_stock_item.get_stock()
            stock_to_add = min(storage_item.get_stock(), available_space)
            low_stock_item.set_stock(low_stock_item.get_stock() + stock_to_add)
            storage_item.set_stock(storage_item.get_stock() - stock_to_add)
            print(f"{stock_to_add} units of item {storage_item.get_name()} added to the shelves and removed from storage room.")
            return True
        except LowStockError as e:
            print(f"Low stock error: {str(e)}")
            return False

    def remove_item_from_shelf(self, barcode: str, shelves: List[Product], storage_room: List[Product]) -> bool:
        """
        Remove an item from the shelves and return it to the storage room.

        Args:
            barcode (str): The barcode of the item to be removed from the shelves.
            shelves (List[Product]): The list of products on the shelves.
            storage_room (List[Product]): The list of products in the storage room.

        Returns:
            bool: True if the item was successfully removed from the shelves and returned to the storage room,
             False otherwise.

        Note:
            If the item is not found in the storage room, a new instance of the Product class with the same attributes
             as the item on the shelves will be created and added to the storage room.

        """
        # Find the item on the shelves
        try:
            item_on_shelf = next((item for item in shelves if item.get_barcode() == barcode), None)

            if item_on_shelf is None:
                raise ItemNotFoundError(f"No item with barcode {barcode} found on the shelves.")

            if item_on_shelf.get_item_type() not in self._responsible_item_types:
                print(f"Organizer is not responsible for items of type {item_on_shelf.get_item_type()}.")
                return False

            item_in_storage_room = next((item for item in storage_room if item.get_barcode() == barcode), None)

            if item_in_storage_room is None:
                # Create a new instance of the Product class with the same attributes as item_on_shelf
                new_item_in_storage = Product(
                    item_on_shelf.get_barcode(),
                    item_on_shelf.get_name(),
                    item_on_shelf.get_price(),
                    item_on_shelf.get_item_type(),
                    item_on_shelf.get_stock()
                )
                storage_room.append(new_item_in_storage)
            else:
                item_in_storage_room.set_stock(item_in_storage_room.get_stock() + item_on_shelf.get_stock())

            # Update the stock on the shelf
            item_on_shelf.set_stock(0)
            print(f"Item {item_on_shelf.get_name()} with barcode {barcode} removed from the shelf and returned to storage room.")
            return True
        except ItemNotFoundError as e:
            print(f"Item not found error: {str(e)}")
            return False

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, Organiser):
            return (
                    super().__eq__(other) and
                    self._responsible_item_types == other._responsible_item_types
            )
        return False

    # Overridden __str__ method
    def __str__(self):
        employee_str = super().__str__()  # Get the string representation from the parent class
        return (
            f"{employee_str}\nResponsible Item Types: {self._responsible_item_types}\n"
        )
