from DataModels.Persons.Employees.Employee import Employee
from typing import List
from DataModels.Persons.Employees.Organisers.Organiser import Organiser
from DataModels.Persons.Employees.Organisers.IOrganiser import IOrganiser
from DataModels.Product import Product


class ShiftManager(Organiser, IOrganiser):
    def __init__(self, ID: str, full_name: str, phone_number: str, employee_number: str,
                 shift_type: str, responsible_employees: List[Employee]):
        super().__init__(ID, full_name, phone_number, employee_number, shift_type, Organiser.ALLOWED_ITEM_TYPES)
        self._responsible_employees = responsible_employees or []

    @property
    def responsible_employees(self):
        return self._responsible_employees

    @responsible_employees.setter
    def responsible_employees(self, employees):
        for employee in employees:
            if not isinstance(employee, Employee):
                raise ValueError("Invalid employee object.")
        self._responsible_employees = employees

    def view_responsible_employees(self) -> None:
        """
        Displays the list of employees under the shift manager's responsibility.
        """
        print(f"List of employees under the shift manager {self.get_full_name()}'s responsibility: ")
        for employee in self._responsible_employees:
            print(employee)

        print("End of list")

    def fill_shelves_with_low_stock_item(self, barcode: str, shelves: List[Product], storage_room: List[Product]):
        """
        Fills the shelves with a low stock item from the storage room.

        Parameters:
        - barcode (str): The barcode of the item to be filled.
        - shelves (List[Product]): The list of products on the shelves.
        - storage_room (List[Product]): The list of products in the storage room.
        """
        low_stock_threshold = 100  # Minimum stock level considered as low stock
        max_stock_per_shelf = 400  # Maximum stock that can be added to a shelf

        # Find the item with the specified barcode in low stock
        low_stock_item = next((item for item in shelves if item.get_barcode() == barcode and item.get_stock() < low_stock_threshold), None)

        if low_stock_item is None:
            print(f"No item with barcode {barcode} found in low stock on the shelves.")
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

    def remove_item_from_shelf(self, barcode: str, shelves: List[Product], storage_room: List[Product]):
        """
        Removes an item from the shelves and returns it to the storage room.

        Parameters:
        - barcode (str): The barcode of the item to be removed.
        - shelves (List[Product]): The list of products on the shelves.
        - storage_room (List[Product]): The list of products in the storage room.
        """
        # Find the item on the shelves
        item_on_shelf = next((item for item in shelves if item.get_barcode() == barcode), None)

        if item_on_shelf is None:
            print(f"No item with barcode {barcode} found on the shelves.")
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

    @staticmethod
    def remove_item_from_storage_room(barcode: str, storage_room: List[Product]):
        """
        Removes an item from the storage room.

        Parameters:
        - barcode (str): The barcode of the item to be removed.
        - storage_room (List[Product]): The list of products in the storage room.
        """
        # Find the item in the storage room
        item_in_storage_room = next((item for item in storage_room if item.get_barcode() == barcode), None)

        if item_in_storage_room is None:
            print(f"No item with barcode {barcode} found in the storage rooms.")
            return False

        # Update the stock on the shelf
        item_in_storage_room.set_stock(0)
        print(f"Item {item_in_storage_room.get_name()} with barcode {barcode} removed from the shelf and returned to storage room.")
        return True

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, ShiftManager):
            return super().__eq__(other) and self._responsible_employees == other._responsible_employees
        return False

    # Overridden __str__ method
    def __str__(self):
        organiser_str = super().__str__()
        employee_ids = [employee.get_ID() for employee in self._responsible_employees]
        return f"{organiser_str}\nResponsible Employees: {employee_ids}"
