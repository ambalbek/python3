#!/usr/bin/env python3
import csv
from operator import itemgetter
def csv_creator(x):
    #csv_list= sorted(x, key=itemgetter('volume_size'), reverse=True) if you wish to sort
    csv_list=x
    #print(x)
    csv_columns = csv_list[0]
    #csv_columns = ['UserName','UserId', 'Days'] #
    csv_file='python3_output.csv'
    with open(csv_file,'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for d in csv_list:
            writer.writerow(d)