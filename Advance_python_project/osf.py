import os
print(os.path.isfile("student.txt"))
if os.path.isfile("student.txt"):
    f=open("student.txt")
    print(f)
else:
    print("Not Valid")

print('------------------------------')
import os
print(os.path.isfile("student1.txt"))
if os.path.isfile("student1.txt"):
    f=open("student1.txt")
    print(f)
else:
    print("Not Valid")