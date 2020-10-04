import src.utils.syntax_check as syntax
from src.utils.utils import *
import datetime


class Query:

    def __init__(self):
        self.national_park = None
        self.genus = None
        self.specific_name = None
        self.newvalue = None
        self.ch = 0

    def get_np(self):
        self.national_park = input("Enter unitcode of National Park: ")
        return True

    def get_genus(self):
        self.genus = input("Enter genus of species: ")
        return True

    def get_specific_name(self):
        self.specific_name = input("Enter specific name of species: ")
        return True

    options = [
        'total_population',
        'average_lifespan'
    ]

    def get_newvalue(self):
        self.newvalue = int(input("Enter updated value: "))
        return True

    def show_options(self):
        for i in range(len(self.options)):
            print('{}. {}'.format(i + 1, self.options[i]))

    def get_option(self):
        self.ch = int(input("What do you want to update: "))
        return True

    def Update_demography(self):
        repeat_and_error(self.get_np)()
        repeat_and_error(self.get_genus)()
        repeat_and_error(self.get_specific_name)()
        repeat_and_error(self.get_option, self.show_options)()
        repeat_and_error(self.get_newvalue)()

        query = """
                    UPDATE Demography 
                    SET {} = {}, time_stamp = '{}' WHERE presence_id IN
                    (SELECT presence_id FROM Presence WHERE 
                    national_park = '{}' AND genus = '{}' AND specific_name = '{}')
                """.format(self.options[self.ch - 1], self.newvalue,
                           datetime.datetime.now(), self.national_park,
                           self.genus, self.specific_name)

        print(query)
        return [query]


    def Find_national_parks_of_species(self):
        repeat_and_error(self.get_genus)()
        repeat_and_error(self.get_specific_name)()

        query = """
                    SELECT * FROM National_Park N, Presence P
                    WHERE N.unit_code = P.national_park 
                    AND genus LIKE '%{}%' AND specific_name LIKE '%{}%'
                """.format(self.genus, self.specific_name)

        print(query)
        return [query]
