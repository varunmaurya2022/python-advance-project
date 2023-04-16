import mysql.connector
try:
    conn=mysconn=mysql.connector.connect(user='root',password='varun321',host='localhost',port=3306)
    print(conn.is_connected())
    print("Connected")
except:
    print('Unable to Connect')
conn.close()
