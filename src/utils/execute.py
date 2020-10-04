

def execute_query(query):

    for qr in query:
        try:
            cur.execute(qr)
            rows = cur.fetchall()
            for row in rows:
                print(row)
            print("Inserted Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to insert into database")
            print(">>>>>>>>>>>>>", e)