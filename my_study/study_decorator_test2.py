'''
写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：
@log('execute')
def f():
    pass
'''


def log(*arg):
    def decorator(fn):
        def warp(*arg):
            if arg:
                print(arg[0])
            return fn(*arg)

        return warp

    return decorator


@log
def f():
    print('abc')


@log('leo')
def g(b):
    print('aaa', b)


# f()
g('bbb')
