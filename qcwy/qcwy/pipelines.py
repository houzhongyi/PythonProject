# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import cx_Oracle
from twisted.enterprise import adbapi
from scrapy import signals

class QcwyJsonPipeline(object):
    def __init__(self):
        self.file = open('F:\\Python\\qcwy.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class QcwyOraclePipeline(object):
    def __init__(self):
        self.coonpool = adbapi.ConnectionPool(
            'cx_Oracle',
            'scott',
            'tiger',
            'localhost/orcl'
        )

    def process_item(self, item, spider):
        query = self.coonpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        title = item['title']
        amount = item['amount']
        experience = item['experience']
        education = item['education']
        scale = item['scale']
        link = item['link']
        company = item['company']
        salary = item['salary']
        updatetime = item['updatetime']
        address = item['address']
        jobInfo = item['jobInfo']
        jobUrl = item['jobUrl']
        if item.get('title'):
            tx.execute("insert into QCWY values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)",
                       (title, amount, experience, company, link, scale, salary, updatetime, address, jobInfo, jobUrl, education))

    def handle_error(self, e):
        print(e)


# def Connectdb():
#     db = cx_Oracle.connect('scott/tiger@localhost/orcl')
#     print('Success!')
#     return db
#
# # 数据库创建表
# def CreateStu(db):
#     cursor = db.cursor()
#     # cursor.execute("DROP TABLE STUDENT")
#     sql = """CREATE TABLE STUDENT (
#             ID INT,
#             NAME VARCHAR (100),
#             GRADE VARCHAR (100))
#         """
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except Exception as e:
#         print(e)
#
# # oracle数据库查询
# def Querydb(db):
#     cursor = db.cursor()
#     sql = "SELECT * FROM STUDENT"
#     try:
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         print(results)
#         for row in results:
#             ID = row[0]
#             Name = row[1]
#             Grade = row[2]
#             print("ID: %s, Name: %s, Grade: %s" % (ID, Name, Grade))
#     except:
#         print("Error: unable to fetch data")
#
# # oracle数据库插入数据
# def Insertdb(db):
#     cursor = db.cursor()
#     # oracle怎么一次性插入多行？？？？？？？？？？？？？？
#     sql = """ """
#     try:
#         print(sql)
#         cursor.execute(sql)
#         db.commit()
#     except Exception as e:
#         # Rollback in case there is any error
#         print(e)
#         db.rollback()

