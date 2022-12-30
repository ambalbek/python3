#!/usr/bin/env python3
class Dog():
    def __init__(self,name):
        self.dogs_name=name
    def speak(self):
        return 'my name is {}'.format(self.dogs_name)
class Cat():
    def __init__(self,name):
        self.cats_name= name
    def speak(self):
        return 'my name is {}'.format(self.cats_name)
koshka= Cat(name='silvester')
pes = Dog(name='Graf')
print(pes.speak())
print(koshka.speak())