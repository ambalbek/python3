#!/usr/bin/env python3
####### kak nayti '''abcde * a = eeeeee'''
def abcde(n):
    num = 0
    while num < n:
        a = 0
        _count=1
        num+=111111
        while _count < 10:
            _count+=1
            divident = num//_count
            str_num = [i for i in str(divident).split()[0]]
            if len(str_num) == 5:
                a,b,c,d,e = int(str_num[0]),int(str_num[1]),int(str_num[2]),int(str_num[3]),int(str_num[4])
                if a != b and a != c and a != d and a != e\
                    and b != c and b != d and b != e\
                        and c != d and c != e and d != e and a == _count:
                    if divident*_count==num:
                        return divident, f'===> {_count}'
print(abcde(int(input('To find abcde please enter the number greater or equal to 6 digits: '))))




    




