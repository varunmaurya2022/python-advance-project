import pickle,stu
with open("Student.dat",mode='rb') as f:
    while True:
        try:
            obj=pickle.load(f)
            obj.disp()
        except EOFError:
            
            print("Done")
            break;
            
            