#Passing memeber of one class to anothe class.
class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def disp(self):
        print("Student Name:",self.name)
        print("Student Roll number:",self.roll)
class User:
    @staticmethod
    def show(s):
        print("User Name:",s.name)
        print("User Roll number:",s.roll)
        s.disp()
St=Student('Rahul',101)
User.show(St)