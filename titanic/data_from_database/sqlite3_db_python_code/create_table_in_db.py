import sqlite3

connection = sqlite3.connect("classroomDB.db")
cursor = connection.cursor()

create_table = """
                CREATE TABLE classroom (
                student_id INTEGER PRIMARY KEY,
                name VARCHAR(20),
                gender CHAR(1),
                physics_marks INTEGER,
                chemistry_marks INTEGER,
                mathematics_marks INTEGER
                );"""

cursor.execute(create_table)
connection.commit()
connection.close()
