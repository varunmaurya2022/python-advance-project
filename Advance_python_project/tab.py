import mysql.connector
try:
    con=mysql.connector.connect(
    user='root',
    password='varun321',
    host='localhost',
    database='personal',
    port=3306
    )
    if (con.is_connected()):
        print("connected")
except:
    print("Unable to connect")
sql='SHOW TABLES'
#(stuid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), roll INT,fees FLOAT )'
myc=con.cursor()
myc.execute(sql)
for t in myc:
    print(t)
myc.close()
con.close()

