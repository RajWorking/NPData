import subprocess as sp
import pymysql.cursors
import config

from src.Employee import Employee
from src.Department import Department
from src.User import User
from src.Services import Service
from src.Feedback import ServiceFeedback, FeatureFeedback

def execute_query(query):
    try:
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)


def dispatch(option):
    if option == 1:
        query = Employee().hire()
    elif option == 2:
        query = Department().add()
    elif option == 3:
        query = User().hire()
    elif option == 4:
        query = Service().add()
    elif option == 8:
        query = ServiceFeedback().add()
    elif option == 9:
        query = FeatureFeedback().add()
    elif option == 11:
        query = Department.remove()
    else:
        print("Error: Invalid Option")
        return

    execute_query(query)


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
                print("2. Add a new Department")
                print("3. Hire a User")
                print("4. Add a new Service")
                print("8. Add a feedback for a service")
                print("9. Add a feedback for a feature")
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
