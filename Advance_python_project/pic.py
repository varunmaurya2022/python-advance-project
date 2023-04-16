import pickle,stu
n=int(input("Enter number of students:"))
with open("student.dat",mode="wb") as f:
    for i in range(n):
        name=input("Enter Student Name:")
        roll=int(input("Enter Roll Number:"))
        age=int(input("Enter Age:"))
        address=input("Enter The Address:")
        
        stu1=stu.Student(name,roll,age,address)
    pickle.dump(stu1,f)
    print("Pickling Done!")