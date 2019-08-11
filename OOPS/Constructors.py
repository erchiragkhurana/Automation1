#Constructors are special type of method, created with _init()_
#First argument is always self, it can take arguments but never returns any value because they are used for initialization only
#Automatically called when an object is created
# We use constructor where we have to run the code before the full method like making a connection with the database

class A:

    def __init__(self):
        print("This is my first constructor")

    def hello(self):
        print("Hello World") #some other function

obj = A()
obj.hello()

class B:

#Constructor can take arguments too
    def __init__(self, a, b):
        c=a+b
        print(c)

obj = B(25,37)

class C:

    def testing(self):
        print("Testing Testing")

#We can also import another python file which is called module
from OOPS import FirstClass

obj = FirstClass.a() #Object was already create I have created it here again, it will show the results of full class a
obj.welcome() #It will only show the result of welcome function


# some other function without class
def welcome():
    print("Welcome World")

def sum(a,b):
    c=a+b
    print(c)

def mul(a,b):
    c=a*b
    return c