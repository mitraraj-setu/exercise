import csv
import xlsxwriter
m = []

with open('05.csvout1.csv', mode='r') as file:
     csvFile = csv.DictReader(file, delimiter=',')
     for lines in csvFile:
            m.append(lines)

l = []
for i in m:
    optiontype = i.get("optionType")
    if optiontype not in l:
          l.append(optiontype)
print(l)


workbook = xlsxwriter.Workbook("05.csvout1.xlsx")
for i in l:
      worksheet = workbook.add_worksheet(i)
      row = 1
      col = 0
      for key in m[0].keys():
          worksheet.write(0, col, key)
          col += 1
      for x in m:
            if i == x["optionType"]:
                    col = 0
                    for key, value in x.items():
                        worksheet.write(row,col, value)
                        col += 1
                    row += 1
workbook.close()


