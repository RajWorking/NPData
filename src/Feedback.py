import src.utils.syntax_check as syntax
from src.utils.utils import repeat_and_error, perror, psuccess


class Feedback:
    def __init__(self, type):
        self.id = {
            "id": None,
            "type": type
        }
        self.user_id = None
        self.rating = None
        self.remarks = None
        self.date = None

    def get_id(self):
        self.user_id = int(input("Enter User ID: "))
        return True

    def get_fs_id(self):
        self.id["id"] = int(input("Enter " + self.id["type"] + " ID: "))
        return True

    def get_rating(self):
        self.rating = float(input("Enter Rating: "))
        return True

    def get_remarks(self):
        self.remarks = input("Enter Remarks: ").lower()
        return perror("Remarks cannot be empty") if syntax.empty(self.remarks) else True

    def get_date(self):
        self.date = input("Enter Date of writing feedback (YYYY-MM-DD): ")
        return perror("Invalid Date") if not syntax.validate_date(self.date) else True

    def add(self):

        print("Please provide the details of feedback: ")

        repeat_and_error(self.get_id)()
        repeat_and_error(self.get_fs_id)()
        repeat_and_error(self.get_rating)()
        repeat_and_error(self.get_remarks)()
        repeat_and_error(self.get_date)()

        query = []
        if self.id["type"] == "feature":
            query.append("INSERT INTO Feature_Feedback(feature_id, user_id, rating, remarks, date)" \
                         "VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                self.id["id"], self.user_id, self.rating, self.remarks, self.date))
        elif self.id["type"] == "service":
            query.append("INSERT INTO Service_Feedback(service_id, user_id, rating, remarks, date)" \
                         "VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                self.id["id"], self.user_id, self.rating, self.remarks, self.date))

        print(query)
        return query
