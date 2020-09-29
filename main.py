import pymysql.cursors

import config
import src.insert as ins

while True:

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

        ins.insert_species()

        if con.open:
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input(">>>")
    except:
        print("Error occurred")
        tmp = input(">>>")
