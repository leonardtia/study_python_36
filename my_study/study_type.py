'''
元类学习
'''


class leonard(object):
    def hello(self, name='world'):
        print('hello %s.' % name)


def fn(self, name='ttt'):
    print('hello ,%s' % name)


# 动态创建类
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了元祖（tuple）里，单个元素，是用（x,）来表示；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
abc = type('ttnd', (object,), dict(tt=fn))

a = abc()
a.tt('ooo')
