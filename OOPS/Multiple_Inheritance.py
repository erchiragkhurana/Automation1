class A:
    def amethod(self):
        print("This is A class method")

class B:
    def bmethod(self):
        print("This is B class method")

class C(A,B):
    def cmethod(self):
        print("This is C class method")

obj = C()
obj.amethod()
obj.bmethod()
obj.cmethod()