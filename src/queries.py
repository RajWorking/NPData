import src.utils.syntax_check as syntax
from src.utils.utils import repeat_and_error, perror, psuccess


class Queries():

    def __init__(self):
        self.np = None
        self.des_rating = None
        self.booking_id = None
        self.year_range = None
        self.researcher_name = None
        self.study_type = None

    def get_np(self):
        self.np = input("Enter Code of National Park: ")
        return perror("Code cannot be empty") if syntax.empty(self.np) else True

    def get_rating(self):
        self.des_rating = float(input("Enter Desired Value of Rating: "))
        return True

    def get_booking_id(self):
        self.booking_id = int(input("Enter Booking ID to delete: "))
        return True

    def get_year_range(self):
        self.year_range = input("Enter period in years (YYYY-YYYY): ")
        return True

    def get_researcher_name(self):
        self.researcher_name = input("Enter the Name of the Researcher: ").lower()
        return perror("Name cannot be empty") if syntax.empty(self.researcher_name) else True

    def get_study_type(self):
        self.study_type = input("Enter the Type of Study: ").lower()
        return perror("Name cannot be empty") if syntax.empty(self.study_type) else True

    def generateReport(self):
        repeat_and_error(self.get_np)()
        query = ["SELECT genus, `specific_name`, abundance, total_population FROM" \
                 " Demography D, Presence P WHERE D.presence_id = P.presence_id and " \
                 "P.national_park = '{}'".format(self.np)]
        print(query)
        return query

    def retrieveFeatures(self):
        repeat_and_error(self.get_np)()
        query = ["SELECT feature_name, availability, avg(rating) " \
                 "from Features A, Feature_Feedback B where A.feature_id = B.feature_id" \
                 " and A.feature_id in" \
                 " { SELECT feature_id from `ZONE` C , ZONE_CONTAINS D" \
                 " where C.zone_number = D.zone_number and C.belongs_to = '{}' }" \
                 " GROUP BY B.feature_id having" \
                 " avg(rating) >= '{}'".format(self.np, self.des_rating)]

        print(query)
        return query

    def retreiveServices(self):
        repeat_and_error(self.get_np)()
        query = ["SELECT service_id, name, sum(price) " \
                 "from Booking_service A, Service_timings B, Services C " \
                 "where A.sub_service_id = B.sub_service_id and " \
                 "B.service_id = C.service_id and C.provided_by = '{}'" \
                 " GROUP BY B.service_id ORDER BY sum(price) DESC".format(self.np)]
        print(query)
        return query

    def performCancellation(self):
        repeat_and_error(self.get_booking_id)()

        query = ["DELETE FROM Booking where booking_id = '{}'".format(self.booking_id)]
        print(query)
        return query

    def getDemographyOfPeriod(self):
        repeat_and_error(self.get_year_range)()
        y1, y2 = self.year_range.split('-')

        query = ["SELECT * from Demography where time_stamp > '{}-01-01'"
                 " and time_stamp < '{}-12-31'".format(y1, y2)]
        print(query)
        return query

    def getStudyByNP(self):
        repeat_and_error(self.get_np)()
        query = [
            "SELECT A.study_id, A.researcher, A.type, A.start_date, C.* from "
            "Study A, Study_data B, Data C where A.national_park = '{}'" \
            " and A.study_id = B.study_id and B.data_id = C.data_id ".format(self.np)]
        print(query)
        return query

    def getStudyByResearcher(self):
        repeat_and_error(self.get_researcher_name)()
        query = ["SELECT A.*,  C.* from Study A, Study_data B, Data C, Researcher D where" \
                 " A.researcher = D.researcher_id and D.name = '{}' and A.study_id = B.study_id " \
                 "and B.data_id = C.data_id".format(self.researcher_name)]
        print(query)
        return query

    def getStudyByType(self):
        repeat_and_error(self.get_study_type)()
        query = ["SELECT A.*,  C.* from Study A, Study_data B, Data C where" \
                 " A.study_id = B.study_id and B.data_id = C.data_id" \
                 " and A.type = '{}'".format(self.study_type)]
        print(query)
        return query
