# #to check the sequence
# li = [1,3,5,6,9]
#
# j=0
# x = li[j + 1] - li[j]
#
#
#
# for i in range(len(li)-1):
#         if (li[i + 1] - li[i])!= x:
#             print("This is not a sequence")
#             break
#
#         elif (li[i + 1] - li[i])==x:
#             return True
#             print("This is sequence")


# 1. Check even odd

class A:

    def checkEvenOdd(self, inputNumber):
        if (inputNumber<0):
            print("This is invalid number")

        elif (inputNumber==0):
            print("This is zero")

        elif (inputNumber%2==0):
            print("This is even number")

        else:
            print("This is odd number")

obj = A()
obj.checkEvenOdd(1)

# 2. Grading System = Create a method which will take students marks and verify
# (a) if marks are less than 0  or more than 100 then show invalid marks
# (b) between 1-30 then failed, 31-45 then 3rd, 46-60 then 2nd, 61-100 then 1st

class Marks:

    def checkGradingSystem(self, inputMarks):
        if (inputMarks<0 or inputMarks>100):
            print("Invalid Marks")
        elif (inputMarks>0 and inputMarks<=30):
            print("Sorry, you are failed")
        elif (inputMarks>30 and inputMarks<=45):
            print("You are third division")
        elif (inputMarks>45 and inputMarks<=60):
            print("You are second division")
        else:
            print("Congrats you are first")

obj=Marks()
obj.checkGradingSystem(31)

# 3. Check Fibonacci series upto 100 (0,1,1,2,3,5,8,13,21...) first two numbers are defined
class Fibonacci:

    def generateFibonacci(self,userInput):
        a=0
        b=1
        print (str(a)+ "," + str(b))
        while (a+b<userInput):
            b=a+b
            a=b-a
            print("," + str(b))

obj=Fibonacci()
obj.generateFibonacci(100)

# 4. Largest amongst three numbers - condition handling
class LargestNumber:
    def findLargestNumber(self,a,b,c):
        if (a>b and a>c):
            print(str(a) + " is the largest")
        elif(b>a and b>c):
            print(str(b) + " is the largest")
        else:
            print(str(c) + " is the largest")
obj=LargestNumber()
obj.findLargestNumber(90,90,65)

# 5. Check whether a number is divisible by 5 or 11 or both
class Divide:
    def checkDivide(self,enterNumber):
        if (enterNumber%5==0 and enterNumber%11==0):
            print(str(enterNumber) + " is divisible by 5 and 11" )
        elif (enterNumber%11==0):
            print(str(enterNumber) + " is divisible by 11" )
        elif (enterNumber%5==0):
            print(str(enterNumber) + " is divisible by both 5")
        else:
            print(str(enterNumber)+ " is not divisible by 5 and 11")
obj=Divide()
obj.checkDivide(55)

# 6.
li = 