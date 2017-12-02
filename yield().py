from itertools import chain

def foo_yield(x):
    i = 1
    while i <= x:
        yield range(0, i)
        i += 1

'''
if you call foo_yield(4)
you will get a generator object
then you can call
for i in chain.from_iterable(foo_yield(4)):
    print(i)
and you will get evaluated result below:
0
0
1
0
1
2
0
1
2
3
'''
'''
or you can call without chain() method
for i in foo_yield_from(4):
    print(i)
istead, which implement yield from expression for generator delegation.
since Python 3.3
'''    

def foo_yield_from(x):
    i = 1
    while i <= x:
        yield from range(0, i)
        i += 1

