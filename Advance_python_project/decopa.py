class Mobile:
    fp='Realme 2'  #class variable
    @classmethod  #decorator
    def show_model(cls,r):
        cls.ram=r
        print(cls.fp,cls.ram)
realme=Mobile()
Mobile.show_model(101)