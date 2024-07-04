import csv
import xlsxwriter
m = []

with open('06.hospital_directory.csv', mode='r') as file:
     csvFile = csv.DictReader(file, delimiter=',')
     for lines in csvFile:
            m.append(lines)
print()
l = []
for i in m:
    State = i.get("State")
    if State not in l:
          l.append(State)
print(l)



workbook = xlsxwriter.Workbook("06.hospital_directory.xlsx")
for i in l:
      worksheet = workbook.add_worksheet(i)
      row = 1
      col = 0
      for key in m[0].keys():
          worksheet.write(0, col, key)
          col += 1
      for x in m:
            if i == x["State"]:
                    col = 0
                    for key, value in x.items():
                        worksheet.write(row,col, value)
                        col += 1
                    row += 1
workbook.close()