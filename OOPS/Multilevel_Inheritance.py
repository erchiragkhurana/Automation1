class A:
    def amethod(self):
        print("This is A class method")

class B(A):
    def bmethod(self):
        print("This is B class method")

class C(B):
    def cmethod(self):
        print("This is C class method")

obj = C()
obj.amethod()
obj.bmethod()
obj.cmethod()