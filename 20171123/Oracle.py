# coding=utf-8
import cx_Oracle
db=cx_Oracle.connect('scott/tiger@localhost/orcl')
cr = db.cursor() #创建cursor
sql = 'select * from emp where SAL >= 3000'
cr.execute(sql)
rs = cr.fetchall()
print "print all: (%s)" %rs
for x in rs:
    print x
#一次返回一行 fetchone
print 'fetchone:'
cr.execute(sql)

db.close()