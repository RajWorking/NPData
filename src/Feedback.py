class ServiceFeedback:
    def __init__(self):
        self.feature_id = None
        self.user_id = None
        self.rating = None
        self.remarks = None
        self.date = None

    def add(self):
        print("Please provide the details of feedback: ")
        self.service_id = input("Service ID: ")
        self.user_id = int(input("User ID: "))
        self.rating = float(input("Rating: "))
        self.remarks = input("Remarks: ")
        self.date = input("Date (YYYY-MM-DD): ")

        query = """INSERT INTO Service_Feedback(service_id, user_id, rating, remarks, date)
          VALUES (%s, %s, %s, %s, %s)"""
        values = (self.service_id, self.user_id, self.rating, self.remarks, self.date)

        print(query, values)
        return [query, values]


class FeatureFeedback:
    def __init__(self):
        self.feature_id = None
        self.user_id = None
        self.rating = None
        self.remarks = None
        self.date = None

    def add(self):
        print("Please provide the details of feedback: ")
        self.feature_id = input("Feature ID: ")
        self.user_id = int(input("User ID: "))
        self.rating = float(input("Rating: "))
        self.remarks = input("Remarks: ")
        self.date = input("Date (YYYY-MM-DD): ")

        query = """INSERT INTO Feature_Feedback(feature_id,user_id, rating, remarks, date)
          VALUES (%s, %s, %s, %s, %s)"""
        values = (self.feature_id, self.user_id, self.rating, self.remarks, self.date)

        print(query, values)
        return [query, values]
