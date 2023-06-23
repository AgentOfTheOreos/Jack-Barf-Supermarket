from DataModels.Persons.Employees.Employee import Employee


class HeadManager(Employee):
    def __init__(self, ID: str, full_name: str, phone_number: str, employee_number: str,
                 shift_type: str, years_of_experience: int, department: str):
        super().__init__(ID, full_name, phone_number, employee_number, shift_type)
        self._years_of_experience = years_of_experience
        self._department = department

    @property
    def subclass_identifier(self):
        return "HeadManager"

    # Getters
    def get_years_of_experience(self):
        return self._years_of_experience

    def get_department(self):
        return self._department

    # Setters
    def set_years_of_experience(self, years_of_experience):
        self._years_of_experience = years_of_experience

    def set_department(self, department):
        self._department = department

    # Overridden __eq__ method
    def __eq__(self, other):
        if isinstance(other, HeadManager):
            return super().__eq__(other) and self._years_of_experience == other._years_of_experience and \
                   self._department == other._department
        return False

    # Overridden __str__ method
    def __str__(self):
        employee_str = super().__str__()  # Get the string representation from the parent class
        return f"{employee_str}, Years of Experience: {self._years_of_experience}, \n" \
               f"Department: {self._department}\n"
