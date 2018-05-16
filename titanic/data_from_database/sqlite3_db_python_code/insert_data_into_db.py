import sqlite3


classroom_data = [(1, "Raj", "M", 70, 84, 92), (2, "Poonam", "F", 87, 69, 93),
                  (3, "Nik", "M", 65, 83, 90), (4, "Rahul", "M", 83, 76, 89)]

connection = sqlite3.connect("classroomDB.db")
cursor = connection.cursor()

for student in classroom_data:
    insert_statement = """INSERT INTO classroom (student_id, name, gender, physics_marks, chemistry_marks, mathematics_marks) VALUES ({0}, "{1}", "{2}", {3}, {4}, {5});""".format(
        student[0], student[1], student[2], student[3], student[4], student[5])
    cursor.execute(insert_statement)
    connection.commit()


connection.close()
