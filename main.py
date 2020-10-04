import subprocess as sp
import pymysql.cursors
import config

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
        query = Query().Update_demography()
        insert_query(query)
    elif option == 2:
        query = Query().Find_national_parks_of_species()
        fetch_query(query)
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
                print("1. Update Demography ")
                print("2. Get National Parks of a species")
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