import src.utils.syntax_check as syntax
from src.utils.utils import repeat_and_error, perror, psuccess


# password should be crypted

class User:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.email = None
        self.password = None
        self.contact_number = None

    def get_id(self):
        self.user_id = int(input("Enter User ID: "))
        return True

    def get_name(self):
        self.username = input("Enter Username: ").lower()
        return perror("Username cannot be empty") if syntax.empty(self.username) else True

    def get_email(self):
        self.email = input("Enter the email of the user: ").lower()
        return perror("Invalid email") if not syntax.validate_email(self.email) else True

    def get_password(self):
        self.password = input("Enter Password: ")
        return perror("Password cannot be empty") if syntax.empty(self.password) else True

    def get_contact(self):
        self.contact_number = input("Enter the Contact Number of the User: ").lower()
        return perror("Invalid Contact Number") if not syntax.validate_phone_number(
            self.contact_number) else True

    def hire(self):
        try:
            repeat_and_error(self.get_id)()
            repeat_and_error(self.get_name)()
            repeat_and_error(self.get_email)()
            repeat_and_error(self.get_password)()
            repeat_and_error(self.get_contact)()

            query = "INSERT INTO User(user_id, username, email, password,contact_number)" \
                    "VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                self.user_id, self.username, self.email, self.password, self.contact_number)
            print(query)
            return query

        except ValueError as e:
            print(e.args[0])
