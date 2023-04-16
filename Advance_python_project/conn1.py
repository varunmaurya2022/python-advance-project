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
sql='CREATE TABLE student2(stuid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),roll INT,fees FLOAT)'
myc=conn.cursor()
myc.execute(sql)
myc.close()
conn.close()
