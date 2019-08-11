from builtins import reversed

#how to find before 3 characters of a substring
a="Testing"
b="ing"
x = a.find(b) #return index value which is 4 here
print(a[x-3:x]) #1:4

#Reverse a string (1st method)
list1=(list(reversed(a))) #reversed function return an object
print(" ".join(list1))

#Reverse a string (2nd method)
for i in reversed(a): #we can use list1 instead of reversed(a) too
    print(i)

#Reverse a string (3rd method)
l=len(a) #length is full and indexing starts from 0 so we have to take l-1
for i in range((l-1),-1,-1):
    print(a[i])

#Reverse a string (4th method)
a="Testing"
b=""
l=len(a) #length is full and indexing starts from 0 so we have to take l-1
for i in range((l-1),-1,-1):
    b=b+a[i]
print(b)

#Palindrome
a = "MadaM" #as python is case sensitive
b = ""
l = len(a)  # length is full and indexing starts from 0 so we have to take l-1
for i in range((l - 1), -1, -1):
    b = b + a[i]

if (a==b):
    print("This is a palindrome")
else:
    print("This is not a palindrome")

#Read all characters from file and display one by one
for i in obj.read():
    print(i)

#Read all characters from first line and display one by one
#for i in obj.readline():
    #print(i)

#Read all characters from file line by line
s = obj.readline()
while (s):
    print(s)
    s=obj.readline() #Till the value of s exist this loop will run

#It will read full file line by line without any spacing
s=obj.read()
while (s):
    print(s)
    s=obj.read()

#In Inheritance methods will only call its own class constructor only, not of the parent class and for that you have to create
#the new object for the parent class to call its init constructor

#we use xlrd librar and its functions to read data from excel sheets

#Q - How do you handle javascript in python with Selenium (javascript handle browser)
driver.execute_script("window.scrollTo(0,400);") #This is to scroll down the horizontal scroller upto 400 px and javascript is separated by;