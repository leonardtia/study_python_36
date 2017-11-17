from functools import reduce


def ppa(x, y):
    return x * y


def prod(L):
    print(reduce(ppa, L))


prod([1, 3, 5, 7, 9])


def chartoint(x):
    '''将字符串转化成数字数组..ok'''
    l = []
    for i, c in enumerate(x):
        l.append(int(c))
    return l


def strtoint(x):
    '''将字符串转化成数字'''
    ccc = chartoint(x)
    r = reduce(lambda x, y: x * 10 + y, ccc)
    return r


def strtofll(x):
    '''将字符串转化成浮点数'''
    ccc = chartoint(x)
    a = map(lambda x: x * pow(0.1, len(ccc)), ccc)
    r = reduce(lambda x, y: x * 10 + y, a)
    return r


print(strtoint('0'))
print(strtoint('50'))
print(strtoint('1234'))


def strtonum(x):
    return reduce(lambda x, y: x * 10 + y, x)


def strtofloat(x):
    if x.find('.') >= 0:
        s = str.split(x, '.')
        ccc = chartoint(s[0])
        ccc1 = chartoint(s[1])
        r = strtonum(ccc)
        ccc2 = map(lambda x: x * pow(0.1, len(ccc1)), ccc1)
        r1 = strtonum(ccc2)
        sf = r + r1
        return sf


print(strtofloat('123.456'))
print(strtofloat('3.45'))
