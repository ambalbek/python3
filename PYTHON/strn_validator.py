#!/usr/bin/env python3
if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum():
            a=True
        if i.isalpha():
            b=True
        if i.isdigit():
            c=True
        if i.isupper():
            d=True
        if i.islower():
            e=True
print(a)
print(b)
print(c)
print(d)
print(e)
