class User:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.email = None
        self.password = None
        self.contact_number = None

    def hire(self):
        print("Enter new User's details: ")
        self.user_id = int(input("User ID: "))
        self.username = input("Name: ").lower()
        self.email = input("Email: ").lower()
        self.password = input("Password: ").lower()
        self.contact_number = input("Contact Number: ")

        query = """INSERT INTO User(user_id, username, email, password,contact_number)
          VALUES (%s, %s, %s, %s, %s)"""

        values = (self.user_id, self.username, self.email, self.password, self.contact_number)
        print(query, values)
        return [query, values]
