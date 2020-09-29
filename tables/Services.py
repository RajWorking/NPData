class Service:
    def __init__(self):
        self.service_id = None
        self.name = None
        self.availability = None
        self.capacity = None
        self.price = None
        self.description = None
        self.provided_by = None

    def add(self):
        print("Enter details of new Service: ")
        self.service_id = int(input("Service ID: "))
        self.name = input("Name: ").lower()
        self.availability = int(input("Availability: "))
        self.capacity = int(input("Capacity: "))
        self.price = float(input("Price: "))
        self.description = input("Description: ").lower()
        self.provided_by = int(input("Provided by which National Park: "))

        query = """INSERT INTO Services(service_id, name, availability, capacity, price,description,
         provided_by)
          VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        values = (self.service_id, self.name, self.availability, self.capacity, self.price,
                  self.description, self.provided_by)
        print(query, values)
        return [query, values]

    def remove(self):
        print("Enter Service details for removal: ")
        self.service_id = int(input("Service ID: "))
        self.provided_by = int(input("Provided by which National Park: "))

        query = "DELETE from Services WHERE (contained_in = %s and service_id = %s)"
        values = (self.provided_by, self.service_id)
        print(query, values)
        return [query, values]
