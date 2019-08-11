# take a number from user to check condition handling using if and else

x = input("Hey User type your number")

if(int(x)==100):
    print("Number is Greater")
else:
    print("Number is smaller")


if(int(x)>100):
    print("Number is Greater")
else:
    print("Number is smaller")

#check multiple condition handling elif statements

inputnum = input("type your number")
inputnum = int(inputnum) # typecasting to change the string to integer

if(inputnum<0):
    print("Number is less than zero")
elif(inputnum==0):
    print("Number is equal to zero")
elif(inputnum%2==0): #if number remainder is 0
    print("This is even number")
else:
    print("This is odd number")

#check nested condition handling examples
inputnum = input("Give your num input")
inputnum = int(inputnum)

if (inputnum>=0):
    if(inputnum%2==0):
        print("This is even number")
    else:
        print("This is odd number")
else:
    print("This is negative number")

#check condition handling with logical or operator and this should be in lower case as it is case sensitive
inputnum = input("Give your num input")
inputnum = int(inputnum)

if (inputnum> 100 or inputnum <0):
    print(" This is invalid number")
else:
    print("This is valid number")

#check condition handling with logical and operator and same goes with not operator which is !
inputnum = input("Give your num input")
inputnum = int(inputnum)

if (inputnum> 0 and inputnum >10):
    print(" This is valid number")
else:
    print("This is invalid number")
