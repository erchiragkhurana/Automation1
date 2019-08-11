#in one number, give character string value instead of number integer to generate exception

try:
    user_input1= input("Please enter your number")
    user_input2= input("Please enter your 2nd number")

    c = int(user_input1) + int(user_input2)
    print(c)

except:
    print("Your input is incorrect, please enter correct data")

finally:
    print("This code I want to execute at the end")

# to check config file, import ConfigParser class from configparser module
from configparser import ConfigParser

#Create an object for this ConfigParser class
config=ConfigParser()

#To read data from config file, use the inbuilt/predefined read method (always use forward slash for the path
#config.read("C:/Users/chirag/PycharmProjects/Automation1/Config.cfg")
config.read("./InputFiles/Config.cfg") #single dot is for current project d

print(config.get("Section 1", "username"))