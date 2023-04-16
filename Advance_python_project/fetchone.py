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
sql='SELECT * FROM student'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'row inserted')
    print(myc.lastrowid,"Last Row Id")
except:
    conn.rollback()
    print("Unable to Insert Data")
try:
    myc.execute(sql)
    row=myc.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()
    print("Total Rows:",myc.rowcount)
except:
    conn.rollback()
    print('Unable to show data')
    
myc.close()
conn.close()
