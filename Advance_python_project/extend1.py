#extend():-This method is used to append  another  array or iterable object at the end of the array.
#Syntax:-array_name.extend(arr)
from array import*
stu=array('i',[101,102,103,104,105])
arr=array('i',[110,112,111])
n=len(stu)
i=0
while i<n:
    print(stu[i])
    i+=1
print("___________________")
print("Afetr Extend")
stu.extend(arr)
n=len(stu)
i=0
while i<n:
    print(stu[i])
    i+=1
print("End Of Program")