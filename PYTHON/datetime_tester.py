import datetime
time = datetime.datetime.now()
def data(god):
    god = datetime.datetime(2020,8,28,11,17)
    itogo = time - god

    print(itogo.days)
data(datetime.datetime(2019,9,10))