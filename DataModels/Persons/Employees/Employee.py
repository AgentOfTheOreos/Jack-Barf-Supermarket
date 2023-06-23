from abc import ABC
from DataModels.Persons.Person import Person


class Employee(Person, ABC):
    def __init__(self, ID: str, full_name: str, phone_number: str, employee_number: str, shift_type: str):
        super().__init__(ID, full_name, phone_number)
        self._employee_number = employee_number
        self._shift_type = shift_type

    @property
    def subclass_identifier(self):
        return "Employee"

    @property
    def employee_number(self):
        return self._employee_number

    @employee_number.setter
    def employee_number(self, employee_number):
        self._employee_number = employee_number

    @property
    def shift_type(self):
        return self._shift_type

    @shift_type.setter
    def shift_type(self, shift_type):
        valid_shifts = ["Morning", "Evening", "Midnight"]
        if shift_type not in valid_shifts:
            raise ValueError("Invalid shift type.")
        self._shift_type = shift_type

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, Employee):
            return super().__eq__(other) and self._employee_number == other._employee_number
        return False

    # Overridden __str__ method
    def __str__(self):
        person_str = super().__str__()  # Get the string representation from the parent class
        return f"{person_str}, Employee Number: {self._employee_number}, Shift Type: {self._shift_type}"
