#!/usr/bin/env python3
def length(n):
    if len(n)<2:
        return n
    return n[0:2]+n[-2:]
if __name__=='__main__':
    #print(length('thequickbrownfoxjumpsoverthelazydog'))
    x = 'google.com'
    dict={}
    for i in x:
        keys=dict.keys()
        if i in keys:
            dict[i]+=1
        else:
            dict[i]=1
    #print(dict)
def change_char(str1):
    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]
    return str1

print(change_char('azizbek gapurov'))