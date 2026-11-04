'''
	dbhelper
'''
from sqlite3 import connect,Row

database:str = "school.db"

def createDB()->None:
    conn:any = connect(database)
    sql:str = "CREATE TABLE `students`(id integer primary key autoincrement,idno varchar(10) unique, lastname varchar(50),firstname varchar(50),course varchar(10),level varchar(5));"
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def updatestudent(table:str,**kwargs)->None:  
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    newflds:list = []
    for i in range(1,len(vals)):
        newflds.append("`"+keys[i]+"`='"+vals[i]+"'")
    flds:str = ",".join(newflds)
    sql:str = f"UPDATE `{table}` SET {flds} WHERE `{keys[0]}`='{vals[0]}'"
    print(sql)
    conn:any = connect(database)
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True if cursor.rowcount>0 else False


def addstudent(**kwargs)->None:
    keys:list = list(kwargs.keys())
    vals:list = list(kwargs.values())
    fields:str = ",".join(keys)
    data:str = "','".join(vals)
    sql:str = f"INSERT INTO `students`({fields}) VALUES('{data}')"
    print(sql)
    conn:any = connect(database)
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True if cursor.rowcount>0 else False

def getall(table:str)->None:
    sql:str = f"SELECT * FROM `{table}`"
    conn:any = connect(database)
    conn.row_factory = Row
    cursor:any = conn.cursor()
    cursor.execute(sql)
    data:list = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
    
def getrecord(table:str,idno:str)->None:
    sql:str = f"SELECT * FROM `{table}` WHERE `idno`={idno}"
    conn:any = connect(database)
    conn.row_factory = Row
    cursor:any = conn.cursor()
    cursor.execute(sql)
    data:list = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
    
def deleterecord(table:str,idno:str)->None:
    sql:str = f"DELETE FROM `{table}` WHERE `idno`={idno}"
    conn:any = connect(database)
    cursor:any = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True if cursor.rowcount>0 else False


def main()->None:
    #print(addstudent(idno='1002',lastname='charlie',firstname='delta',course='bsit',level='2'))
    students:list = getall('students')
    for student in students:
        print(f"{student['idno']}\t{student['lastname']}\t{student['firstname']}\t{student['course']}\t{student['level']}")
    print(updatestudent('students',idno='1003',lastname='xxxx',firstname='yyyy',course='bsbs',level='2'))
    students:list = getall('students')
    for student in students:
        print(f"{student['idno']}\t{student['lastname']}\t{student['firstname']}\t{student['course']}\t{student['level']}")
if __name__=="__main__":
    main()
