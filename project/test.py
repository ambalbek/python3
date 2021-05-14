import json
import csv
def test():
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    key={}
    value={}
    lst=[]
    for k,v in data.items():
        key['word']=k
        value['definition']=(' '.join([str(elem) for elem in v]))
        new = {**key ,**value}
        lst.append(new)
    csv_columns = lst[0].keys()
    csv_file='data_file.csv'
    try:
        with open(csv_file,'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for i in lst:
                writer.writerow(i)
    except Exception as e:
        print(e)
test()
