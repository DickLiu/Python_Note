class a:
    def __init__(self):
        print('root')

    def get_form(self, s, obj=None, **kwargs):
        for i in kwargs:
            print(i, '=', kwargs[i])


class b(a):
    def __init__(self):
        super().__init__

    def get_form(self, s, obj=None, **kwargs):
        if obj is None:
            kwargs['form']='mimi'
        return super().get_form(s, obj, **kwargs)

'''
super()是依據__mro__去決定調用的對象
不一定總是parent class
以上例而言
b.__mro__會是
(<class '__main__.b'>, <class '__main__.a'>, <class 'object'>)

如果建立1個b class的instance叫做s如下
>>> s = b()
>>> s.get_form('k', form='sky')
form = mimi

因為s.get_form()在b class中會override原有a class的get_form()
ovveride的內容是當obj為None時，將kwargs中form的value改成'mimi'
最後又透過super()去調用a class中的get_form()
這時候pass給a.get_form()的
s沒有變、obj依舊為None，但是kwargs中form的value已經被改寫成'mimi'了
'''
