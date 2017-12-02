
year_date = ['2017-10-01',
             '2015-04-01',
             '2013-01-01',
             '2011-02-01',
             '2008-09-01']
    

def map_date(a):    
    for i in  map(lambda d: (d, 'y'), a):
        print(i)

'''
if we call map_date(year_date)
the result will be
('2017-10-01', 'y')
('2015-04-01', 'y')
('2013-01-01', 'y')
('2011-02-01', 'y')
('2008-09-01', 'y')
'''


