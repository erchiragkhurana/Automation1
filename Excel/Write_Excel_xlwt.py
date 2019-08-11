import xlwt

#First we need to create object of workbook

wb = xlwt.Workbook("E://XLRD_File.xlsx")
# It can also write to a blank sheet
# wb = xlwt.Workbook()

ws = wb.add_sheet("Testing")
ws.write(0,0,"Testing Khurana")
ws.write(0,1,"PythonTesting")

wb.save("E://XLWT_File.xls") #Save the Workbook and it didnt run with xlsx format to write (this is a drawback)
