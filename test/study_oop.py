'''
面向对象的练习
'''

import functools


def int2(x, base=2):
    return int(x, base=base)


int2 = functools.partial(int, base=2)  # 偏函数可以固定某些参数

print(int2('10010'))


class student(object):
    '''
    面向对象的练习
    '''

    def __init__(self, name, score):
        '''
        内置函数（特殊方法）：构造函数
        '''
        self.name = name
        self.score = score
        self.__grade1()

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

    def __grade1(self):
        '''
        私有函数
        '''
        if self.score >= 90:
            self.__grade = 'A'  # 私有变量
        elif self.score >= 60:
            self.__grade = 'B'
        else:
            self.__grade = 'C'

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade
        return self.__grade


bart = student('leonard', 99)
print(bart.name)
print(bart.score)
bart.print_score()
print(bart.get_grade())
bart.set_grade('D')
print(bart.get_grade())
