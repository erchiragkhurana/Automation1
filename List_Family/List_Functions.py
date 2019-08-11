list1=[14,22.33,"Testing",56,57,"Khurana"]
list2=[25,22.33,"Chirag",56,57,"Khurana"]
list3=list1 + list2
print(list3)

#to find by index
print(list1[1])
print(len(list1))

#to find by range of index
print(list1[1:5])

#if you want to update the value of a list(no dot function is used)
list1[1]=100
print(list1)

#if you want to insert the value in a list
list1.insert(5,"Chirag")
print(list1)

#if you want to delete/remove the value from a list
list1.remove(56) #need to pass object only
print(list1)

