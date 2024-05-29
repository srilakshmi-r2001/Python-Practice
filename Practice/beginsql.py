import mysql.connector

db = mysql.connector.connect(host="localhost", user="root",
                              passwd="root", database="testdb")

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person (PersonID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(30), Age SMALLINT UNSIGNED)")
#mycursor.execute("DESCRIBE Person")
#mycursor.execute("INSERT INTO Person(name, age) VALUES(%s,%s)",("Sri",22))
#db.commit()

mycursor.execute("SELECT * FROM Person")

for i in mycursor:
    print(i)