import pickle 
class Student:
    def __init__(self,name,roll,age,address):
        self.name=name
        self.roll=roll;
        self.age=age;
        self.address=address;
    def disp(self):
        print(f'Name:{self.name} Roll:{self.roll} Age:{self.age} Address:{self.address}')
with open("Student.dat",mode='wb') as f:
    stu1=Student('Rahul',101,21,'Agra')
    stu2=Student('Amar',102,23,'Farrukhabad')
    pickle.dump(stu1,f)
    pickle.dump(stu2,f)
    print("Pickling Done!")
with open("Student.dat",mode='rb')  as f:
    obj=pickle.load(f)
    obj1=pickle.load(f)
    print("Unpickling Done!")
    obj.disp()
    obj1.disp()
    

    