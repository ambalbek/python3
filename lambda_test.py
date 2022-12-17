from math import pi
from functools import reduce
import logging
logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# lambda_test = lambda x, y: x/y

# print(lambda_test(2,4))
    

# temp_convert = lambda c: 9/5*c+32

# print(temp_convert(-30))


# circle_area = lambda r: pi*r**2

# print(circle_area(4))

# sphere_volume = lambda r : 3/4*pi*r**2
# print(sphere_volume(4))




# print((lambda r : 3/4*pi*r**2)(4))


# print((lambda a,b,c: a*b/c)(5,7,5))


# print((lambda f : (f-32)*5/9)(25))


# x = [4 , 6, 7, 2, 12, 5]
# total = (list(map(lambda a : a**2, filter(lambda c : c, x))))

# for i in total:
#     fib = lambda n: reduce(lambda b, _: b+[b[-1]+b[-2]],range(n-2), [0, 1])
#     ac = fib(i)
#     print(ac[-1])
# #print([lambda n: reduce(lambda b, _: b+[b[-1]+b[-2]],range(n-2), [0, 1]) for i in x])


# fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
# print(fib(10))


# print((lambda x: 'older' if x > 30 else 'younder')(25))


# print((lambda x: x if x%2==0 else 'odd')(26))


# for i in range(1,10):
#     print((lambda x : x+x)(i), end='')


class Test1:
    def __init__(self,n):
        self.n = n

    def _secondary(self):
        return self.n

    def _primary(self):
        return f"""string {self.n} is {len(self.n)}"""

class Test2(Test1):
    def _third(self):
        print(len(self.n))
        logger.info((lambda x: True if len(x)%2==0 else False)(self.n))
        return (lambda x: True if len(x)%2==0 else False)(self.n)

_test= Test1
_test2 = Test2('Once upon a time')
print(_test2._primary())
print(_test2._third())