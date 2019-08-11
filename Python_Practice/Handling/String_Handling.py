#double quotes inside whole single quote
from builtins import print

mynumber = '"Chirag"147'
print(mynumber)

#single quote comes inside wholde double quote
mynumber = "Chirag'147'"
print(mynumber)

#three time quotes if you write bigger information which exist in more than one line
mynumber="""
My number is
147
"""
print(mynumber+"Thank you ji") # Concatenate
print(mynumber*3) #to display it 3 times

#String indexing and inbuilt string functions
number = "  ChiragKhurana147  "
print(number[0:7])
print(len(number)) # it is a common fucntion can be used with list,tupple etc. and it also counts the spaces
print(number.upper())
print(number.lower())
print(number.capitalize())
print(len(number.lstrip())) #Left strip used with len function
print(len(number.rstrip())) #Right strip
print(len(number.strip())) #Both Left and right strip
print(number.strip()) #without len function
print(number.replace("147","rana"))
a="Testing"
b="ing"
print(a.find(b)) #find function

#how many a in your string
x = (len(number)) #20
y = (len(number.replace("a",""))) #17
print(x-y)

#second method to find
for i in number:
    if(i=="a"):
        print("Yes Found")

#third method to find
z=0
for i in number:
    if(i=="a"):
        z=z+1
print(z)

#split function
x = "You are the best"
z=0
list1 = x.split(" ") #space is mandatory
for i in list1:
    if(i=="are"):
        z=z+1
print(z)

#Compare 2 strings
a="Testing"
b="  Testing  "
c="TESTING"
d="testing"
if (a.strip()==b.strip()):
    print("Compared")
else:
    print("Not Compared")

if (c.upper()==d.upper()):
    print("Compared")
else:
    print("Not Compared")