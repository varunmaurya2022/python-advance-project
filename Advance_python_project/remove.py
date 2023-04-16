#reomove():-This method is used to remove first occurrence of given elelment from the existing array.
#If it doesn't found the element, shows valueError.
#array_name.remove(element)
from array import* 
dtu=array('i',[101,102,103,104,105])
n=len(dtu)
i=0
while i<n:
    print(dtu[i])
    i+=1
print("______________")
print("Array After Remove")

dtu.remove(102)
dtu.remove(109)
n=len(dtu)
i=0
while i<n:
    print(dtu[i])
    i+=1
print("Rest of Code")