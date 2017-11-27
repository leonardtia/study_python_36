'''
错误处理
'''
import logging

# logging用来记录错误日志，可以有ERROR,WARNING,INFO,DEBUG四种级别记录，用日志记录，不会抛出异常
logging.basicConfig(level=logging.INFO)


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) ** 2


def main():
    try:
        bar('0')
    # except Exception as e:
    finally:
        logging.warning('aaeeeeeee')


main()
print('END')


# 定义一个错误的class 使用继承 抛出错误的实例
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value %s' % s)
    return 10 / n


foo('0')
