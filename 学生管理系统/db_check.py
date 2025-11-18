import pymysql

# 直接连接数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='qwe123',
    database='student',
    charset='utf8'
)

cursor = conn.cursor()

# 查看techer_class_infos表结构
print('=== techer_class_infos表结构 ===')
cursor.execute('DESC techer_class_infos')
for field in cursor.fetchall():
    print(field)

# 查看前5条数据
print('\n=== techer_class_infos前5条数据 ===')
cursor.execute('SELECT * FROM techer_class_infos LIMIT 5')
for row in cursor.fetchall():
    print(row)

# 查看students_decision_infos表结构
print('\n=== students_decision_infos表结构 ===')
cursor.execute('DESC students_decision_infos')
for field in cursor.fetchall():
    print(field)

# 查看前5条数据
print('\n=== students_decision_infos前5条数据 ===')
cursor.execute('SELECT * FROM students_decision_infos LIMIT 5')
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
