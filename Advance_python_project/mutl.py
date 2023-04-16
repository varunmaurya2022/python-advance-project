import mysql.connector
def student_data(n,r,f):
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
        print("Unable to Connect")
sql='INSERT INTO student(name,roll,fees)VALUES(%s,%s,%s)'
myc=conn.cursor()
try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount,"Row Inserted")
    print(f' Stu Id:{stuid} Insreted')
except:
    conn.rollback()
    print("Unable To Insert Data")
myc.close()
conn.close()
while True:
    nm=input("Enter Name:")
    ro=int(input("Enter Roll :"))
    fe=float(input("Enter Fees :"))
    params=(nm,ro,fe)
    ans=input("Do ypu Want to exit?(y/n)")
    if ans==y:
        break;
