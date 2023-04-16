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
sql='INSERT INTO student(name, roll, fees) VALUES ("Arun",109,7673.1)'
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'row inserted')
    print(myc.lastrowid,"Last Row Id")
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()
