'''
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
能在函数调用的前后打印出'begin call'和'end call'的日志。
'''
import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def fnk(*args, **kw):
        startTime = time.time()
        print('begin call')
        fn(*args, **kw)
        print('end call')
        endTime = time.time()
        st = endTime - startTime
        print('%s executed in %s ms' % (fn.__name__, st))
        return fn(*args, **kw)

    return fnk


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print(f, s)
