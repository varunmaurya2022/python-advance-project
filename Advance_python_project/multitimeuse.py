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
        print("Unable To Connect")
    sql='INSERT INTO student(name,roll,fees)VALUES(%s,%s,%s)'
    params=(nm,ro,fe)
    myc=conn.cursor()
    try:
        myc.execute(sql,params)
        conn.commit()
        print(myc.rowcount,"Inserts Rows")
        print(f'Stu Id:{myc.lastrowid} Inserted')
    except:
        conn.rollback()
        print("Unable To Inserted Data")
        myc.close()
        conn.close()
while True:
    nm=input("Eneter Name:")
    ro=int(input("Enter Roll Number:"))
    fe=float(input("Eneter Fees:"))
    student_data(nm,ro,fe)
    ans=input('Do you want to exit?(y/n)')
    if ans==y:
        break

        
        
    
    
    
