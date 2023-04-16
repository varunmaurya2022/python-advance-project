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
        print("Successfully Connected:")
except:
    print('Unable to Connect!')
sql='INSERT INTO student(name,roll,fees) VALUES ("Rohan",102,200.5) '
myc=conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print("Raw Inserted")
except:
    conn.rollback()
    print("Unable to Insert Data")
myc.close()
conn.close()
