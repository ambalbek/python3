#!/bin/bash 
mylist= [('ibrash', 115000),('daniyar', 95000),('ulan', 110000),('kuba brat', 180000)]
def maxcheck(mylist):
    maxzp=0
    boyvatcha=''
    for x,y in mylist:
        if y > maxzp:
            maxzp=y
            boyvatcha=x
        else:
            pass
    #return (boyvatcha, maxzp)
    print(boyvatcha, maxzp)
maxcheck(mylist)
