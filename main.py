import pymysql

import src.admin_interface
import src.scientific_interface
import src.user_interface
import src.utils.database as db
from src.utils.utils import *


def dispatch(option):
    if option == 1:
        f = Figlet(font='slant')
        AI = src.admin_interface.AdminInterface(np)
        AI.loop()
    elif option == 2:
        f = Figlet(font='slant')
        UI = src.user_interface.UserInterface(np)
        UI.loop()
    elif option == 3:
        f = Figlet(font='slant')
        SI = src.scientific_interface.ScientificInterface(np)
        SI.loop()
    else:
        perror("Error: Invalid Option")
        return


print_header('National Park')

global np

while True:
    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        np = db.Database()

        np.open_connection()

        if np.con.open:
            print("Connected to the National Park database")

        else:
            print("Failed to connect")

        tmp = input("Press any key to start")

        with np.con.cursor() as np.cur:
            while True:
                tmp = sp.call('clear', shell=True)
                print("Select the interface  you want to access")
                print("1. Admin Interface")
                print("2. User Interface")
                print("3. Scientific Interface")
                choice = int(input('>>> '))
                if syntax.validate_range(choice, 1, 3):
                    tmp = sp.call('clear', shell=True)
                    dispatch(choice)
                    tmp = input("Enter any key to CONTINUE> ")
                    if tmp == 'exit':
                        break

    except pymysql.err.OperationalError as e:
        print(e.args[0], ':', e.args[1])
        tmp = input(">>>")
