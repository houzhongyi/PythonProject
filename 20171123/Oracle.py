#coding:utf-8
import cx_Oracle

def Connectdb():
    print("Connecting...")
    db=cx_Oracle.connect('scott/tiger@localhost/orcl')
    print("Success!!")
    return db

def CreateStu(db):
    cursor = db.cursor()
    # cursor.execute("DROP TABLE STUDENT")
    sql = """CREATE TABLE STUDENT (
            ID INT,
            NAME VARCHAR (100),
            GRADE VARCHAR (100))
        """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)


def Insertdb(db):
    cursor = db.cursor()
    #oracle怎么一次性插入多行？？？？？？？？？？？？？？
    sql = """INSERT INTO STUDENT VALUES (1, 'A', '10');
              INSERT INTO STUDENT VALUES (2, 'B', '20');
              INSERT INTO STUDENT VALUES (3, 'C', '30');
              INSERT INTO STUDENT VALUES (4, 'D', '40');
              INSERT INTO STUDENT VALUES (5, 'E', '50');
              INSERT INTO STUDENT VALUES (6, 'F', '60');
              INSERT INTO STUDENT VALUES (7, 'G', '70');
              INSERT INTO STUDENT VALUES (8, 'H', '80');"""
    try:
        print(sql)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        #Rollback in case there is any error
        print(e)
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
    # CreateStu(db)
    # Insertdb(db)
    Querydb(db)

if __name__ == '__main__':
    main()