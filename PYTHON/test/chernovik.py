#!/usr/bin/env python3
import os.path,sys, re, json,re
import pandas as pd



def logs_from_file(logs):    
    test_file = open(real_path,'r') 
    for line in test_file.readlines():
        if re.search('\*400\*',line):
            print(re.sub('[(*+)]', ' ',line))
            #print(re.sub(r'\s+', ' ',line))
            logs['Availity'].append(line)
        if '*030240122' in line:
            logs['RealMed'].append(line)
        if '*030550127' in line:
            re.search('\*271\*',line)
            #logs['Hews'].append(line)
    test_file.close()


def init_logs():
    logs = {}
    logs['Availity']=[]
    logs['RealMed']=[]
    logs['Hews']=[]
    return logs
    
def converter():
    logs = init_logs()
    logs_from_file(logs)
    avility=logs['Availity']
    realmed=logs['RealMed']
    hews = logs['Hews']  
    pattern = re.compile('1030223')   
    #av_type_270 = [i for i in avility if '*1030223*' in i] 
  
    for i in hews:
      if re.search('\*271\*',i):
        x = i
        
        # print(x)
        

if __name__ == '__main__':
    inventory_dir = os.path.dirname(__file__)
    file_name = 'test.txt'
    real_path = os.path.join(inventory_dir,file_name)
    converter()
        



# inventory_dir = os.path.dirname(__file__)
# file_name = '/Users/akmanait/Documents/project/python3/project/aziz.json'
# real_path = os.path.join(inventory_dir,file_name)
# pattern = re.compile("tree")
# f = open(real_path)

# filename = json.load(f)
# count = 0
# for i in filename:
        
#         result = re.finditer(pattern,i)#'acidification')
        
#         for i in result:

#                 count+=1
# print(count)

