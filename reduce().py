from functools import reduce

a = [(1,'a',3),(2,'b',6),(3,'c',9),(4,'d',12)]

def special(x, y):
    i0 = x[0]+y[0]
    i1 = x[1]+y[1]
    i2 = x[2]*y[2]
    return(i0, i1, i2)
        

# result
'''
>>> b = reduce(special, a)
>>> print(b)
(10, 'abcd', 1944)
>>> 
'''

'''
explain
當你的程式看到很多次的
a = func(a, b)
a = func(a, c)
a = func(a, d)
或是
b = init_value
for value in value_list:
    b = func_handler(b, value)
那就轉用 reduce 吧。
'''

# use reduce() with Django's Q object

'''
Poll.objects.filter(
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)) |
    Q(question__startswith='Who')
)

if you operator.or_() and reduce(), you can make the above expression
change like below

from operator import or_

Poll.objects.filter(
    reduce(
        or_,
        [Q(pub_date=date(2005, 5, 2)), Q(pub_date=date(2005, 5, 6)),
        Q(question__startswith='Who'])
)

'''

