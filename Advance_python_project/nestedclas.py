class Army:
    def __init__(self):
        self.name='Rahul'
        self.gun=self.Gun()
    def show(self):
        print("Name:",self.name)
class Gun:
    def __init__(self):
        self.name='Ak47'
        self.capacity='75 Rounds'
        self.length='34.3In'
    def disp(self):
        print("Gun Name:",self.name)
        print("Gun Capacity:",self.capacity)
        print("Gun length:",self.length)
a=Army()
print(a.name())
print(a.show())
print(a.gun.name())
g=a.gun
print()
print(g.name)
print()
g.disp()