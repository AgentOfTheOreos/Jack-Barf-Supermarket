from datetime import datetime
from typing import List, Any, Union

from DataModels.Order import Order
from DataModels.Persons.Customer import Customer
from DataModels.Persons.Employees.Cashier import Cashier
from DataModels.Persons.Employees.Employee import Employee
from DataModels.Persons.Employees.Organisers.Organiser import Organiser
from DataModels.Product import Product


class Supermarket:
    def __init__(self):
        self._storage_room = []
        self._shelves = []
        self._customers = []
        self._employees = []

    # Storage Room
    @property
    def storage_room(self):
        return self._storage_room

    @storage_room.setter
    def storage_room(self, products: List[Product]):
        self._storage_room = products

    # Shelves
    @property
    def shelves(self):
        return self._shelves

    @shelves.setter
    def shelves(self, products: List[Product]):
        self._shelves = products

    # Customers
    @property
    def customers(self):
        return self._customers

    @customers.setter
    def customers(self, customers: List[Customer]):
        self._customers = customers

    # Employees
    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, employees: List[Employee]):
        self._employees = employees

    # ========================================== Functionality for the system ==========================================
    # ------------------------------------------------------------------------------------------------------------------
    def add_customer(self, customer: Customer) -> bool:
        """
        Adds a customer to the system.

        Parameters:
        - customer (Customer): The customer to be added.

        Returns:
        - bool: True if the customer is added successfully, False if the customer already exists in the system.
        """
        for existing_customer in self._customers:
            if existing_customer.get_ID() == customer.get_ID() or\
                    existing_customer.get_phone_number() == customer.get_phone_number():
                print("Customer already exists in the system, please consider logging in.")
                return False
        self._customers.append(customer)
        print(f"Customer {customer.get_full_name()} with ID {customer.get_ID()} added to the system successfully.")
        return True

    def create_purchase_order(self, customer: Customer, cash_register_number: str, shift: str) -> bool:
        """
        Creates a purchase order for a customer.

        Parameters:
        - customer (Customer): The customer for whom the purchase order is created.
        - cash_register_number (str): The cash register number where the order will be processed.
        - shift (str): The shift during which the order is being created.

        Returns:
        - bool: True if the purchase order is created successfully, False otherwise.
        """
        if customer.get_total_grocery_price() > customer.account_balance:
            print("Insufficient account balance to create order.")
            return False

        # Find the cashier with the specified cash_register_number
        cashier = None
        for employee in self._employees:
            if employee.subclass_identifier == "Cashier" and employee.get_cash_register_number() == cash_register_number\
                    and employee.shift_type == shift:
                cashier = employee
                break

        if not cashier:
            print("Cashier not found.")
            return False

        # Check if the cashier has more than 50 orders
        if len(cashier.get_orders()) > 50:
            print("Cashier has reached the maximum number of orders.")
            return False

        # Create the order and add it to the list of orders
        order = Order("Standing", customer.shopping_list.copy(),
                      customer.get_ID(), customer.get_full_name(), cash_register_number)
        cashier.get_orders().append(order)
        customer.order_list.append(order)
        customer.clear_shopping_list()  # Clear the shopping list after creating the order
        print("Order created successfully, please wait for the cashier to process your purchase.")
        return True

    def purchase_confirmation(self, cashier: Cashier, order_number: int) -> bool:
        """
        Confirms a purchase order.

        Parameters:
        - cashier (Cashier): The cashier who confirms the purchase.
        - order_number (int): The number of the order to be confirmed.

        Returns:
        - bool: True if the purchase order is confirmed successfully, False otherwise.
        """
        order = None
        customer = None
        for cust in self._customers:
            for customer_order in cust.order_list:
                if customer_order.order_code == order_number:
                    order = customer_order
                    customer = cust
                    break

        if not order:
            print(f"Order with number {order_number} not found.")
            return False

        if order.status != "Standing":
            print("Only standing orders can be confirmed.")
            return False

        if order.total_price > customer.account_balance:
            print("Customer does not have enough balance to confirm the order.")
            return False

        # Confirm the purchase
        customer.account_balance -= order.total_price
        customer.purchased_items.extend(order.products)
        cashier.set_total_transactions(cashier.get_total_transactions() + 1)
        order.status = "Completed"
        print("Purchase confirmed successfully.")
        return True

    def get_shelf_items_organiser(self, logistics_worker: Organiser) -> List[Product] or None:
        """
        Retrieves the items on the shelves that are organized by a logistics worker.

        Parameters:
        - logistics_worker (Organiser): The logistics worker responsible for organizing the items.

        Returns:
        - List[Product] or None: The list of items on the shelves organized by the logistics worker,
          or None if no matching items are found.
        """
        responsible_types = logistics_worker.responsible_item_types

        matching_items = []

        for item in self._shelves:
            if item.item_type in responsible_types:
                matching_items.append(item)

        if not matching_items:
            return None
        else:
            return matching_items

    def cancel_purchase_order(self, customer: Customer, order_code: int) -> bool:
        """
        Cancels a purchase order for a customer.

        Parameters:
        - customer (Customer): The customer who placed the order.
        - order_code (int): The code of the order to be canceled.

        Returns:
        - bool: True if the purchase order is canceled successfully, False otherwise.
        """
        order = None
        for an_order in customer.order_list:
            if an_order.order_code == order_code:
                order = an_order
                break
        if not order:
            print("Order not found.")
            return False

        cashier = None
        for employee in self._employees:
            if isinstance(employee, Cashier) and employee.get_cash_register_number == order.cash_register_number:
                cashier = employee
                break
        if not cashier:
            print("Cashier register specified in order not found.")
            return False

        if order not in cashier.get_orders():
            print("Order not found in cashier's list.")
            return False

        customer.order_list.remove(order)
        cashier.get_orders().remove(order)
        print("Order canceled successfully.")
        return True

    def search_query_items_on_shelves(self, category: str, query: str) -> List[Product] or None:
        """
        Searches for items on the shelves based on a category and query.

        Parameters:
        - category (str): The category to search within ('name', 'barcode', 'price', 'type').
        - query (str): The query string to match within the specified category.

        Returns:
        - List[Product] or None: The list of items on the shelves that match the search query,
          or None if no matching items are found.
        """
        filtered_items = []
        for item in self._shelves:
            if category.lower() == 'name' and query.lower() in item.get_name().lower():
                filtered_items.append(item)
            elif category.lower() == 'barcode' and query.lower() in item.get_barcode().lower():
                filtered_items.append(item)
            elif category.lower() == 'price':
                try:
                    query_price = float(query)
                    if query_price == item.get_price():
                        filtered_items.append(item)
                except ValueError:
                    return None
            elif category.lower() == 'type' and query.lower() in item.get_item_type().lower():
                filtered_items.append(item)

        if not filtered_items:
            return None

        return filtered_items

    def search_query_items_in_storage_room(self, category: str, query: str) -> List[Product] or None:
        """
        Searches for items in the storage room based on a category and query.

        Parameters:
        - category (str): The category to search within ('name', 'barcode', 'price', 'type').
        - query (str): The query string to match within the specified category.

        Returns:
        - List[Product] or None: The list of items in the storage room that match the search query,
          or None if no matching items are found.
        """
        filtered_items = []
        for item in self._storage_room:
            if category.lower() == 'name' and query.lower() in item.get_name().lower():
                filtered_items.append(item)
            elif category.lower() == 'barcode' and query.lower() in item.get_barcode().lower():
                filtered_items.append(item)
            elif category.lower() == 'price':
                try:
                    query_price = float(query)
                    if query_price == item.get_price():
                        filtered_items.append(item)
                except ValueError:
                    print("Invalid query for price category, must be numerical!")
                    return filtered_items
            elif category.lower() == 'type' and query.lower() in item.get_item_type().lower():
                filtered_items.append(item)
        return filtered_items

    def get_items_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """
        Retrieves items on the shelves within a specified price range.

        Parameters:
        - min_price (float): The minimum price of the items.
        - max_price (float): The maximum price of the items.

        Returns:
        - List[Product]: The list of items on the shelves that fall within the specified price range.
        """
        filtered_items = []
        for item in self._shelves:
            price = item.get_price()
            if min_price <= price <= max_price:
                filtered_items.append(item)
        return filtered_items

    def add_items_to_purchase(self, barcode: str, customer: Customer) -> bool:
        """
        Adds an item to a customer's shopping list and reduces the stock on the shelves.

        Parameters:
        - barcode (str): The barcode of the item to be added.
        - customer (Customer): The customer to whom the item is being added.

        Returns:
        - bool: True if the item is successfully added to the shopping list, False otherwise.
        """
        for item in self._shelves:
            if item.get_barcode() == barcode:
                stock = item.get_stock()
                if stock > 0:
                    customer.shopping_list.append(item)
                    item.set_stock(stock - 1)  # Reduce the stock by 1
                    print(f"Item {item.get_name()} with barcode {barcode} added to customer's shopping list.")
                    return True
                else:
                    print(f"Item {item.get_name()} with barcode {barcode} is out of stock.")
                    return False

        print(f"Item with barcode {barcode} not found on the shelves.")
        return False

    def remove_items_from_purchase(self, barcode: str, customer: Customer) -> bool:
        """
        Removes an item from a customer's shopping list and increases the stock on the shelves.

        Parameters:
        - barcode (str): The barcode of the item to be removed.
        - customer (Customer): The customer from whom the item is being removed.

        Returns:
        - bool: True if the item is successfully removed from the shopping list, False otherwise.
        """
        item_found = False

        for item in customer.shopping_list:
            if item.get_barcode() == barcode:
                customer.shopping_list.remove(item)
                item.set_stock(item.get_stock() + 1)  # Increase the stock by 1
                item_found = True
                break

        if item_found is False:
            print(f"Item with barcode {barcode} not in customer's shopping list.")
            return False

        for shelf_item in self._shelves:
            if shelf_item.get_barcode() == barcode:
                shelf_item.set_stock(shelf_item.get_stock() + 1)  # Increase the stock on the shelves
                print(f"Item {shelf_item.get_name()} with barcode {barcode} removed from customer's shopping list.")
                return True

        print(f"Item with barcode {barcode} not found on the supermarket's shelves.")
        return False

    def edit_item_in_storage_room(self, barcode: str, property_name: str, new_value: Any) -> bool:
        """
        Edits the specified property of an item in the storage room with the given barcode.

        Parameters:
        - barcode (str): The barcode of the item to be edited.
        - property_name (str): The name of the property to be edited.
        - new_value (Any): The new value to be assigned to the property.

        Returns:
        - bool: True if the item's property is successfully edited, False otherwise.
        """
        for item in self._storage_room:
            if item.get_barcode() == barcode:
                # Update the specified property with the new value
                try:
                    current_value = getattr(item, property_name)
                    if isinstance(current_value, type(new_value)):
                        setattr(item, property_name, new_value)
                        print(f"Item {item.get_name()} with barcode '{barcode}' has been updated.")
                        return True
                    else:
                        print(f"Invalid value type for property '{property_name}'.")
                        return False
                except AttributeError:
                    print(f"Invalid item property: '{property_name}'.")
                    return False

        print(f"Item with barcode '{barcode}' not in the storage room.")
        return False

    def edit_item_on_shelves(self, barcode: str, property_name: str, new_value: Any) -> bool:
        """
        Edits the specified property of an item on the shelves with the given barcode.

        Parameters:
        - barcode (str): The barcode of the item to be edited.
        - property_name (str): The name of the property to be edited.
        - new_value (Any): The new value to be assigned to the property.

        Returns:
        - bool: True if the item's property is successfully edited, False otherwise.
        """
        for item in self._shelves:
            if item.get_barcode() == barcode:
                # Update the specified property with the new value
                try:
                    current_value = getattr(item, property_name)
                    if isinstance(new_value, type(current_value)):
                        setattr(item, property_name, new_value)
                        print(f"Item {item.get_name()} with barcode '{barcode}' has been updated.")
                        return True
                    else:
                        print(f"Invalid value type for property '{property_name}'.")
                        return False
                except AttributeError:
                    print(f"Invalid item property: '{property_name}'.")
                    return False

        print(f"Item with barcode '{barcode}' not found on the shelves.")
        return False

    def add_item_to_storage_room(self, item: Product) -> None:
        """
        Adds an item to the storage room. If the item already exists in the storage room, the stock is increased.

        Parameters:
        - item (Product): The item to be added to the storage room.

        Returns:
        - None
        """
        for existing_item in self._storage_room:
            if existing_item.get_barcode() == item.get_barcode():
                existing_item.set_stock(existing_item.get_stock() + item.get_stock())
                print(f"Item {item.get_name()} with barcode '{item.get_barcode()}' already exists in the storage room. "
                      f"Increasing stock by {item.get_stock()}.")
                return

        self._storage_room.append(item)
        print(f"Item {item.get_name()} with barcode '{item.get_barcode()}' added to the storage room.")

    def add_item_to_shelves(self, item: Product) -> None:
        """
        Adds an item to the shelves. If the item already exists on the shelves, the stock is increased.

        Parameters:
        - item (Product): The item to be added to the shelves.

        Returns:
        - None
        """
        for existing_item in self._shelves:
            if existing_item.get_barcode() == item.get_barcode():
                existing_item.set_stock(existing_item.get_stock() + item.get_stock())
                print(f"Item {item.get_name()} with barcode '{item.get_barcode()}' already exists on the shelves. "
                      f"Increasing stock by {item.get_stock()}.")
                return

        self._shelves.append(item)
        print(f"Item {item.get_name()} with barcode '{item.get_barcode()}' added to the shelves.")

    def add_employee(self, employee: Employee) -> bool:
        """
        Adds an employee to the system.

        Parameters:
        - employee (Employee): The employee to be added.

        Returns:
        - bool: True if the employee is added successfully, False if the employee already exists in the system.
        """
        for existing_employee in self._employees:
            if existing_employee.employee_number == employee.employee_number or\
                    existing_employee.get_ID() == employee.get_ID():
                print("Employee already exists in the system")
                return False
        self._employees.append(employee)
        print(f"Employee {employee.get_full_name()} with ID {employee.get_ID()} added to the system successfully.")
        return True

    def remove_employee(self, id: str) -> bool:
        """
        Removes an employee from the system based on their ID.

        Parameters:
        - id (str): The ID of the employee to be removed.

        Returns:
        - bool: True if the employee is removed successfully, False if the employee is not found in the system.
        """
        for existing_employee in self._employees:
            if existing_employee.get_ID() == id:
                self._employees.remove(existing_employee)
                print("Employee removed from the system successfully.")
                return True
        print(f"Employee with ID {id} not in the system.")
        return False

    def edit_employee_property(self, employee_id: str, property_name: str, new_value: str) -> bool:
        """
        Edits the specified property of an employee.

        Parameters:
        - employee_id (str): The ID of the employee to be edited.
        - property_name (str): The name of the property to be edited.
        - new_value (str): The new value to be assigned to the property.

        Returns:
        - bool: True if the employee's property is successfully edited, False otherwise.
        """
        for employee in self._employees:
            if employee.get_ID() == employee_id:
                # Check if the property exists in the employee object
                if hasattr(employee, property_name):
                    current_value = getattr(employee, property_name)
                    # Check if the property is a numerical value
                    if isinstance(current_value, (int, float)):
                        try:
                            # Try to convert the new value to the appropriate type
                            if isinstance(current_value, int):
                                new_value = int(new_value)
                            else:
                                new_value = float(new_value)
                        except ValueError:
                            print(f"Cannot change property '{property_name}' to a textual value.")
                            return False
                    # Update the property value
                    setattr(employee, property_name, new_value)
                    print(f"Employee property '{property_name}' updated successfully.")
                    return True
                else:
                    print(f"Employee does not have a property named '{property_name}'.")
                    return False
        print(f"Employee with ID '{employee_id}' not found.")
        return False

    def search_employees(self, category: str, query: str) -> List[Employee] or None:
        """
        Searches for employees based on the specified category and query.

        Parameters:
        - category (str): The category to search for (e.g., "class type", "employee number", "shift type", "id",
                          "full name", "phone number").
        - query (str): The query string to search for.

        Returns:
        - List[Employee] or None: A list of employees matching the search criteria, or None if no employees
                                  match the search criteria.
        """
        filtered_employees = []

        # Search and filter employees based on the given category and query
        if category.lower() == "class type":
            filtered_employees = [employee for employee in self._employees if query.lower() in employee.subclass_identifier.lower()]
        elif category.lower() == "employee number":
            filtered_employees = [employee for employee in self._employees if query.lower() in employee.employee_number.lower()]
        elif category.lower() == "shift type":
            filtered_employees = [employee for employee in self._employees if query.lower() in employee.shift_type.lower()]
        elif category.lower() == "id":
            filtered_employees = [employee for employee in self._employees if query.lower() in employee.get_ID().lower()]
        elif category.lower() == "full name":
            filtered_employees = [employee for employee in self._employees if query.lower() in employee.get_full_name().lower()]
        elif category.lower() == "phone number":
            filtered_employees = [employee for employee in self._employees if
                                  query.lower() in employee.get_phone_number().lower()]

        # Check if the filtered list is empty
        if not filtered_employees:
            return None

        # Return the filtered employees
        return filtered_employees

    def display_filtered_orders(self, category: str, query: Union[str, int, float, datetime]) -> None:
        """
        Displays the orders that match the specified category and query.

        Parameters:
        - category (str): The category to filter the orders by (e.g., "order code", "status", "customer id",
                          "customer name", "cash register number", "total price", "datetime").
        - query (Union[str, int, float, datetime]): The query value to filter the orders.

        Returns:
        - None
        """
        filtered_orders = []

        # Convert the query to the appropriate type if necessary
        if isinstance(query, str):
            query = query.lower()

        # Search and filter orders based on the given category and query
        if category.lower() == 'order code':
            for employee in self._employees:
                if isinstance(employee, Cashier):
                    filtered_orders.extend([order for order in employee.get_orders() if query == order.order_code.lower()])
        elif category.lower() == "status":
            for employee in self._employees:
                if isinstance(employee, Cashier):
                    filtered_orders.extend([order for order in employee.get_orders() if query == order.status.lower()])
        elif category.lower() == "customer id":
            for employee in self._employees:
                if isinstance(employee, Cashier):
                    filtered_orders.extend([order for order in employee.get_orders() if query == order.customer_id.lower()])
        elif category.lower() == "customer name":
            for employee in self._employees:
                if isinstance(employee, Cashier):
                    filtered_orders.extend([order for order in employee.get_orders() if query in order.customer_name.lower()])
        elif category.lower() == "cash register number":
            try:
                query = int(query)  # Convert the query to an integer
                for employee in self._employees:
                    if isinstance(employee, Cashier):
                        filtered_orders.extend([order for order in employee.get_orders() if query == order.cash_register_number])
            except ValueError:
                print("Invalid query. The 'cash register number' category requires an integer query.")
                return
        elif category.lower() == "total price":
            try:
                query = float(query)  # Convert the query to a float
                for employee in self._employees:
                    if isinstance(employee, Cashier):
                        filtered_orders.extend([order for order in employee.get_orders() if query == order.total_price])
            except ValueError:
                print("Invalid query. The 'total price' category requires a numeric query.")
                return
        elif category.lower() == "datetime":
            try:
                if isinstance(query, str):
                    query_date = datetime.strptime(query,
                                                    "%Y-%m-%d").date()  # Convert the query string to a date object
                elif isinstance(query, datetime):
                    query_date = query.date()  # Extract the date from the datetime object
                else:
                    raise ValueError(
                        "Invalid query. The 'datetime' category requires a valid datetime or date string in the format 'YYYY-MM-DD'.")
                for employee in self._employees:
                    if isinstance(employee, Cashier):
                        filtered_orders.extend(
                            [order for order in employee.get_orders() if query_date == order.datetime.date()])
            except ValueError as e:
                print(str(e))
                return
        else:
            print("Invalid category.")
            return

        if not filtered_orders:
            print("No orders found matching the search criteria.")
            return

        for order in filtered_orders:
            print(order)
            print("---------------")

    # Methods to display the entities in the supermarket in an organised manner
    def display_orders(self) -> List[Order] or None:
        print("List of all orders:")
        for employee in self._employees:
            if isinstance(employee, Cashier):
                for order in employee.get_orders():
                    print(order)
                    print("--------------------")

    def display_products_in_storage(self):
        print("Products in Storage:")
        for product in self._storage_room:
            print(product)
            print("--------------------")

    def display_products_on_shelves(self):
        print("Products on Shelves:")
        for product in self._shelves:
            print(product)
            print("--------------------")

    def display_customers(self):
        print("Customers:")
        for customer in self._customers:
            print(customer)
            print("--------------------")

    def display_employees(self):
        print("Employees:")
        for employee in self._employees:
            print(employee)
            print("--------------------")

    def find_user(self, phone_number, ID):
        for user in self._customers + self._employees:
            if user.get_phone_number() == phone_number and user.get_ID() == ID:
                return user
        return None

    # -----------------------------------------------------------------------------------------------------------------
    def __eq__(self, other):
        if isinstance(other, Supermarket):
            return (
                    self._storage_room == other._storage_room and
                    self._shelves == other._shelves and
                    self._customers == other._customers and
                    self._employees == other._employees
            )
        return False

    def __str__(self):
        return (
            f"Storage Room: {self._storage_room}\n"
            f"Shelves: {self._shelves}\n"
            f"Customers: {self._customers}\n"
            f"Employees: {self._employees}\n"
        )
