class parentclass:
    def parentclassmethod(self):
        print("This is Parent Class")

class childclass(parentclass):
    def childclassmethod(self):
        print("This is Child Class")

obj=childclass()
obj.parentclassmethod()
obj.childclassmethod()