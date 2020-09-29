class Department:
    def __init__(self):
        self.dep_number = None
        self.dep_name = None
        self.contained_in = None
        self.is_chaired_by = None

    def add(self):
        print("Enter new Department's details: ")
        self.dep_number = int(input("Department Number: "))
        self.dep_name = input("Department Name: ")
        self.contained_in = int(input("Present in which National Park: "))
        self.is_chaired_by = int(input("Supervisor: "))

        query = """INSERT INTO Department(dep_number, dep_name, contained_in, is_chaired_by)
         VALUES (%s, %s, %s, %s)"""
        values = (self.dep_number, self.dep_name, self.contained_in, self.is_chaired_by)
        print(query, values)
        return [query, values]

    def remove(self):
        print("Enter Department's details for removal: ")
        self.dep_number = int(input("Department Number: "))
        self.contained_in = int(input("Present in which National Park: "))

        query = """DELETE from Department WHERE (contained_in = %s and dep_number = %s)"""
        values = (self.contained_in, self.dep_number)
        print(query, values)
        return [query, values]

