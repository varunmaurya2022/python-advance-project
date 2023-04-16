def fibon(n):
    assert n>=0 and int(n)==n,'Please Enter Posirive value'
    if n in [0,1]:
        return n
    else:
        return fibon(n-1)+fibon(n-2)
print(fibon(5))
print("____________________")