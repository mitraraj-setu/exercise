import csv
import xlsxwriter

file2 = "csvfile.csv"
file1 = "csvfile3.xlsx"

final_dict = {}

with open(file2) as f2:
    csvFile = csv.DictReader(f2)

    for i in csvFile:
        if(i.get('optionType') not in final_dict):
            final_dict.update({i.get('optionType'):[]})
        final_dict.get(i.get('optionType')).append(i)

f2.close()

with open(file1,'w') as f:

    workbook = xlsxwriter.Workbook(file1)

    for i in final_dict.keys():
        worksheet = workbook.add_worksheet(i)

        key_list = list(final_dict.get(i)[0].keys())
        worksheet.write_row(0,0,key_list)

        for j in range(len(final_dict.get(i))):
            value_list = list(final_dict.get(i)[j].values())
            worksheet.write_row(j+1,0, value_list)

    workbook.close()

f.close()