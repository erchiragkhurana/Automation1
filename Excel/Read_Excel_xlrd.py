import xlrd

# 1.We need to create object of workbook

wb = xlrd.open_workbook("E://XLRD_File.xlsx")

#Found number of sheets
print(wb.nsheets)

# 2.Now we need to move to the sheet level
ws = wb.sheet_by_index(0) #0 means first sheet here and 1 means 2nd sheet in the workbook
print(ws.nrows)
print(ws.ncols)

#one more approach
ws = wb.sheet_by_name("TravelBudget")
print(ws.nrows)
print(ws.ncols)

#Read data from all rows and columns
ws = wb.sheet_by_name("TravelBudget")
r = ws.nrows
c = ws.ncols

for i in range(0,r): #Now run a loop for number of rows
    for j in range (0,c):
        wc = ws.cell(i,j)
        print(wc.value)


# 3.Now move to cell level to pick data from cells
wc = ws.cell(1,1)
print(wc.value)