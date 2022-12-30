#!/usr/bin/env python3
class Termo:
    def __init__(self):
        self.name='this will return temperature'
    def fahrenheit(self,**x):
        for k,v in x.items():
            if k=='f': return (lambda i: f'temperature in fahrenhet is :{(i*9/5)+32::.1f}F')(int(v))
            else: return (lambda i: f'temperature in celcius is :{(i-32)*5/9:.1f}C')(int(v))    
    def main(self,**x):
        return self.fahrenheit(**x)

if __name__ == '__main__':
    tmp = input('Would you like to convert celcius or fahrenheit? c for celcius f for fahrenheit: ')
    gradus = Termo()    
    if tmp == 'c': print(gradus.main(tmp=int(input('please provide your temperature in fahrenheit: '))))
    else: print(gradus.main(tmp=int(input('please provide your temperature in celcius: '))))
    