'''
装饰器，切面编程
'''
import functools
import time


def deco(func):
    '''
    假如没有dec这个闭包函数，则在下面运行过程中，遇到@就会直接执行装饰器函数里的逻辑
    '''

    @functools.wraps(func)
    def dec():
        startT = time.time()
        func()
        endT = time.time()
        msecs = (endT - startT)
        print('%s it\'s: %f ms' % (func.__name__, msecs))
        return func

    return dec


@deco
def fa():
    print('start')
    time.sleep(1.7)
    print('end')


'''相当于fb = deco(fb)'''


@deco
def fb():
    print('开始')
    time.sleep(1)
    print('结束')


fb()


def logging(text):
    '''
    装饰器函数如果要传递参数：text，则要在装饰器函数上定义一个高阶函数logging,将参数传递到logging中
    :param text:
    :return:
    '''

    def deco(func):
        '''
        如果不加下面这句，那么fc.__name__就会被传递为logtext，加上下面这句后，fc.__name__不会有变化
        '''

        @functools.wraps(func)
        def logtext():
            startT = time.time()
            func()
            endT = time.time()
            msecs = (endT - startT)
            print('%s it\'s: %f ms\n %s' % (func.__name__, msecs, text))
            return func

        return logtext

    return deco


@logging('leonard_tia')  # 相当于：fc = logging('leonard_tia')(fc)
def fc():
    print('01')
    time.sleep(0.5)
    print('02')


fc()
print(fc.__name__)
