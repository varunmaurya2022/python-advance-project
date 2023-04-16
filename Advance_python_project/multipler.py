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
sql='''INSERT INTO student(name,roll,fees) VALUES ("jai",103,2001.5),
("Arun",104,4000.5),("kajal",105,400.8)'''
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
