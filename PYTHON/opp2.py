from math import pi
class Rectangle():
    def __init__(self,length,width,height):
        self.lenth_of_rectangle= length
        self.width_of_rectangle = width
        self.height_of_rectangle = height
    def calculate(self):
        perimeter=(self.width_of_rectangle+self.lenth_of_rectangle)*2
        area= self.width_of_rectangle*self.lenth_of_rectangle
        volume = self.width_of_rectangle*self.lenth_of_rectangle*self.height_of_rectangle
        return 'perimeter of rectangle is {p}, volume is {v}sqf, and area is {a}cubicsqf'.format(p=perimeter,a=area,v=volume)
        
pryamougolnik = Rectangle(length=20, width=12, height=15)
print(pryamougolnik.calculate())