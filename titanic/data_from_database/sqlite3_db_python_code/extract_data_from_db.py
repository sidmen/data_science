import sqlite3

connection = sqlite3.connect("classroomDB.db")
cursor = connection.cursor()
query = "SELECT * FROM classroom"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

connection.close()
