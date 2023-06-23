from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, ID: str, full_name: str, phone_number: str):
        self._ID = ID
        self._full_name = full_name
        self._phone_number = phone_number

    @property
    @abstractmethod
    def subclass_identifier(self):
        pass

    # Getters
    def get_ID(self):
        return self._ID

    def get_full_name(self):
        return self._full_name

    def get_phone_number(self):
        return self._phone_number

    # Setters
    def set_ID(self, ID):
        self._ID = ID

    def set_full_name(self, full_name):
        self._full_name = full_name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, Person):
            return self._ID == other._ID
        return False

    # Overridden __str__ method
    def __str__(self):
        return f"ID: {self._ID}, \nFull Name: {self._full_name}, \nPhone Number: {self._phone_number}\n"
