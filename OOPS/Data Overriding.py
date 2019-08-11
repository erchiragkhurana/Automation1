class A:
    def amethod(self):
        print("This is A class method")

    def sub(self,a,b):
        print(a-b)

class C(A):
    def cmethod(self):
        print("This is C class method")

    def sub(self,a,b):
        print(b-a)


obj = C()
obj.amethod()
obj.cmethod()
obj.sub(10,21)

#Overridden method
# #It will call its own class method not parents if created with same name
#Signature means same parameter and same class name