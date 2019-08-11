# user_input = int(input("Please enter your number"))
#
# assert user_input>18
# print("Done")

#another method for failure
user_input = int(input("Please enter your number"))

assert user_input>18, "Failed as data is not correct"
print("Done")