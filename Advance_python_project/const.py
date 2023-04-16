class Mobile:
    def __init__(self,m,v=80):
        self.model=m
        self.volume=v
    def show_model(self,p):
        self.price=p
        print("Model:",self.model)
        print("Volume:",self.volume)
        print("Price:",self.price)
realme=Mobile('Realme X',90)
realme.show_model(1000)
print('-------------------')
redmi=Mobile('Redmi 7',102)
redmi.show_model(3000)
print('--------------------')
oppo=Mobile('Oppo',110)
oppo.show_model(4000)