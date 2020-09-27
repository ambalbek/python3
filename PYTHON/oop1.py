class Emir():
    def __init__(self,sex,name,lastname):
        self.babies_sex=sex
        self.babies_name=name
        self.babies_lastname= lastname
    def speak(self):
        print('My name is {a}'.format(a=self.babies_name))
son= Emir(sex='boy', name='Emir', lastname='Nazar')
#print(son.babies_name,son.babies_lastname, son.babies_sex)
print(son.speak())