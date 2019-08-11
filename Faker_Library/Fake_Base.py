import faker
import xlwt

fake = faker.Faker()
wk = xlwt.Workbook()
ws = wk.add_sheet("Sheet1")

def displayWelcomeMessage():
    print("*********************************")
    print("Welcome to Test Data Generator")
    print("*********************************")

def enterNumberOfRecords():
    r = input("Please enter Number of Records---")
    return r

def selectOptions():
    print("Please select data which you want to generate\n\n")
    print("Enter 1 for Full Name")
    print("Enter 2 for Address")
    print("Enter 3 for Email")
    print("Enter 4 for Phone number\n\n")
    op = input("Please enter your choice (use comma in case of multiple option)")
    return op

def GenerateData(rec,data):
    r = int(rec)
    li = data.split(",")
    for i in range(0,r):
        count=0
        for j in li:
            if(j==1):
                ws.write(i, count, fake.name())
                count=count+1
            elif(j==2):
                ws.write(i, count, fake.address())
                count=count+1
            elif(j==3):
                ws.write(i, count, fake.email())
                count=count+1
            elif(j==4):
                ws.write(i, count, fake.phone_number())
                count=count+1

    wk.save("E:\\PythonAut\\faker1.xls")


