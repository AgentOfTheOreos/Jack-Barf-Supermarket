import sys
import msvcrt

from DataModels.LogicHandlers.AccountManager import AccountManager
from DataModels.LogicHandlers.FileHandler import FileHandler
from DataModels.Persons.Customer import Customer
from DataModels.Persons.Employees.Cashier import Cashier
from DataModels.Persons.Employees.HeadManager import HeadManager
from DataModels.Persons.Employees.Organisers.Organiser import Organiser
from DataModels.Persons.Employees.Organisers.ShiftManager import ShiftManager
from DataModels.Product import Product


class MenuManager:
    def __init__(self):
        self._supermarket = FileHandler.load_supermarket()
        self.menu_stack = []

    def get_supermarket(self):
        return self._supermarket

    def initialize(self):
        print("""
           _________________________     __________________________________________     __________________________  ____
   7  77  _  77     77  7  7     7  _  77  _  77  _  77     77  77     77 7     7     77     77     77    \ 7  7
___|  ||  _  ||  ___!|   __!     |   __||  _  ||    _||  ___!|  ||  _  |!/      |   __!|  7  ||  7  ||  7  ||  |
7  !  ||  7  ||  7___|     |     |  _  ||  7  ||  _ \ |  __| |  ||  7  |        |  !  7|  |  ||  |  ||  |  |!__!
|     ||  |  ||     7|  7  |     |  7  ||  |  ||  7  ||  7   |  ||  |  |        |     ||  !  ||  !  ||  !  |____
!_____!!__!__!!_____!!__!__!     !_____!!__!__!!__!__!!__!   !__!!__!__!        !_____!!_____!!_____!!_____!7__7
                                                                                                                
                                            ⠀⠈⠛⠻⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠈⢻⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
                                    ⠀⠀⠀⠀⠀⠀⠀⢻⡏⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⣿⠉⠉⠉⠉⠉⣹⠇⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣀⣀⣀⣸⣧⣀⣀⣀⣀⣿⣄⣀⣀⣀⣠⡿⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⠁⠀⠀⠀⣿⠃⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣤⣼⣧⣤⣤⣤⣤⣿⣤⣤⣤⣼⡏⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⢸⡇⠀⠀⠀⠀⣿⠀⠀⢠⡿⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠤⠼⠷⠤⠤⠤⠤⠿⠦⠤⠾⠃⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣷⢶⣶⠶⠶⠶⠶⠶⠶⣶⠶⣶⡶⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣠⡿⠀⠀⠀⠀⠀⠀⢷⣄⣼⠇⠀
        \n""")
        print("""============================================
        Initializing supermarket...
        Supermarket initialized successfully.\n""")
        self.main_menu()

    def main_menu(self):
        """
        Displays the main menu options and handles user input.

        This method presents the user with the main menu options, such as login to an existing account or client registration.
        It handles the user's choice and invokes the corresponding methods based on the selected option.
        The menu continues to be displayed until the user chooses to quit the program.

        Note:
        - The menu stack is used to keep track of the previous menus.
        - The program terminates when the user selects the "Q" option.
        """
        while True:
            print("""============================================")
            ==== MAIN MENU ====
            1. Login to an existing account.
            2. Client Registration.\n""")
            choice = self.get_user_input("Enter your choice: ")
            if choice == "1":
                self.menu_stack.append(self.main_menu)
                self.login_prompt()
            elif choice == "2":
                self.menu_stack.append(self.main_menu)
                self.register_prompt()
            elif choice == "Q":
                """if self.menu_stack:1
                    self.menu_stack.pop()()  # Call the previous menu function
                else:"""
                print("Thank you for using the Supermarket Management System. Goodbye!")
                sys.exit()  # Terminate the program
            else:
                print("Invalid choice. Please try again.")
                continue

    def login_prompt(self):
        """
        Prompts the user to enter login credentials and validates the login.

        This method prompts the user to enter their phone number and ID for login.
        It calls the AccountManager's `validate_login` method to validate the login credentials.
        Based on the user type, it navigates to the corresponding menu or returns to the main menu.
        If the user is not found, it displays an appropriate message and returns to the main menu.
        """
        print("==== LOGIN ====")
        phone_number = input("Enter your phone number: ")
        print('\n')
        ID = input("Enter your ID: ")
        print('\n')

        user = AccountManager.validate_login(phone_number, ID, self._supermarket)
        if user is not None:
            if isinstance(user, Customer):
                self.customer_menu(user)
            elif isinstance(user, Cashier):
                self.cashier_menu(user)
            elif isinstance(user, ShiftManager):
                self.shift_manager_menu(user)
            elif isinstance(user, HeadManager):
                self.head_manager_menu()
            elif isinstance(user, Organiser):
                self.organiser_menu(user)
            else:
                print("Invalid user type.")
                self.main_menu()
        else:
            print("User not found. Returning to the main menu...")
            self.main_menu()

    def register_prompt(self):
        """
        Prompts the user to register a new client.

        This method prompts the user to enter the necessary information for registering a new client.
        It validates the input and creates a new `Customer` object.
        If the registration is successful, it adds the customer to the supermarket and saves the changes to a file.
        After registration, it returns to the main menu.
        """
        print("==== CLIENT REGISTRATION ====")
        client_id = input("Please enter the new client's ID: ")
        if not client_id.isdigit():
            print("Client ID must be numerical only.")
            self.main_menu()

        client_name = input("Please enter the new client's full name: ")
        if not client_name.isalpha():
            print("Client name must be textual only.")
            self.main_menu()

        client_phone_number = input("Please enter new client's phone number: ")
        if not client_phone_number.isdigit() or not client_phone_number.startswith("05"):
            print("Phone number must be numerical and start with 05x.")
            self.main_menu()

        client_account_balance = input("Please enter the new client's account balance: ")
        if not client_account_balance.isdigit():
            print("Client account balance must be numerical only.")
            self.main_menu()
        elif float(client_account_balance) < 0:
            print("Client account balance cannot be negative.")
            self.main_menu()

        client = Customer(client_id, client_name, client_phone_number, float(client_account_balance), [], [], [])
        if self._supermarket.add_customer(client):
            FileHandler.save_supermarket(self._supermarket)
        self.main_menu()

    def customer_menu(self, user: Customer):
        """
        Displays the menu options for a customer and handles their choices.

        Args:
            user (Customer): The customer object.

        Returns:
            None
        """
        while True:
            print("""============================================
            ----=CUSTOMER MENU=----
            1. View total price of items in grocery list.
            2. View list of orders.
            3. Commence grocery list purchase.
            4. Display items on shelves in supermarket.
            5. Cancel a standing order.
            6. Add an item to grocery list.
            7. Remove an item from grocery list.
            8. View grocery list.
            9. Clear shopping list.\n""")
            choice = self.get_user_input("Enter your choice: ")
            if choice == "1":
                print("============================================")
                if not user.shopping_list:
                    print("Your grocery list is empty.")
                else:
                    user.view_total_price_of_grocery_list()
                continue
            elif choice == "2":
                print("============================================")
                if not user.order_list:
                    print("Your order list is empty.")
                else:
                    user.view_list_of_customer_orders()
                continue
            elif choice == "3":
                print("============================================")
                if not user.shopping_list:
                    print("Your grocery list is empty. Cannot commence purchase order.")
                else:
                    register_number = input("Please enter cash register number to send order to: ") + '\n'
                    shift = input("Please enter the shift at which you wish your order to be viewed.") + '\n'
                    if shift not in "Morning" or "Evening" or "Midnight":
                        print("Invalid shift!")
                    elif self._supermarket.create_purchase_order(user, register_number, shift):
                        FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "4":
                print("============================================")
                self.search_shelves_prompt()
            elif choice == "5":
                print("============================================")
                if not user.order_list:
                    print("Your order list is empty.")
                else:
                    while True:
                        order_code = input(
                            "Please enter the order code of the order you wish to cancel: ")
                        if order_code.isdigit():
                            order_code = int(order_code)
                            if self._supermarket.cancel_purchase_order(user, order_code):
                                FileHandler.save_supermarket(self._supermarket)
                            break
                        else:
                            print("Invalid order code. Please enter a numeric value.")
                continue
            elif choice == "6":
                print("============================================")
                barcode = input(
                    "Please enter the barcode of the product you wish to add to your grocery list: ")
                if self._supermarket.add_items_to_purchase(customer=user, barcode=barcode):
                    FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "7":
                print("============================================")
                if not user.shopping_list:
                    print("Your grocery list is empty. No products to remove from the list.")
                else:
                    barcode = input(
                        "Please enter the barcode of the product you wish to remove from your grocery list: ")
                    if self._supermarket.remove_items_from_purchase(customer=user, barcode=barcode):
                        FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "8":
                print("============================================")
                if not user.shopping_list:
                    print("Your grocery list is empty. Nothing to view.")
                else:
                    user.view_list_of_customer_grocery_list()
                continue
            elif choice == "9":
                print("============================================")
                if not user.shopping_list:
                    print("Your grocery list is empty. Nothing to clear.")
                else:
                    user.clear_shopping_list()
                continue
            elif choice == "Q":
                self.menu_stack.pop()()
            else:
                print("Invalid choice. Please try again.")
                continue

    def cashier_menu(self, user: Cashier):
        """
        Displays the menu options for a cashier and handles their choices.

        Args:
            user (Cashier): The cashier object.

        Returns:
            None
        """
        while True:
            print("""============================================
            ----=CASHIER MENU=----
            1. View list of assigned orders.
            2. Confirm a customer's purchase order.""")
            choice = self.get_user_input("Enter your choice: ")
            if choice == "1":
                print("============================================")
                if not user.get_orders():
                    print("Your assigned orders list is empty. Nothing to view.")
                else:
                    user.view_list_of_cashier_orders()
                continue
            elif choice == "2":
                print("============================================")
                if not user.get_orders():
                    print("Your order list is empty.")
                else:
                    while True:
                        order_code = input(
                            "Please enter the order code of the assigned order you wish to confirm: ")
                        if order_code.isdigit():
                            order_code = int(order_code)
                            if self._supermarket.purchase_confirmation(user, order_code):
                                FileHandler.save_supermarket(self._supermarket)
                            break
                        else:
                            print("Invalid order code. Please enter a numeric value.")
                continue
            elif choice == "Q":
                self.menu_stack.pop()()
            else:
                print("Invalid choice. Please try again.")
                continue

    def organiser_menu(self, user: Organiser):
        """
        Displays the menu options for an organiser and handles their choices.

        Args:
            user (Organiser): The organiser object.

        Returns:
            None
        """
        while True:
            print("""============================================
            ----=ORGANISER MENU=----
            1. View items on shelves under organiser's responsible types.
            2. Fill the stock of a product under organiser's responsible types.
            3. Remove item from supermarket shelves under organiser's responsible types.""")
            choice = self.get_user_input("Enter your choice: ")
            if choice == "1":
                print("============================================")
                matching_items = self._supermarket.get_shelf_items_organiser(user)
                if matching_items is None:
                    print("Matching items falling under organiser responsible types not found.")
                else:
                    for item in matching_items:
                        print(item)
                continue
            elif choice == "2":
                print("============================================")
                barcode = input("Please enter the barcode of the item you wish to fill out the stock for.")
                if user.fill_shelves_with_low_stock_item(barcode, self._supermarket.shelves,
                                                         self._supermarket.storage_room):
                    FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "3":
                print("============================================")
                barcode = input("Please enter the barcode of the item you wish to remove from the shelves.")
                if user.remove_item_from_shelf(barcode, self._supermarket.shelves, self._supermarket.storage_room):
                    FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "Q":
                self.menu_stack.pop()()
            else:
                print("Invalid choice. Please try again.")
                continue

    def shift_manager_menu(self, user: ShiftManager):
        """
        Displays the menu options for a shift manager and handles their choices.

        Args:
            user (ShiftManager): The shift manager object.

        Returns:
            None
        """
        while True:
            print("""============================================
            ----=SHIFT MANAGER MENU=----
            1. View products on the shelves.
            2. View products in the storage room.
            3. Edit property of a product in the system.
            4. View list of employees that the shift manager is responsible for.
            5. Remove a product from the system.
            6. Add a product to the system.
            7. Fill products with low stock on the shelves.""")
            choice = self.get_user_input("Enter your choice: ")
            if choice == "1":
                print("============================================")
                self.search_shelves_prompt()
                continue
            elif choice == "2":
                print("============================================")
                self.search_storage_room_prompt()
                continue
            elif choice == "3":
                print("============================================")
                product_barcode = input("Please enter the barcode of the product you wish to edit information of: ")
                if not product_barcode.isdigit():
                    print("Product barcode must be numerical.")
                else:
                    property_to_edit = input("Please enter the name of the property you wish to edit: ")
                    new_value = input(
                        "Please enter the new value you wish to update the old value in the property to: ")
                    location = input("Please enter the location of the product you wish to edit: ")
                    if location.lower() == "shelves":
                        if self._supermarket.edit_item_on_shelves(product_barcode, property_to_edit, new_value):
                            FileHandler.save_supermarket(self._supermarket)
                    elif location.lower() == "storage room":
                        if self._supermarket.edit_item_in_storage_room(product_barcode, property_to_edit, new_value):
                            FileHandler.save_supermarket(self._supermarket)
                    else:
                        print("Invalid location, can either be shelves or storage room.")
                continue
            elif choice == "4":
                print("============================================")
                if not user.responsible_employees:
                    print("Shift manager has no employees he's responsible for.")
                else:
                    user.view_responsible_employees()
                continue
            elif choice == "5":
                print("============================================")
                barcode = input("Please enter the barcode of the item you wish to remove from the storage room: ")
                location = input("Please enter the location that you wish to remove the product from: ")
                if location.lower() == "shelves":
                    if user.remove_item_from_shelf(barcode, self._supermarket.shelves, self._supermarket.storage_room):
                        FileHandler.save_supermarket(self._supermarket)
                elif location.lower() == "storage room":
                    if user.remove_item_from_storage_room(barcode, self._supermarket.storage_room):
                        FileHandler.save_supermarket(self._supermarket)
                else:
                    print("Invalid location, can either be shelves or storage room.")
                continue
            elif choice == "6":
                print("============================================")
                self.add_product_prompt()
                continue
            elif choice == "7":
                print("============================================")
                barcode = input("Please enter the barcode of the item you wish to fill the stock of: ")
                if user.fill_shelves_with_low_stock_item(barcode, self._supermarket.shelves,
                                                         self._supermarket.storage_room):
                    FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "Q":
                self.menu_stack.pop()()
            else:
                print("Invalid choice. Please try again.")
                continue

    def head_manager_menu(self):
        """
        Displays the menu options for a head manager and handles their choices.

        Returns:
            None
        """
        while True:
            print("""============================================
            ----=HEAD MANAGER MENU=----
            1. View items on the shelves.
            2. View items in the storage room.
            3. View employees in the system.
            4. View orders in the system.
            5. Edit property of an employee.
            6. Add employee to the system.
            7. Remove employee from the system.""")
            choice = self.get_user_input("Enter your choice: ")
            if choice == "1":
                print("============================================")
                self.search_shelves_prompt()
                continue
            elif choice == "2":
                print("============================================")
                self.search_storage_room_prompt()
                continue
            elif choice == "3":
                print("============================================")
                self.search_employees_prompt()
                continue
            elif choice == "4":
                print("============================================")
                self.search_orders_prompt()
                continue
            elif choice == "5":
                print("============================================")
                employee_id = input("Please enter the ID of the employee you wish to edit information of: ")
                if not employee_id.isdigit():
                    print("Employee ID must be numerical.")
                else:
                    property_to_edit = input("Please enter the name of the property you wish to edit: ")
                    new_value = input(
                        "Please enter the new value you wish to update the old value in the property to: ")
                    if self._supermarket.edit_employee_property(employee_id, property_to_edit, new_value):
                        FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "6":
                print("============================================")
                self.add_employee_prompt()
                continue
            elif choice == "7":
                print("============================================")
                employee_id = input("Please enter the ID of the employee you wish to remove: ")
                if not employee_id.isdigit():
                    print("Employee ID must be numerical.")
                else:
                    if self._supermarket.remove_employee(employee_id):
                        FileHandler.save_supermarket(self._supermarket)
                continue
            elif choice == "Q":
                self.menu_stack.pop()()
            else:
                print("Invalid choice. Please try again.")
                continue

    def add_product_prompt(self):
        """
        Prompts the user to enter details for a new product and adds it to the supermarket's shelves or storage room.

        Returns:
        - None
        """
        while True:
            barcode = input("Please enter the new product's barcode: ")
            if not barcode.isdigit():
                print("Product barcode must be numerical only.")
                break

            product_name = input("Please enter the new product's name: ")
            if product_name.isdigit():
                print("Product name cannot be entirely made up of digits.")
                break

            product_price = input("Please enter product's price: ")
            if not product_price.isdigit():
                print("Product price must be numerical only.")
                break
            elif float(product_price) < 1.0:
                print("Product price cannot be smaller than 1.")
                break

            product_type = input("Please enter the type of the product: ")
            if product_type not in Product.ALLOWED_ITEM_TYPES:
                print("""
                Invalid Product type, must be one of the following:
                "Fruit", "Vegetable", "Canned", "Dairy", "Meat", "Seafood", "Deli",
                "Condiment", "Snack", "Baking", "Beverage", "Starch", "Frozen",
                "Hygiene", "Pharmaceutical", "Household", "Baby-care", "Pet-care",
                "Auto-repair", "Hardware".
                 """)
                break

            product_stock = input("Please enter product's stock: ")
            if not product_stock.isdigit():
                print("Product stock must be numerical only.")
                break
            elif int(product_stock) < 1:
                print("Product stock cannot be smaller than 1.")
                break

            product = Product(barcode, product_name, float(product_price), product_type, int(product_stock))
            location = input("Please enter the location that you want to add the product to: ")
            if location.lower() == "shelves":
                if self._supermarket.add_item_to_shelves(product):
                    FileHandler.save_supermarket(self._supermarket)
            elif location.lower() == "storage room":
                if self._supermarket.add_item_to_storage_room(product):
                    FileHandler.save_supermarket(self._supermarket)
            else:
                print("Invalid location, can either be shelves or storage room.")
            break

    def add_employee_prompt(self):
        """
        Prompts the user to enter details for a new employee and adds them to the supermarket's employee list.

        Returns:
        - None
        """
        while True:
            employee_id = input("Please enter the new employee's ID: ")
            if not employee_id.isdigit():
                print("Employee ID must be numerical only.")
                break

            employee_name = input("Please enter the new employee's full name: ")
            if not employee_name.isalpha():
                print("Employee name must be textual only.")
                break

            employee_phone_number = input("Please enter employee's phone number: ")
            if not employee_phone_number.isdigit() or not employee_phone_number.startswith("05"):
                print("Phone number must be numerical and start with 05x.")
                break

            employee_number = input("Please enter the number of the employee: ")
            if not employee_number.isdigit():
                print("Employee number must be numerical.")
                break

            shift_type = input("Please enter the employee's shift: ")
            if not shift_type.isalpha() or shift_type not in ["Morning", "Evening", "Midnight"]:
                print("Shift must be textual and one of the following: Morning, Evening, Midnight.")
                break

            employee_subclass = input("Please enter the type of the employee: ")
            if employee_subclass.lower() == "cashier":
                cash_register_number = input("Please enter the cash register number: ")
                total_transactions = 0
                orders = []
                employee = Cashier(employee_id, employee_name, employee_phone_number, employee_number,
                                   shift_type, cash_register_number, total_transactions, orders)
            elif employee_subclass.lower() == "organiser":
                employee = Organiser(employee_id, employee_name, employee_phone_number, employee_number,
                                     shift_type, [])
            elif employee_subclass.lower() == "shift manager":
                employee = ShiftManager(employee_id, employee_name, employee_phone_number, employee_number,
                                        shift_type, [])
            else:
                print("Invalid employee subclass. Please try again.")
                break

            if self._supermarket.add_employee(employee):
                FileHandler.save_supermarket(self._supermarket)
            break

    def search_orders_prompt(self):
        """
        Displays a menu for searching orders in the system and performs the selected search operation.

        Returns:
        - None
        """
        while True:
            print("=================SEARCH ORDERS MENU====================")
            print("1. Search orders in the system by category and query.")
            print("2. View all orders in the system.")
            search_option = self.get_user_input("Enter your choice: ")
            if search_option == "1":
                category = input("Enter the category: ")
                query = input("Enter the query: ")
                self._supermarket.display_filtered_orders(category, query)
                break
            elif search_option == "2":
                self._supermarket.display_orders()
                break
            elif search_option == "Q":
                break
            else:
                print("Invalid choice. Please try again.")
            continue

    def search_employees_prompt(self):
        """
        Displays a menu for searching employees in the system and performs the selected search operation.

        Returns:
        - None
        """
        while True:
            print("=================SEARCH EMPLOYEES MENU====================")
            print("1. Search employees in the system by category and query.")
            print("2. View all employees in the system.")
            search_option = self.get_user_input("Enter your choice: ")
            if search_option == "1":
                category = input("Enter the category: ")
                query = input("Enter the query: ")
                results = self._supermarket.search_employees(category, query)
                if results is None:
                    print(
                        "Search operation failed, either the employees you are looking for do not match your search"
                        "criteria, or you have entered an invalid category, or you have entered a textual query "
                        "for a numerical category.")
                else:
                    for employee in results:
                        print(employee)
                        print("-----")
                break
            elif search_option == "2":
                self._supermarket.display_employees()
                break
            elif search_option == "Q":
                break
            else:
                print("Invalid choice. Please try again.")
            continue

    def search_shelves_prompt(self):
        """
        Displays a menu for searching items on shelves in the supermarket and performs the selected search operation.

        Returns:
        - None
        """
        while True:
            print("=================SEARCH SHELVES MENU====================")
            print("1. Search items on shelves by category and query.")
            print("2. View all items on shelves.")
            search_option = self.get_user_input("Enter your choice: ")
            if search_option == "1":
                category = input("Enter the category: ")
                query = input("Enter the query: ")
                results = self._supermarket.search_query_items_on_shelves(category, query)
                if results is None:
                    print(
                        "Search operation failed, either the items you are looking for do not match your search"
                        "criteria, or you have entered an invalid category, or you have entered a textual query "
                        "for a numerical category.")
                else:
                    for item in results:
                        print(item)
                        print("-----")
                break
            elif search_option == "2":
                self._supermarket.display_products_on_shelves()
                break
            elif search_option == "Q":
                break
            else:
                print("Invalid choice. Please try again.")
            continue

    def search_storage_room_prompt(self):
        """
        Displays a menu for searching items in the storage room of the supermarket and performs the selected search operation.

        Returns:
        - None
        """
        while True:
            print("=================SEARCH STORAGE ROOM MENU====================")
            print("1. Search items in storage room by category and query.")
            print("2. View all items in storage room.")
            search_option = self.get_user_input("Enter your choice: ")
            if search_option == "1":
                category = input("Enter the category: ")
                query = input("Enter the query: ")
                results = self._supermarket.search_query_items_in_storage_room(category, query)
                if results is None:
                    print(
                        "Search operation failed, either the items you are looking for do not match your search"
                        "criteria, or you have entered an invalid category, or you have entered a textual query "
                        "for a numerical category.")
                else:
                    for item in results:
                        print(item)
                        print("-----")
                break
            elif search_option == "2":
                self._supermarket.display_products_in_storage()
                break
            elif search_option == "Q":
                break
            else:
                print("Invalid choice. Please try again.")
            continue

    @staticmethod
    def get_user_input(prompt):
        """
        Displays the specified prompt to the user and waits for their input.

        Parameters:
        - prompt (str): The prompt message to display.

        Returns:
        - str: The user's input, converted to uppercase.
        """
        print(prompt, end="")
        while True:
            char = msvcrt.getwche()
            if char in ("\r", "\n"):  # Handle Enter key press
                print()
                continue
            elif char == chr(3):  # Handle Ctrl+C
                raise KeyboardInterrupt
            else:
                print('\n')
                return char.upper()  # Convert to uppercase for uniform comparison
