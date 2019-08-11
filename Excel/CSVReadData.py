import csv

#Opening a file
f = open('E:\\Python.csv')
csv_data = csv.reader(f)
list1 = list(csv_data)
print(list1)

#some other method
f = open('E:\\Python.csv')
csv_data = csv.reader(f)
print(f.read())

# read all content from csv through looping
# f = open('E:\\Python.csv')
# csv_data = csv.reader(f)
# list1 = list(csv_data)
#
# for row in list1:
#     l = len(row)
#     for j in range(0,l):
#         print(row(j))

# 2. read all content from csv through looping
f = open('E:\\Python.csv')
csv_data = csv.reader(f)
list1 = list(csv_data)
print(list1)

l = len(list1)

for i in range(0,l):
    print(list1[i][0])
    print(list1[i][1])
    print(list1[i][2])