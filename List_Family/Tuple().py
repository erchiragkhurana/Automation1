#In Tuple we use () bracket instead of []
#In tuple we cannnot update, insert or delete or increase or decrease size of Tuple
tuple1 = (12,13,14,"Chirag","Khurana",46,46)
tuple2 = (32,13,14,"Chirag","Khurana",47,48)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple1[2])

#Count number of times
print(tuple1.count(46))

#find index of any value in tuple
print(tuple1.index(46)) #by default it will show the index of the value which comes first

#how to print all values in tuple using for loop
for i in tuple3:
    print(i) #It will show all values in vertical format instead of horizontal and withou any bracket

#another way using len function
x = len(tuple1)
y = list(range(0,x))
print(y)
for i in y: #or range(0,x)
    print(tuple1[i])
