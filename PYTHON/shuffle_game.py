def lesser_of_two_evens(a,b):
    if sum((a,b)) % 2 == 0:
        print(min(a,b))
    else:
        print(max(a, b))
#lesser_of_two_evens(2,4)
#lesser_of_two_evens(2,5)

def animal_crackers(text):
    textsplit= text.split()
    if textsplit[0][0] == textsplit[1][0]:
        print(True)
    else:
        print(False)
#animal_crackers('Levelheaded Llama')
#animal_crackers('Crazy Kangaroo')
def makes_twenty(n1,n2):
    if sum((n1, n2))==20 or n1==20 or n2==20:
        print(True)
    else:
        print(False)
#makes_twenty(2,3)
def old_macdonald(name):
    print(name[:3].capitalize()+name[3:].capitalize())
#old_macdonald('macdonald')
def master_yoda(text):
    print(' '.join(text.split()[::-1]))
#master_yoda('I am home')
def almost_there(n):
    #return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#a = almost_there(104)
#print(a)

names=['aziz','akmanai','emir']
# print(list(map(lambda txt: txt[::-1], names)))
def name(txt):
    if len(txt)%2==0:
        return('even')
    else:
        return(txt[0])
#print(list(map(name, names)))

numbers=[1,2,3,4,5,6,7,8,9,10]
#print(list(map(lambda num: , numbers)))
def num(nums):
    if nums%2==0:
        return 'even'
    else:
        return nums
#print(list(map(num, numbers)))

def filt(num):
    return num%2==0
#print(list(filter(filt, numbers)))
#for i in filter(filt, numbers):
    #print(i)

group=['aziz','akmanai','emir']
name=['gapurov','turganbaeva','nazar']
#print(list(map(lambda name: name, group)))

text='this is global text'
def local():
    text='this is local text'
    def inlocal():
        print('hello from '+text)
    inlocal()
local()