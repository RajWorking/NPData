import subprocess as sp
import pymysql.cursors
import config

from src.Employee import Employee
from src.Department import Department
from src.User import User
from src.Services import *
from src.Feedback import Feedback
from src.queries import *


def fetch_query(query):
    for qr in query:
        try:
            cur.execute(qr)
            rows = cur.fetchall()
            for row in rows:
                print(row)
            print("Fetched from Database")
        except Exception as e:
            con.rollback()
            print("Failed to fetch from database")
            print(">>>>>>>>>>>>>", e)


def insert_query(query):
    for qr in query:
        try:
            cur.execute(qr)
            cur.commit()
            print("Inserted into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)


def delete_query(query):
    for qr in query:
        try:
            cur.execute(qr)
            cur.commit()
            print("Deleted from Database")
        except Exception as e:
            con.rollback()
            print("Failed to delete from database")
            print(">>>>>>>>>>>>>", e)


def dispatch(option):
    if option == 1:
        query = Employee().hire()
    elif option == 2:
        query = Queries().generateReport()
        fetch_query(query)
    elif option == 3:
        query = Queries().getDemographyOfPeriod()
        fetch_query(query)
    elif option == 4:
        query = Queries().performCancellation()
        delete_query(query)
    elif option == 5:
        query = Queries().getStudyByNP()
        fetch_query(query)
    elif option == 6:
        query = Queries().getStudyByResearcher()
        fetch_query(query)
    elif option == 7:
        query = Queries().getStudyByType()
        fetch_query(query)
    elif option == 8:
        query = Feedback("service").add()
        insert_query(query)
    elif option == 9:
        query = Feedback("feature").add()
        insert_query(query)
    elif option == 10:
        query = ServiceTimings().add()
    elif option == 11:
        query = Department.remove()
    else:
        print("Error: Invalid Option")
        return


while True:
    tmp = sp.call('clear', shell=True)

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(
            host='localhost',
            user=config.username,
            password=config.password,
            database=config.db,
            port=config.port,
            cursorclass=pymysql.cursors.DictCursor
        )
        tmp = sp.call('clear', shell=True)

        if con.open:
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE> ")

        with con.cursor() as cur:
            while (1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Hire an Employee ")
                print("2. Get Report of National Park")
                print("3. Retrieve Demography of a period")
                print("4. Perform a Booking Cancellation")
                print("5. Retrieve studies of a National Park")
                print("6. Retrieve studies done by Researcher")
                print("7. Retrieve various type of studies")
                print("8. Add a feedback for a service")
                print("9. Add a feedback for a feature")
                print("10. Add timings for service")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch >= 100:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE> ")



    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused")
        tmp = input("Enter any key to CONTINUE> ")
