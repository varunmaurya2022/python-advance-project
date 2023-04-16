c=10
e=2
try:
    f=c/e
    print(f)
except ZeroDivisionError:
    print("Division by Zero not allowed")
else:
    a=10
    b=10
    d=a=b
    print(d) 
    print("Inside Else")  
print("***------***")

