#r,w,a
#r+,w+,a+ = read and write mode, write and read mode, append and read mode
# 1.Reading data from the file
#obj = open("E:\Py.txt",'r')

#Read all the data from file
#print(obj.read())
#print(obj.read(12)) #It will show the 12 characters from the file

#Read first line from the file
#print(obj.readline(7)) #It will read first 7 characters including space in the first line of first line
#print(obj.readline()) #It will read rest of the characters of the firt line
#print(obj.readline()) #It will read all the characters of the second line

#Read all characters from file and display one by one
# for i in obj.read():
#     print(i)

#Read all characters from first line and display one by one
# for i in obj.readline():
#     print(i)

#Read all characters from file line by line
# s = obj.readline()
# while (s):
#     print(s)
#     s=obj.readline() #Till the value of s exist this loop will run

#It will read full file line by line without any spacing
# s=obj.read()
# while (s):
#     print(s)
#     s=obj.read()

# 2.Writing data to file (.txt) if it will not exist it will create one and write it
# obj = open("E:\Py1.txt",'w') #It will remove all previous data if file is already there
# obj.write("I am writing using Pycharm write method")
# obj.close()

# 3. If you do not want to remove previous data then use append fucntion
# obj = open("E:/py1.txt",'a')
# obj.write(" Hello Hello") #everytime you run this program it will write everytime the write operation
# obj.close()

# 4. Tell Method will tell you about your cursor position
obj = open("E:\Py.txt",'r')
print(obj.tell())

obj.readline()
print(obj.tell()) #once you read a line your cursor position will change

# 5. Seek Method - is used to navigate the cursor to a different location
obj.seek(5)
print(obj.tell())

