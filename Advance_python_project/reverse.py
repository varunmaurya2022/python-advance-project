#reverse():-This method is used to reverse the order of elements in the array.
#Syntax:-array_name.reverse()
from array import*
array_name=array('i',[101,102,103,104,105])
n=len(array_name)
i=0
while i<n:
    print(array_name[i])
    i+=1
print("______________")
print("Rest of Code")
print("After REverse")

array_name.reverse()
n=len(array_name)
i=0
while i<n:
    print(array_name[i])
    i+=1
print("----------------")

