import src.utils.syntax_check as syntax
from src.utils.utils import repeat_and_error

# still doesnot work for empty line in int
# gender options 4 option is true

class Employee:
    gender_enum = [
        'Male',
        'Female',
        'Others'
    ]

    def __init__(self):
        self.emp_id = None
        self.emp_Name = None
        self.gender = None
        self.emp_email = None
        self.date_of_birth = None
        self.date_of_joining = None
        self.role = None
        self.works_for_dno = None
        self.national_park = None

    def get_id(self):
        self.emp_id = input("Enter Employee ID: ")
        return print("ID cannot be empty") if syntax.empty(self.emp_id) else True

    def get_name(self):
        self.emp_Name = input("Enter the Name of the Employee: ")
        return print("Name cannot be empty") if syntax.empty(self.emp_Name) else True

    def get_gender_options(self):
        print("Choose one among the genders: ")
        for i in range(len(self.gender_enum)):
            print('{}. {}'.format(i + 1, self.gender_enum[i]))

    def get_gender(self):
        self.gender = int(input('Choosing the following for gender of Employee: '))
        self.gender -= 1
        return print("Gender must be from one of the options") if not syntax.validate_range(
            self.gender, 0, len(self.gender_enum)) else True

    def get_email(self):
        self.emp_email = input("Enter the email of the Employee: ")
        return print("Invalid email") if not syntax.validate_email(self.emp_email) else True

    def get_dob(self):
        self.date_of_birth = input("Enter Birth Date (YYYY-MM-DD): ")
        return print("Invalid Date") if not syntax.validate_date(self.date_of_birth) else True

    def get_doj(self):
        self.date_of_joining = input("Enter Date Of Joining (YYYY-MM-DD): ")
        return print("Invalid Date") if not syntax.validate_date(self.date_of_joining) else True

    def get_role(self):
        self.role = input("Enter Role of Employee: ")
        return print("Role cannot be empty") if syntax.empty(self.role) else True

    def get_dno(self):
        self.works_for_dno = input("Enter Department Number for above employee: ")
        return print("Department Number cannot be empty") if syntax.empty(
            self.works_for_dno) else True

    def get_national_park(self):
        self.national_park = input("Enter the Code of National Park in which the employee works: ")
        return print("Unit code cannot be empty") if syntax.empty(self.national_park) else True

    def hire(self):
        print("Enter new Employee's details: ")

        try:
            repeat_and_error(self.get_id, None)()
            repeat_and_error(self.get_name, None)()
            repeat_and_error(self.get_gender, self.get_gender_options)()
            repeat_and_error(self.get_email, None)()
            repeat_and_error(self.get_dob, None)()
            repeat_and_error(self.get_doj, None)()
            repeat_and_error(self.get_role, None)()
            repeat_and_error(self.get_dno, None)()
            repeat_and_error(self.get_national_park, None)()

            query = "INSERT INTO Employee(emp_id, emp_Name, gender, emp_email,date_of_birth, " \
                    "date_of_joining, role, works_for_dno, national_park)" \
                    "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                self.emp_id, self.emp_Name,
                self.gender, self.emp_email, self.date_of_birth,
                self.date_of_joining, self.role, self.works_for_dno, self.national_park)

            print(query)
            return query

        except ValueError as e:
            print(e.args[0])
