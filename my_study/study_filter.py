'''
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
'''


def number():
    '''
    创建1个无限的数组列表
    :return: 返回一个生成器对象
    '''
    n = 0
    while True:
        n += 1
        yield n
        if (n == 1000):
            break


def findhui(x):
    '''
    从传递进来的值反向读取数字和原值做比较
    :param x: 原数值
    :return: 反向的数值
    '''
    y = str(x)
    if not y.isalnum():
        return 0
    z = ''
    for i in range(len(y)):
        z += y[-i - 1]
    if int(z) == x:
        return z


a = filter(findhui, number())
for fa in a:
    print(fa)
