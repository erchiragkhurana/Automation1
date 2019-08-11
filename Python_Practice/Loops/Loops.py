#For Loop with final range

for i in range(10):
    print(i)

#For loop - if have to take integer from user as input

number = input("Type your number please")
for i in range(int(number)):
    print(i)

#For Loop with initial and final range
z=10
for i in range (1,10):
    print( str(z)+"*" + str(i) + "=" + str(z*i))

#For Loop with initial and final range
number = input("Type ur number")
for i in range (1,11):
    print(number + "*" + str(i) + "="+ str(int(number)* i) )

#For Loop with icrement value
for i in range(1,10,4): #first is starting point, 2nd is ending point, 3rd is increment
    print(i)
#For Loop with decrement value, it is used when we have to go in reverse order
for i in range(10,1,-3): #first is starting point, 2nd is ending point, 3rd is increment
    print(i)

#anothe rexample
number = input("Type your numb")
for i in range (10,0,-1):
    print(int(number)* i)

#For Loop with list
#first we need to create a list with some data and can use different data types

list1 = [1, 4, 7, "Chirag", "Khurana"]
for i in list1:
    print(i)

list1 = input("Type your number")
for i in list1:
    print(i)

