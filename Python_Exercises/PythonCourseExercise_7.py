import xlsxwriter
import json
import csv

file1 = "nse_data_prac.json"
file2 = "csvfile2.xlsx"

with open(file1) as f:
    data = json.load(f)
    # print(data)
    data2 = {}

    for i in data.keys():
        if (type(data.get(i)) == type([])):
            data2.update({i:data.get(i)})

    with open(file2, 'w') as f1:

        workbook = xlsxwriter.Workbook(file2)
        for i in data2.keys():
            worksheet = workbook.add_worksheet(i)

            key_list1 = list(data2.get(i)[0].keys())
            worksheet.write_row(0,0, key_list1)
            print(key_list1)

            for j in range(len(data2.get(i))):

                value_list = list(data2.get(i)[j].values())
                worksheet.write_row(j+1,0,value_list)
        workbook.close()

    f1.close()

f.close()

# with open(file2) as f2:
#     print(f2.read())
#     f2.close()








