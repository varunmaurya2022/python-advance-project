from types import ModuleType


class Mobile:
    def __init__(self,model):
        self.model = model 
    def show_model(self):
        print("Model:",self.model)
Realme=Mobile(101)
Realme.show_model()