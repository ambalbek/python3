#!/usr/bin/env python3
class Test:
    def __int__(self,name):
        self.my_lambda= lambda x: x**2
    def some_func(self, *args):
        result = (list(filter(lambda x: len(x)%2==0 ,args)))
        return result

    def seconday(self,*args):
        x =self.some_func(*args)
        return list(map(lambda _i,i: {str(_i[0])+'_Gapurov':i}, enumerate(x),x ))
    def primar(self,*args):
        a=self.seconday(*args)
        #print(a)
        return list(map(lambda x: f'this is the result of the {x}',a))
        
x = Test()
print(x.primar('Azizbek','Emir','Khabib','Akmanai'))


