import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


'''
print()回傳的是args.accumulate作用在args.integers的結果

>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='?', const='c', default='d')
>>> parser.add_argument('bar', nargs='?', default='d')

>>> parser.parse_args(['XX', '--foo', 'YY'])
Namespace(bar='XX', foo='YY')

>>> parser.parse_args(['XX', '--foo'])
Namespace(bar='XX', foo='c')   #produce value of const

>>> parser.parse_args([])
Namespace(bar='d', foo='d') #produce value of default

可以從上例看出，有option string(--foo)時，但後面無跟隨任何arguments時，
會produce的是const value。
但如果連option string(--foo)都沒有時，會produce default的value

所以回到我們的例子，當沒有option string(--sum)時，accumulate的值會是
default的max，args.accumulate(args.integers)就會是max(args.integers)，
如果有option string(--sum)時，store const的結果就會是將sum assign給accumulate，
所以args.accumulate(args.integers)就會是sum(args.integers)
'''


