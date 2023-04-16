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
sql='INSERT INTO student(name,roll,fees) VALUES ("Sumit",101,2000.5) '
myc=conn.cursor()
myc.execute(sql)
conn.commit()
myc.close()
conn.close()
