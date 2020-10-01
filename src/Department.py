import src.utils.syntax_check as syntax
from src.utils.utils import repeat_and_error, perror, psuccess


class Department:
    def __init__(self):
        self.dep_number = None
        self.dep_name = None
        self.contained_in = None
        self.is_chaired_by = None

    def get_dep_number(self):
        self.dep_number = int(input("Enter Department Number: "))
        return True

    def get_dep_name(self):
        self.dep_name = input("Enter the Name of the Service: ").lower()
        return perror(" Department Name cannot be empty") if syntax.empty(self.dep_name) else True

    def get_national_park(self):
        self.contained_in = int(
            input("Enter the Code of National Park in which the Department is present: "))
        return True

    def get_supervisor(self):
        self.is_chaired_by = int(input("Enter the ID of Supervisor: "))
        return True

    def add(self):
        try:
            repeat_and_error(self.get_dep_number)()
            repeat_and_error(self.get_dep_name)()
            repeat_and_error(self.get_national_park)()
            repeat_and_error(self.get_supervisor)()

            query = "INSERT INTO Department(dep_number, dep_name, contained_in, is_chaired_by)" \
                    "VALUES ('{}', '{}', '{}', '{}')".format(
                self.dep_number, self.dep_name, self.contained_in, self.is_chaired_by)
            print(query)
            return query
        except ValueError as e:
            print(e.args[0])

    def remove(self):
        print("Enter Department's details for removal: ")
        self.dep_number = int(input("Department Number: "))
        self.contained_in = int(input("Present in which National Park: "))

        query = """DELETE from Department WHERE (contained_in = %s and dep_number = %s)"""
        values = (self.contained_in, self.dep_number)
        print(query, values)
        return [query, values]
