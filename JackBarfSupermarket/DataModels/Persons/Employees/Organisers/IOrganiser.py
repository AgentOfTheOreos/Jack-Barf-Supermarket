from abc import ABC, abstractmethod
from typing import List

from DataModels.Product import Product


class IOrganiser(ABC):
    @abstractmethod
    def fill_shelves_with_low_stock_item(self, barcode: str, shelves: List[Product], storage_room: List[Product]):
        """
        abstract method signature for organiser objects to fill shelves with low stock items
        , method content can vary depending on objects subclass
        """
        pass

    @abstractmethod
    def remove_item_from_shelf(self, barcode: str, shelves: List[Product], storage_room: List[Product]):
        """
        abstract method signature for organiser objects to remove items from supermarket shelves
        , method content can vary depending on objects subclass
        """
        pass
