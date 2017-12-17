import math
import random

class Circle(object):
    version = '0.5b'

    __slots__ = ('radius')

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter
    
class Tire(Circle):

    def perimeter(self):
        return Circle.perimeter(self) * 1.25

    __perimeter = perimeter


circles = (Circle(random.randint(1,99)) for i in range(1000))
dict_list = []
for i in circles:
    dict_list.append(i)

print(dict_list)
    

'''
name mangling的原始意圖並不只是private purpose
而是讓base class在多重繼承的情況下
能夠避免與subclass產生衝突，在上述的程式碼即便Tire這個subclass有
speicify __perimeter = perimeter
但如果我們建立一個Tire() instance如下:
>>> a = Tire(1)
>>> a.area()
3.1416
會去執行Circle()中的perimeter method而不是Tire()中的perimeter method
詳見於此: https://goo.gl/Geb5LN

但如果我們只是使用single underscore的non-public variable(並不會有name mangling的效果)
就會呼叫到Tire()的perimeter method而非Circle()的perimeter method
>>> a = Tire(1)
>>> a.area()
4.9087
詳見於此: https://goo.gl/C7k9HP

參考資料:N. (2013, March 20). Retrieved December 14, 2017,
from https://www.youtube.com/watch?v=HTLu2DFOdTg
'''
