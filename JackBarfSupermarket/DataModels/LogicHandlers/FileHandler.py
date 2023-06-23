import os
import pickle

from DataModels.Exceptions.FileHandlerError import FileHandlerError
from DataModels.Supermarket import Supermarket


class FileHandler:
    @staticmethod
    def save_property(obj, property_name, filename):
        """
        Save a specific property of an object to a file using pickle.

        Args:
            obj (object): The object containing the property to be saved.
            property_name (str): The name of the property to be saved.
            filename (str): The name of the file to save the property to.

        Returns:
            None
        """
        directory = "./ObjectFiles"
        os.makedirs(directory, exist_ok=True)

        file_path = os.path.join(directory, filename)
        with open(file_path, "wb") as file:
            pickle.dump(getattr(obj, property_name), file)
        print(f"Property '{property_name}' saved successfully in files.")

    @staticmethod
    def load_property(obj, property_name, filename):
        """
        Load a property from a file and set it on an object using pickle.

        Args:
            obj (object): The object to set the loaded property on.
            property_name (str): The name of the property to be loaded.
            filename (str): The name of the file to load the property from.

        Returns:
            None
        """
        directory = "./ObjectFiles"

        file_path = os.path.join(directory, filename)
        with open(file_path, "rb") as file:
            setattr(obj, property_name, pickle.load(file))
        print(f"Property '{property_name}' loaded successfully into object.")

    @staticmethod
    def save_supermarket(supermarket: Supermarket):
        """
        Save the state of the supermarket object to files.

        Args:
            supermarket (Supermarket): The supermarket object to be saved.

        Returns:
            None
        """
        try:
            # Save storage room
            FileHandler.save_property(supermarket, "storage_room", "storage_room.pkl")

            # Save shelves
            FileHandler.save_property(supermarket, "shelves", "shelves.pkl")

            # Save customers
            FileHandler.save_property(supermarket, "customers", "customers.pkl")

            # Save employees
            FileHandler.save_property(supermarket, "employees", "employees.pkl")

            print("Supermarket saved successfully.")
        except Exception as e:
            raise FileHandlerError("Error occurred while saving the supermarket.") from e

    @staticmethod
    def load_supermarket() -> Supermarket:
        """
        Load the state of the supermarket object from files.

        Returns:
            Supermarket: The loaded supermarket object.
        """
        try:
            supermarket = Supermarket()

            # Load storage room
            FileHandler.load_property(supermarket, "storage_room", "storage_room.pkl")

            # Load shelves
            FileHandler.load_property(supermarket, "shelves", "shelves.pkl")

            # Load customers
            FileHandler.load_property(supermarket, "customers", "customers.pkl")

            # Load employees
            FileHandler.load_property(supermarket, "employees", "employees.pkl")

            print("Supermarket loaded successfully.")
            return supermarket
        except Exception as e:
            raise FileHandlerError("Error occurred while loading the supermarket.") from e
