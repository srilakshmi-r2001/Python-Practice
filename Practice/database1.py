class MyDatabase:
    def dbconn():
        import mysql.connector
        db = mysql.connector.connect(host = "127.0.0.1", user = "username", password = "password")
        cur = db.cursor()

        cur.execute("CREATE DATABASE employee")
        print("Database has been created")
        cur.execute("SHOW DATABASES")
        print(cur.fetchall())

        db.close()

mydb = MyDatabase
mydb.dbconn()