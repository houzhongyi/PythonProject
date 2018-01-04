#encoding:utf-8
import pymysql

def Connectdb():
    print("connecting...")
    db = pymysql.connect("localhost","root","123456","TestDb")
    print("success!!")
    return db

def Createtable(db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Student")
    sql = """CREATE TABLE STUDENT (
          ID VARCHAR (10) NOT NULL,
          NAME VARCHAR (100),
          GRADE INT (10))"""
    cursor.execute(sql)
    db.commit()

def Insertdb(db):
    cursor = db.cursor()
    sql = """INSERT INTO STUDENT
            VALUES ('001', 'A', 10),
                   ('002', 'B', 20),
                   ('003', 'C', 30),
                   ('004', 'D', 40),
                   ('005', 'E', 50),
                   ('006', 'F', 60),
                   ('007', 'G', 70),
                   ('008', 'H', 80)"""
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        #Rollback in case there is any error
        print(e)
        print('插入失败！')
        db.rollback()


def Querydb(db):
    cursor = db.cursor()
    sql = "SELECT * FROM STUDENT"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        for row in results:
            ID = row[0]
            Name = row[1]
            Grade = row[2]
            print("ID: %s, Name: %s, Grade: %s" %(ID, Name, Grade))
    except:
        print("Error: unable to fetch data")

def main():
    db = Connectdb()
    # Createtable(db)
    # Insertdb(db)
    Querydb(db)


if __name__ == '__main__':
    main()