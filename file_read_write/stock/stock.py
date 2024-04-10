import csv

data = [['Company Name', 'PE Ratio', 'PB Ratio']]
with open("stocks.csv", "r") as input_file:
    content = csv.reader(input_file)
    for index, row in enumerate(content):
        if index != 0:
            temp = []
            pe = round(float(row[1]) / float(row[2]), 2)
            pb = round(float(row[1]) / float(row[3]), 2)
            temp.append(row[0])
            temp.append(pe)
            temp.append(pb)
            data.append(temp)

with open("output.csv", 'w', newline='') as file:
    write = csv.writer(file)
    for row in data:
        write.writerow(row)
