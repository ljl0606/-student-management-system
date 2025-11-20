import sqlite3
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM students_infos')
students = cursor.fetchall()
print("学生数据:")
for student in students:
    print(student)
conn.close()