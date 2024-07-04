import csv
import xlsxwriter

v = []
with open("csvout1.csv", "r") as file:
    csvfile = csv.DictReader(file)
    for lines in csvfile:
        v.append(lines)
# print(v)
list = []
for i in v:
    optiontype = i.get("optionType")
    if optiontype not in list:
        list.append(optiontype)
# print(list)
workbook = xlsxwriter.Workbook("yash.xlsx")
for i in list:
    worksheet = workbook.add_worksheet(i)
    formate = workbook.add_format({"bold": "True"})
    row = 1
    for x in v:
        if i == x["optionType"]:
            col = 0
            for key, value in x.items():
                worksheet.write(0, col, key, formate)
                worksheet.write(row, col, value)
                col += 1
            row += 1

    worksheet.autofit()

workbook.close()
