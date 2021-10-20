import re
import pandas as pd
def converter():
    availibility_list = []
    realmed_list = []
    hews_list = []

    with open('C:/Users/avi8r/Desktop/python/PYTHON/test/test.txt','r') as test_file:   
        line = [line for line in test_file] 
        count =0
        for i in line:
            if '030240928' in i:
                availibility_list.append(i)
            if '030240122'  in i:
                count+=1                
                realmed_list.append(i)
            if '030550127' in i:
                hews_list.append(i)
        #             realmed_list.append(new_line)
    #     for line in test_file:
    #         new_line =re.split('\~|\*', line)
    #         print(new_line)
    #         if '030240928' in new_line:
    #             availibility_list.append(new_line)
    #             print(new_line)
    #         elif '030240122' in new_line:
    #             realmed_list.append(new_line)
                
    #         elif '030550127' in new_line:
    #             hews_list.append(new_line)
    # print(count)
    # print(realmed_list)
    for i in realmed_list:
        if '621' in i:
            il=i
            
            if '1030223' in il:
                _270 = il
                print(il)
            if '191703' in il:
                _271=il    
                print(il)                
            if '085707' in il:
                _276 = il
                print(il)
            if '0877077' in il:
                _277=il
                print(il)
                    
        if '751' in i:
            mt=i
            
            if '1030223' in mt:
                _270 = mt
                print(mt)
            if '191703' in mt:
                _271=mt    
                print(mt)                
            if '085707' in mt:
                _276 = mt
                print(mt)
            if '0877077' in mt:
                _277=mt
                print(mt)
        if '290' in i:
            nm =i
            
            if '1030223' in nm:
                _270 = nm
                print(nm)
            if '191703' in nm:
                _271=nm   
                print(nm)                 
            if '085707' in nm:
                _276 = nm
                print(nm)
            if '0877077' in nm:
                _277=nm
                print(nm)
        if '340' in i:
            ok = i
            
            if '1030223' in ok:
                _270 = ok
                print(ok)
            if '191703' in ok:
                _271=ok  
                print(ok)                  
            if '085707' in ok:
                _276 = ok
                print(ok)
            if '0877077' in ok:
                _277=ok
                print(ok)
        if '400' in i:
            tx=i
            
            if '1030223' in tx:
                _270 = tx
                print(tx)
            if '191703' in tx:
                _271=tx    
                print(tx)               
            if '085707' in tx:
                _276 = tx
                print(tx)
            if '0877077' in tx:
                _277=tx
                print(tx)




converter()