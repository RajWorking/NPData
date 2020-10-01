import src.utils.syntax_check as syntax
from src.utils.utils import repeat_and_error, perror, psuccess


class Service:
    def __init__(self):
        self.service_id = None
        self.name = None
        self.availability = None
        self.capacity = None
        self.price = None
        self.description = None
        self.provided_by = None

    def get_id(self):
        self.service_id = int(input("Enter Service ID: "))
        return True

    def get_name(self):
        self.name = input("Enter the Name of the Service: ").lower()
        return perror("Name cannot be empty") if syntax.empty(self.name) else True

    def get_availability(self):
        self.availability = int(input("Enter the Availability of Service: "))
        return True

    def get_capacity(self):
        self.capacity = int(input("Enter the Capacity for Service: "))
        return True

    def get_price(self):
        self.price = float(input("Enter the price for Service: "))
        return True

    def get_description(self):
        self.description = input("Enter description of the Service: ").lower()
        return perror("Description cannot be empty") if syntax.empty(self.description) else True

    def get_national_park(self):
        self.provided_by = int(
            input("Enter the Code of National Park: "))
        return True

    def add(self):
        print("Enter details of new Service: ")

        try:
            repeat_and_error(self.get_id)()
            repeat_and_error(self.get_name)()
            repeat_and_error(self.get_availability)()
            repeat_and_error(self.get_capacity)()
            repeat_and_error(self.get_price)()
            repeat_and_error(self.get_description)()
            repeat_and_error(self.get_national_park)()

            query = "INSERT INTO Services(service_id, name, availability, capacity, price,description," \
                    "provided_by) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                self.service_id, self.name, self.availability, self.capacity, self.price,
                self.description, self.provided_by)
            print(query)
            return query
        except ValueError as e:
            print(e.args[0])

    def remove(self):
        print("Enter Service details for removal: ")
        self.service_id = int(input("Service ID: "))
        self.provided_by = int(input("Provided by which National Park: "))

        query = "DELETE from Services WHERE (contained_in = %s and service_id = %s)"
        values = (self.provided_by, self.service_id)
        print(query, values)
        return [query, values]
