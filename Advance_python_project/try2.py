a=10
b=3
try:
    d=a/b
    print(d)
except (NameError,ZeroDivisionError) as obj:
    print(obj)
print("___________________")
    