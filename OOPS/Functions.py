#def is the keyword
#return keyword shows the that the it is the end of the function in same indentation

#First type of function which is not taking any argument and not returning any value
def testing():
    "This is the first line and used for commenting, neend not to mention #here"
    print("This is Chirag Khurana")
    print("This is 147")

testing()

#Second type, in which we pass/taking the argument but not returning any value (required arguments)
def sum(a,b):
    c=a+b
    print("Sum of two numbers is "+ str(c))

sum(2,3)

#3rd type, passing argumnet and returning value for the other function
def multiply(a,b):
    c = a * b
    return c

def addition(a,b):
    c=a+b
    print(c)

x= multiply(4,5)
addition(x,10)

#4th type, function which is not taking any argument but returnung value
def retdata():
    a=100
    return a

x= retdata()
print(x)

#different type of arguments (Required Arguments, Keyword Argumnets, Default Arguments)
#Required argumnets are thos in which we have to pass the argumnet mandatory like above examples if two then 2 not be 3
#second type is keyword argument in which we can define which argument needs to be execute first, kind a subset of required
def keywordArg(a,b):
    c=a+b
    print("Sum of two numbers is "+ str(c))

keywordArg(b=5,a=3)

#third type of argument is default argument in which we can specify the value of argument initially
def defArg(a,b=100): #keep in mind that if you specify the first value for a here then it is required to have value for b also
    c=a+b
    print("Sum of two numbers is "+ str(c))

defArg(a=2) or defArg(2) # it is upto us we can pass the second argument value here also, kind of optional