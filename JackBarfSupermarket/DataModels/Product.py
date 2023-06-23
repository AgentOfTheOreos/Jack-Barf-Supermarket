class Product:
    ALLOWED_ITEM_TYPES = [
        "Fruit", "Vegetable", "Canned", "Dairy", "Meat", "Seafood", "Deli",
        "Condiment", "Snack", "Baking", "Beverage", "Starch", "Frozen",
        "Hygiene", "Pharmaceutical", "Household", "Baby-care", "Pet-care",
        "Auto-repair", "Hardware"
    ]

    def __init__(self, barcode: str, name: str, price: float, item_type: str, stock: int):
        self._barcode = barcode
        self._name = name
        self._price = price
        self._item_type = None  # Initialize to None
        self.set_item_type(item_type)  # Use setter method to enforce validation
        self._stock = stock

    # Getters
    def get_barcode(self):
        return self._barcode

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_item_type(self):
        return self._item_type

    def get_stock(self):
        return self._stock

    # Setters
    def set_barcode(self, barcode):
        self._barcode = barcode

    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_item_type(self, item_type):
        if item_type not in self.ALLOWED_ITEM_TYPES:
            raise ValueError("Invalid item type.")
        self._item_type = item_type

    def set_stock(self, stock):
        self._stock = stock

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, Product):
            return (
                self._barcode == other._barcode
                and self._name == other._name
                and self._price == other._price
                and self._item_type == other._item_type
                and self._stock == other._stock
            )
        return False

    # Overridden __str__ method
    def __str__(self):
        return f"Barcode: {self._barcode}, \nName: {self._name}, \nPrice: {self._price}, \n" \
               f"Type: {self._item_type}, \nStock: {self._stock}\n"
