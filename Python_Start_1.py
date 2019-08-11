# This is python first file
from IPython.utils.syspathcontext import prepended_to_syspath

print("This is my first file")

i = input("Please enter your name")
print("Your name is" + i)

#  When we take input from user, it is always a String, if you want number then we have to typecast
age = input("Please enter your age ------")

# Want to add 10 in age number
final_age = int(age) + 10  # Type casted age to number and then added 10
print("Final Age : - " + str(final_age))  # Again type cast back to String to concatnate with another string