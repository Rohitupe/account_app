import sqlite3
try:
    db_conn = sqlite3.connect('Home.db')
    cursor = db_conn.cursor()
except:
    print("no connection")                                                 
finally:
    print("connected")
    try:
        # cursor.execute("""CREATE TABLE user(name VARCHAR(200))""")
        print("table created")
    except:
        print("problem")
    finally:
        print("done")
        cursor.execute("""DROP TABLE user""")