'''
学习__slots__,利用__slots__内置函数限制动态语言里实例的动态属性添加
'''
from types import MethodType


class studunt(object):
    pass


# 自定义一个函数
def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score


if __name__ == '__main__':
    s = studunt()
    s.name = 'leon'  # 动态给 实例 绑定一个属性
    print(s.name)
    s.set_age = MethodType(set_age, s)  # 动态给 实例 绑定一个方法
    s.set_age(25)
    print(s.age)
    s2 = studunt()

    studunt.set_score = set_score  # 动态给 类 绑定一个方法
    s.set_score(100)
    print(s.score)
    s2.set_score(99)
    print(s2.score)


# 如果要限制实例的属性，只允许对类的实例添加特定的属性
class teacher(object):
    __slots__ = ('name', 'age')


if __name__ == '__main__':
    a = teacher()
    a.name = 'leonard'
    a.age = 28
    # a.score = 99
    print(a.name, a.age)

    print(dir(teacher))
