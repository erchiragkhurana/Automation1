#Class can have variables, constants, functions and constructors
#whenever we create any function under the class the first argumnet we have to pass is self
#whenever we want to use any class we have to create an object

class a:

    #This is class function with no argument and no return value
    def welcome(self):
        print("This is my first class")

    #Function, which will take 2 arguments, some value and display it but not returning any value
    def sum(self,a,b):
        c=a+b
        print("Sum is "+ str(c))

    #Function, which will take some argument and return some value
    def mul(self,a,b):
        c=a*b
        return c

obj = a() #To call any member of the class, we have to create the object of the class
obj.welcome() #call function of the class by using object
obj.sum(10,100)
x = obj.mul(10,20)

obj.sum(x,10)

class b:

    #This is class function with no argument and no return value
    def welcome(self):
        print("This is my second class")

    #Function, which will take 2 arguments, some value and display it but not returning any value
    def sum(self,a,b):
        c=a+b
        print("Sum is "+ str(c))

    #Function, which will take some argument and return some value
    def mul(self,a,b):
        c=a*b
        return c

