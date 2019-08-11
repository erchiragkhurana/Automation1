#When we are importing any module , that modules executable code will run
#In modules you can call module function , class (Class can have class functions)
from OOPS import Constructors

#We are calling module functions by module name
Constructors.sum(2, 3)

x = Constructors.mul(2, 3)
print(x)

Constructors.sum(x, 3)
Constructors.sum(5, x)

#We need to create object of class written in any module
obj = Constructors.C()
obj.testing()

#using from - import function
from OOPS.FirstClass import b

objb = b() #(Here we need not to mention the directory name or module file name)
objb.welcome()

