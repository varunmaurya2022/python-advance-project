import mysql.connector
try:
    con=mysql.connector.connect(
    user='root',
    password='varun321',
    host='localhost',
    database='pdb',
    port=3306
    )
    if (con.is_connected()):
        print("connecsted")
except:
    print("Unable to connect")
con.close()
    
