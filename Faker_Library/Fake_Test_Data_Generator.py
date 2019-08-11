import faker
import xlwt

fake = faker.Faker()
wk = xlwt.Workbook()
ws = wk.add_sheet("Sheet1")


#print(fake.name())

#for i in range(1,11):
    #print(fake.name()+" " + fake.email() + " "+ fake.city() + " " + fake.phone_number())

for i in range (0,100):
    ws.write(i,0,fake.name())
    ws.write(i,1,fake.address())
    ws.write(i,2,fake.email())
    
wk.save("E:\\PythonAut\\faker1.xls")

#in short - xlwt.Workbook().add_sheet().write() & xlwt.Workbook().save()