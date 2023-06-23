from DataModels.Supermarket import Supermarket


class AccountManager:
    @staticmethod
    def validate_login(phone_number: str, ID: str, supermarket: Supermarket):
        """
        Validates the login credentials, returns the user, user can be either of employee or client type, or could be null
        """
        user = supermarket.find_user(phone_number, ID)
        return user