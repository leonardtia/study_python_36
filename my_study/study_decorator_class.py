'''
装饰器带类参数
'''
import functools


class locker(object):
    def __init__(self):
        print(self.__name__, ' should be not called0')

    @staticmethod
    def acquire():
        print(locker.acquire.__name__, ' called2')

    @staticmethod
    def release():
        print(locker.release.__name__, ' called4')


def deco(cls):
    def _deco(func):
        @functools.wraps(func)
        def __deco():
            print('before %s called1 %s.' % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()

        return __deco

    return _deco


@deco(locker)
def myfunc():
    print(myfunc.__name__, ' called3')


myfunc()
myfunc()
