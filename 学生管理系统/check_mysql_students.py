import pymysql
# 使用pymysql.connect方法连接本地mysql数据库
db = pymysql.connect(host='192.168.6.88', port=3306, user='root',
                     password='123456', database='student', charset='utf8')
# 操作数据库，获取db下的cursor对象
cursor = db.cursor()
# 执行SQL查询
cursor.execute('SELECT * FROM students_infos')
# 获取查询结果
students = cursor.fetchall()
print("学生数据:")
for student in students:
    print(student)
# 关闭数据库连接
db.close()