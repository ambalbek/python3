import csv
data = open('python3_output.csv')
csv_data = csv.reader(data)
dataline=(list(csv_data))

with open('aziz.csv', 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=dataline[0])
    csv_writer.writeheader()
    csv_writer.writerow(dataline)