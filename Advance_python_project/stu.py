import pickle 
class Student:
    def __init__(self,name,roll,age,address):
        self.name=name
        self.roll=roll;
        self.age=age;
        self.address=address;
    def disp(self):
        print(f'Name:{self.name} Roll:{self.roll} Age:{self.age} Address:{self.address}')