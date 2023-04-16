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
sql='DELETE FROM student where stuid=5'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'row Deleted')
except:
    conn.rollback()
    print("Unable to Delete  Data")
myc.close()
conn.close()
