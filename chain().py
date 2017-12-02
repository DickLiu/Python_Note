from itertools import chain


def chain_test(*args):
    for i in chain(args):
        print(i ,end=' ')


'''
if we call

chain_test([1,2,3],['a'],('a'))

the result will be

[1, 2, 3] ['a'] a

'''
