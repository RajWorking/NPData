class Employee:
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

    def hire(self):
        print("Enter new Employee's details: ")
        self.emp_id = int(input("Employee ID: "))
        self.emp_Name = input("Name: ").lower()
        self.gender = input("Gender: ").lower()
        self.emp_email = input("Email: ").lower()
        self.date_of_birth = input("Birth Date (YYYY-MM-DD): ")
        self.date_of_joining = input("Joining Date (YYYY-MM-DD): ")
        self.role = input("Occupation: ").lower()
        self.works_for_dno = int(input("Department Number: "))
        self.national_park = int(input("National Park code: "))

        query = """INSERT INTO Employee(emp_id, emp_Name, gender, emp_email,date_of_birth,
         date_of_joining, role, works_for_dno, national_park)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (self.emp_id, self.emp_Name, self.gender, self.emp_email, self.date_of_birth,
                  self.date_of_joining, self.role, self.works_for_dno, self.national_park)
        print(query, values)
        return [query, values]
