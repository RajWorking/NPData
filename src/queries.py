import src.utils.syntax_check as syntax
from src.utils.utils import repeat_and_error, perror, psuccess


class getReportOfSpeciesOfNationalPark:

    def __init__(self):
        self.np = None

    def get_np(self):
        self.np = int(input("Enter Code of National Park: "))
        return True

    def generateReport(self):
        repeat_and_error(self.get_np)()

        query = "SELECT genus, specific_name, abundance, percent_of_population FROM" \
                " Demography D, Presence P WHERE D.presence_id = P.presence_id and " \
                "P.national_park = '{}'".format(self.np)

        print(query)


class getFeaturesWithRating:

    def __init__(self):
        self.np = None
        self.des_rating = None

    def get_np(self):
        self.np = int(input("Enter Code of National Park: "))
        return True

    def get_rating(self):
        self.des_rating = float(input("Enter Desired Value of Rating: "))
        return True

    def get_features(self):
        repeat_and_error(self.get_np)()

        query = "SELECT feature_name, availability, avg(rating) " \
                "from Features A, Feature_Feedback B where A.feature_id = B.feature_id" \
                " and A.feature_id in" \
                " { SELECT feature_id from ZONE C , ZONE_CONTAINS D" \
                " where C.zone_number = D.zone_number and C.belongs_to = '{}' }" \
                " GROUP BY B.feature_id having" \
                " avg(rating) >= '{}'".format(self.np, self.des_rating)

        print(query)


class getHighestEarningServices:

    def __init__(self):
        self.np = None

    def get_np(self):
        self.np = int(input("Enter Code of National Park: "))
        return True

    def get_services(self):
        repeat_and_error(self.get_np)()


        query = "SELECT service_id, name, sum(price) " \
                "from Booking_service A, Service_timings B, Services C " \
                "where A.sub_service_id = B.sub_service_id and " \
                "B.service_id = C.service_id and C.provided_by = '{}'" \
                " GROUP BY B.service_id ORDER BY sum(price) DESC".format(self.np)
        print(query)
