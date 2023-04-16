f=open("studet.txt", mode='w')
f.write("I am good ! How are you ?\n")
f=open("studet.txt", mode='a')
f.write("I am also Good ! What are you doing now ?")
f=open("studet.txt",mode="r")
data=f.read()
print(data)
f.close()


