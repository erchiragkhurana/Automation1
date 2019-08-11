#Break Statement with for loop
number = input("Type ur number")

for i in range (1,11):
    if(int(number)*i==5):
        break
    print(int(number)*i)

#Continue Statement (if you do not want to display few things in output)
#Continue with foor loop
for i in range (1,11):
    if(int(number)*i%10==0):
        continue
    print(int(number)*i)

#Else Statement with for loop (after loop)
for i in range(1,11):
    print(i)
else:
    print("Loop has ended7")