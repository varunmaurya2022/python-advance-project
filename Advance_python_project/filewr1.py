f=open('varun.txt',mode='w')
f.write("heloo\n")
f.write("varun\n")
f.write("how are you")
f=open('varun.txt',mode='r')
data=f.read()
print(data)
f.close()