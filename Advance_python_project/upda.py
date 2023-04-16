import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='varun321',
        host='localhost',
        database='pdb',
        port=3306
        )
    if (conn.is_connected()):
            print("Successfully Connected")
except:
    print("Unable To Connect")
sql='UPDATE student SET fees=383.1 WHERE stuid=11'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'row Updated')
    print(myc.lastrowid,'last row ID')
except:
    conn.rollback()
    print("Unable to Update  Data")
myc.close()
conn.close()
