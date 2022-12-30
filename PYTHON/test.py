#!/usr/bin/env python3
x,y=0,1
while y < 100:
    x,y=y,y+x
    #print(y)

def fib(n):
    num=0
    x,y=0,1
    for i in range(n):
        x,y=y,y+x
        #c=y+x
        num+=1
    print(num,y)
fib(10)