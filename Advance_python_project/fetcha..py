import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='varun321',
        host='localhost',
        database='varun',
        port=3306
        )
    if (conn.is_connected()):
            print("Successfully Connected")
except:
    print("Unable To Connect")
sql='SELECT * FROM personal'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'row inserted')
    print(myc.lastrowid,"Last Row Id")
except:
    conn.rollback()
try:
    myc.execute(sql)
    rows=myc.fetchall()
    for i in rows:
        print(i)
        row=myc.fetchone()
    print("Total Rows:",rowcount)
    print(f'Stuid:{stuid} Name:{name} Roll:{roll} Fees:{fees}')
    
except:
    conn.rollback()
    print('Unable to show data')
    
myc.close()
conn.close()
