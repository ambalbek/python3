import re
import pandas as pd
import csv



def converter():
    # availibility_list = []
    # realmed_list = []
    # hews_list = []
    


    with open('C:/Users/avi8r/Desktop/python/PYTHON/test/test.txt','r') as test_file: 
        count_il = 0
        count_mt = 0
        count_nm = 0
        count_ok = 0
        count_tx = 0 
        for line in test_file:
            tx = {}
            il = {}
            mt = {}
            nm = {}
            ok = {}        
            Availity = (line.split('        ')[3])
            RealMed = (line.split('        ')[3]) 
            Hews = (line.split('        ')[3])
            vendor =  (line.split('        ')[2])    
            if '*030240928' in vendor:
                           
                if '1030223' in Availity :                    
                    if '*621*' in Availity:
                        count_il+=1                        
                        il['IL']=count_il
                    if  '*751*' in Availity:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Availity:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Availity:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Availity:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*191703*' in Availity :
                    
                    if '*621*' in Availity:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in Availity:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Availity:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Availity:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Availity:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*085707*' in Availity :
                    
                    if '*621*' in Availity:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in Availity:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Availity:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Availity:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Availity:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*0877077*' in Availity :
                    
                    if '*621*' in Availity:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in Availity:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Availity:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Availity:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Availity:
                        count_tx+=1
                        tx['TX'] = count_tx
            if '*030240122' in vendor:                
                if '*1030223*' in RealMed :                    
                    if '*621*' in RealMed:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in RealMed:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in RealMed:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in RealMed:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in RealMed:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*191703*' in RealMed :
                    
                    if '*621*' in RealMed:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in RealMed:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in RealMed:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in RealMed:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in RealMed:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*085707*' in RealMed :
                    
                    if '*621*' in RealMed:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in RealMed:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in RealMed:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in RealMed:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in RealMed:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*0877077*' in RealMed :
                    
                    if '*621*' in RealMed:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in RealMed:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in RealMed:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in RealMed:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in RealMed:
                        count_tx+=1
                        tx['TX'] = count_tx
                
            if  '*030550127' in vendor:
                
                if '*1030223*' in Hews :
                    
                    if '*621*' in Hews:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in Hews:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Hews:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Hews:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Hews:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*191703*' in Hews :
                    
                    if '*621*' in Hews:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in Hews:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Hews:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Hews:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Hews:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*085707*' in Hews :
                    
                    if '*621*' in Hews:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in Hews:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Hews:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Hews:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Hews:
                        count_tx+=1
                        tx['TX'] = count_tx
                if  '*0877077*' in Hews :
                    
                    if '*621*' in Hews:
                        count_il+=1
                        il['IL']=count_il
                    if  '*751*' in Hews:
                        count_mt+=1
                        mt['MT']=count_mt
                    if  '*290*' in Hews:
                        count_nm+=1
                        nm['NM']=count_nm
                    if  '*340*' in Hews:
                        count_ok+=1
                        ok['OK']=count_ok
                    if  '*400*' in Hews:
                        count_tx+=1
                        tx['TX'] = count_tx
    return il,mt,nm,ok,tx

    
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

    




print(converter())