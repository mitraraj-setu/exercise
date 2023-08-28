import json
import csv

file1 = "nse_data_prac.json"
file2 = "csvfile.csv"

with open(file1) as f:
    data = json.load(f)
    # print(data)
    fields = []
    data2 = {}
    for i in data.keys():
        if (type(data.get(i)) == type([])):
            data2.update({i:data.get(i)})

    for i in data2.values():
        for j in i[0].keys():
            fields.append(j)
        break

    # print(fields)
    # print(data2)

    with open(file2,'w') as f1:
        writer = csv.DictWriter(f1, fieldnames=fields)
        writer.writeheader()

        for i in data2.values():
            writer.writerows(i)

        f1.close()
f.close()

with open(file2) as f2:
    print(f2.read())
    f2.close()