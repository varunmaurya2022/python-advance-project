class Mobile:
    fp='yes'
    @classmethod
    def show_model(cls,r):
        cls.ram=r
        print("Fingerprint:",cls.fp)
        print("Ram:",cls.ram)
realme=Mobile()
Mobile.show_model('4GB')
