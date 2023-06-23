"""from DataModels.LogicHandlers.FileHandler import FileHandler
from DataModels.Persons.Customer import Customer
from DataModels.Persons.Employees.Cashier import Cashier
from DataModels.Persons.Employees.HeadManager import HeadManager
from DataModels.Persons.Employees.Organisers.Organiser import Organiser
from DataModels.Persons.Employees.Organisers.ShiftManager import ShiftManager
from DataModels.Product import Product
from DataModels.Supermarket import Supermarket"""
from DataModels.LogicHandlers.MenuManager import MenuManager

if __name__ == '__main__':
    """
    Code to define entities in the system and to add them to their appropriate object holders. i.e.: Employees
    To list of shift manager's list of responsible employees. Products to shelves and storage room of supermarket. Etc...
    Use the information below if you wish to log in to the system as an entity of your choice
    Uncomment code below along with above imports, and then comment the code at lines 134 and 135, and then execute program
    In order to save lists to your file directory, then do the reverse in order to load into the system with the lists loaded.
    """
    """head_manager = HeadManager("3421213123", "Marlon Brandy", "0523688521", '1', "Morning", 35, "Top-level Management")
    cashier1 = Cashier("0000000001", "Donnie Bakersfield", "0500000001", "1000", "Morning", "01", 0, [])
    cashier2 = Cashier("0000000002", "Hans Schnapps", "0500000002", "1001", "Morning", "02", 0, [])
    cashier3 = Cashier("0000000003", "Thompson J. Redding", "0500000003", "1002", "Morning", "03", 0, [])
    cashier4 = Cashier("0000000004", "Tommy K. Summers", "0500000004", "1003", "Morning", "04", 0, [])
    cashier5 = Cashier("0000000005", "Jonah J. Jameson", "0500000005", "1004", "Morning", "05", 0, [])
    cashier6 = Cashier("0000000006", "Cicero Leviticus", "0500000006", "1005", "Evening", "01", 0, [])
    cashier7 = Cashier("0000000007", "Harvard Orson", "0500000007", "1006", "Evening", "02", 0, [])
    cashier8 = Cashier("0000000008", "Abdallah Al Zahid", "0500000008", "1007", "Evening", "03", 0, [])
    cashier9 = Cashier("0000000009", "Othman Taha", "0500000009", "1008", "Evening", "04", 0, [])
    cashier10 = Cashier("0000000010", "Jerry Seinfeld", "0500000010", "1009", "Evening", "05", 0, [])
    cashier11 = Cashier("0000000011", "Will Springfield", "0500000011", "1010", "Midnight", "01", 0, [])
    cashier12 = Cashier("0000000012", "Mike Victor", "0500000012", "1011", "Midnight", "02", 0, [])
    cashier13 = Cashier("0000000013", "Michael De Santos", "0500000013", "1012", "Midnight", "03", 0, [])
    cashier14 = Cashier("0000000014", "Johnny Gunn", "0500000014", "1013", "Midnight", "04", 0, [])
    cashier15 = Cashier("0000000015", "Vin Diesel", "0500000015", "1014", "Midnight", "05", 0, [])
    organiser1 = Organiser("2849023521", "Hudson Robertson", "059832421", "231", "Morning", ["Fruit", "Beverage"])
    organiser2 = Organiser("4363464312", "Alfred Manfred", "053295820", "572", "Morning", ["Vegetable", "Starch"])
    organiser3 = Organiser("9765634523", "Arby Schofield", "032149814", "547", "Morning", ["Canned", "Frozen"])
    organiser4 = Organiser("1232143253", "Liam Nelson", "03932815021", "763", "Evening", ["Dairy", "Hygiene"])
    organiser5 = Organiser("5476575762", "Scotty Jessman", "0321421411", "345", "Evening", ["Meat", "Pharmaceutical"])
    organiser6 = Organiser("3453453412", "Mark Wahlster", "03219841041", "978", "Evening", ["Seafood", "Household"])
    organiser7 = Organiser("32532532412", "Schuster Aloon", "03218414124", "972", "Midnight", ["Deli", "Baby-care"])
    organiser8 = Organiser("76868566423", "Asterix Asgard", "032141841", "564", "Midnight", ["Condiment", "Pet-care"])
    organiser9 = Organiser("329i522342", "Obelix Brassard", "033285t028", "178", "Midnight", ["Snack", "Auto-repair"])
    organiser10 = Organiser("32492i5235", "Sammy Hyde", "0384937523", "835", "Evening", ["Baking", "Hardware"])
    product1 = Product("383928392323", "Apple", 3.0, "Fruit", 2300)
    product2 = Product("948378233423", "Corncob", 5.0, "Vegetable", 564)
    product3 = Product("3943243284924", "Tomato Sauce", 10.0, "Canned", 345)
    product4 = Product("328459i8359832", "Milk", 7.0, "Dairy", 765)
    product5 = Product("3242424924242", "Cow Ribs", 45.0, "Meat", 324)
    product6 = Product("9885747838322", "Salmon", 55.0, "Seafood", 432)
    product7 = Product("9468596068340", "Salami", 25.0, "Deli", 643)
    product8 = Product("3245949036833", "Ketchup", 8.0, "Condiment", 425)
    product9 = Product("3290852905221", "Bamba", 4.0, "Snack", 128)
    product10 = Product("9680588456023", "Flour", 3.0, "Baking", 947)
    product11 = Product("383928392323", "Apple", 3.0, "Fruit", 234)
    product12 = Product("948378233423", "Corncob", 5.0, "Vegetable", 1980)
    product13 = Product("3943243284924", "Tomato Sauce", 10.0, "Canned", 789)
    product14 = Product("328459i8359832", "Milk", 7.0, "Dairy", 1956)
    product15 = Product("3242424924242", "Cow Ribs", 45.0, "Meat", 112)
    product16 = Product("9885747838322", "Salmon", 55.0, "Seafood", 98)
    product17 = Product("9468596068340", "Salami", 25.0, "Deli", 398)
    product18 = Product("3245949036833", "Ketchup", 8.0, "Condiment", 554)
    product19 = Product("3290852905221", "Bamba", 4.0, "Snack", 678)
    product20 = Product("9680588456023", "Flour", 3.0, "Baking", 713)
    product21 = Product("792000000000", "Heineken", 17.0, "Beverage", 99)
    product22 = Product("792000000001", "Jasmin Rice", 58.0, "Starch", 98)
    product23 = Product("792000000002", "Frozen Schnitzel", 45.0, "Frozen", 97)
    product24 = Product("792000000003", "Dry Hair Shampoo", 15.0, "Hygiene", 96)
    product25 = Product("792000000004", "Medical Bandages", 10.0, "Pharmaceutical", 95)
    product26 = Product("792000000005", "Chair", 580.0, "Household", 94)
    product27 = Product("792000000006", "Castor Oil", 25.0, "Baby-care", 93)
    product28 = Product("792000000007", "Crunchy Fish Biscuits", 65.0, "Pet-care", 92)
    product29 = Product("792000000008", "Tire Wrench", 850.0, "Auto-repair", 91)
    product30 = Product("792000000009", "Screwdriver Set", 75.0, "Hardware", 90)
    product31 = Product("792000000000", "Heineken", 17.0, "Beverage", 499)
    product32 = Product("792000000001", "Jasmin Rice", 58.0, "Starch", 498)
    product33 = Product("792000000002", "Frozen Schnitzel", 45.0, "Frozen", 497)
    product34 = Product("792000000003", "Dry Hair Shampoo", 15.0, "Hygiene", 496)
    product35 = Product("792000000004", "Medical Bandages", 10.0, "Pharmaceutical", 495)
    product36 = Product("792000000005", "Chair", 580.0, "Household", 494)
    product37 = Product("792000000006", "Castor Oil", 25.0, "Baby-care", 493)
    product38 = Product("792000000007", "Crunchy Fish Biscuits", 65.0, "Pet-care", 492)
    product39 = Product("792000000008", "Tire Wrench", 850.0, "Auto-repair", 491)
    product40 = Product("792000000009", "Screwdriver Set", 75.0, "Hardware", 490)
    customer1 = Customer("322123123", "Jones Davis", "05234522312", 50300.00, [], [], [])
    customer2 = Customer("324243241", "Morgan Harlem", "053924212", 73540.00, [], [], [])
    customer3 = Customer("435353421", "Shahar Glick", "053258328", 82930.00, [], [], [])
    customer4 = Customer("546457343", "Jackie Williams", "0532982123", 34872.00, [], [], [])
    customer5 = Customer("232424234", "Murphy Jameson", "05392843294", 53342.00, [], [], [])
    customer6 = Customer("768698645", "Peter Harrison", "0523984284", 67839.00, [], [], [])
    customer7 = Customer("234324234", "Simons Petrov", "05893242232", 78921.00, [], [], [])
    customer8 = Customer("658658543", "Leon S. Kennedy", "0542542445", 98732.00, [], [], [])
    customer9 = Customer("543434545", "Chris Redfield", "0525873273", 83928.00, [], [], [])
    customer10 = Customer("354343434", "Noah Watson", "05357437445", 32422.00, [], [], [])
    customer11 = Customer("786837537", "Jamie Whitfield", "05543437583", 98372.00, [], [], [])
    customer12 = Customer("876767856", "Arthur Richardson", "0553573674", 83728.00, [], [], [])
    shift_manager1 = ShiftManager("3274328412", "Avi Cohen", "05118549654", '2', "Morning", [cashier1, cashier2,
                                                                                             cashier3, cashier4,
                                                                                             cashier5, organiser1,
                                                                                             organiser2, organiser3])
    shift_manager2 = ShiftManager("3829502982", "Benjamin Breckleson", "05542374525", '3', "Evening", [cashier6,
                                                                                                       cashier7,
                                                                                                       cashier8,
                                                                                                       cashier9,
                                                                                                       cashier10,
                                                                                                       organiser4,
                                                                                                       organiser5,
                                                                                                       organiser6,
                                                                                                       organiser10])
    shift_manager3 = ShiftManager("32584817884", "David Rosenberg", "0325145551", '4', "Midnight", [cashier11,
                                                                                                    cashier12,
                                                                                                    cashier13,
                                                                                                    cashier14,
                                                                                                    cashier15,
                                                                                                    organiser7,
                                                                                                    organiser8,
                                                                                                    organiser9])
    supermarket = Supermarket()
    supermarket.shelves = [product1, product2, product3, product4, product5, product6, product7, product8, product9,
                           product10, product21, product22, product23, product24, product25, product26, product27,
                           product28, product29, product30]
    supermarket.storage_room = [product11, product12, product13, product14, product15, product16, product17, product18,
                                product19, product20, product31, product32, product33, product34, product35, product36,
                                product37, product38, product39, product40]
    supermarket.customers = [customer1, customer2, customer3, customer4, customer5, customer6, customer7, customer8,
                             customer9, customer10, customer11, customer12]
    supermarket.employees = [head_manager, shift_manager1, shift_manager2, shift_manager3, cashier1, cashier2, cashier3,
                             cashier4, cashier5, cashier6, cashier7, cashier8, cashier9, cashier10, cashier11,
                             cashier12,
                             cashier13, cashier14, cashier15, organiser1, organiser2, organiser3, organiser4,
                             organiser5,
                             organiser6, organiser7, organiser8, organiser9, organiser10]
    FileHandler.save_supermarket(supermarket)"""
    menu = MenuManager()
    menu.initialize()