'''
装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器
'''
import functools


class mylocker:
    def __init__(self):
        print(self.__name__, ' called0')

    @staticmethod
    def acquire():
        print(mylocker.acquire.__name__, ' mylocker.acquire called2')

    @staticmethod
    def unlock():
        print(mylocker.unlock.__name__, ' mylocker.unlock.called4')


class lockrex(mylocker):
    @staticmethod
    def acquire():
        print(lockrex.acquire.__name__, ' lockrex.acquire.called3')

    @staticmethod
    def unlock():
        print(lockrex.unlock.__name__, ' lockrex.unlock.called5')


def lockhelper(cls):
    def _deco(func):
        @functools.wraps(func)
        def __deco(*args, **kwargs):
            print('before %s called1.' % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return __deco

    return _deco


# 调用装饰器类
class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print(example.myfunc.__name__, ' example.myfunc.called3')

    @lockhelper(mylocker)
    @lockhelper(lockrex)
    def myfunc2(self, a, b):
        print(example.myfunc2.__name__, ' example.myfunc2.called3')
        return a + b


if __name__ == '__main__':
    a = example()
    # a.myfunc()
    # print(a.myfunc())
    print(a.myfunc2(1, 2))
    # print(a.myfunc2(3,4))
