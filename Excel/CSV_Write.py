import csv

f = open("E:\\WriteCSV.csv",'w',newline='')
csv_w = csv.writer(f)
csv_w.writerow(['hello',12,131])
csv_w.writerow(['hello1',12,131])
csv_w.writerow(['hello2',14,134])

f.close()