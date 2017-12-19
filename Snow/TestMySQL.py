import pymysql



# 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
db = pymysql.connect("localhost","root","123456","TESTDB")
cursor = db.cursor()

# cursor.execute("DROP TABLE IF EXISTS Student")
# sql = """CREATE TABLE Student (
#             ID CHAR(10) NOT NULL,
#             Name CHAR(8),
#             Grade INT )"""
# cursor.execute(sql)
# cursor.execute("INSERT INTO STUDENT (ID, Name, Grade) VALUES (1, 'nash', 8)")
try:
    cursor.execute("SELECT * FROM Student")
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        grade = row[2]
        print("id = %s, name = %s, grade = %s" % (id, name, grade))
except:
    print("Error: unable to fetch data")
# 使用 execute()  方法执行 SQL 查询
# a = cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()

# 关闭数据库连接
db.close()


