import mysql.connector
try:
    conn=mysql.connector.connect(user='root',password='varun321',host='localhost',port=3306)
    if (conn.is_connected()):
        print('connected')
except:
    print('Unable to Connect')
myc=conn.cursor()

myc.execute('CREATE DATABASE pdb')
for d in myc:
    print(d)
myc.close()
conn.close()
