s = 'my name is leonard'
print(s[:])
print(s[1:10:1])
print(s[1:10:2])

ss = '%s is ten %d'
print(ss % ('leo', 4))
t = ss.__add__(s)
print(t)
l = '1,2,3,4,5,6,7'
ll = l.split(',')
print(ll)
lll = ','.join(ll)
print(lll)
j = 0
for i in range(1, 101):
    j = i + j
print(j)
j = 0
for h in range(1, 1000):
    if (h % 3 == 0) or (h % 5 == 0):
        k = h
        j = k + j
        # print(k)
print(j)
s = [h for h in range(1, 1000000) if (h % 3 == 0) or (h % 5 == 0)]  # 列表表达式
t = (h for h in range(1, 1000000) if (h % 3 == 0) or (h % 5 == 0))  # 生成器表达式
print(sum(s))
print(sum(t))

b = int(input('please input bingbao:'))
s = []
while b != 1:
    if b % 2 == 0:
        b = b / 2
    else:
        b = b * 3 + 1
    s.append(b)
print(s)

m = [1, 2, 3, 4, 5, 6, 7]
l = []
for n in m:
    l.append(n)
print(l)
print(id(m))

t = set('12345')
print(t)


def tt(x, y):
    print('%s 是 %d 的好人' % (x, y))


l = ['leo', 3]
p = {'x': 'leo', 'y': 3}
tt(*l)  # 传参是list
tt(**p)  # 传参是dict


# 函数的冗余处理，list
def ss(x, y, *z):
    print('%s是%d的的%s人%s' % (x, y, z[0], z[1]))


ss('leo', 3, 'jj', 'ii')


# 函数的冗余处理，dict
def sss(x, y, **z):
    print('%s是%d的%s的人%s' % (x, y, z.get('a'), z.get('b')))
    print(z)


sss('leo', 4, a='bomb', b='leonard')

ster = 'abcdefghijklmnopqrstuvwxyz1234567890'
stl = []
otl = ''
import random

for oss in ster:
    stl.append(ord(oss))
i = 0
while i <= 5:
    i += 1
    otl += chr(random.choice(stl))
print(otl)

import functools as ft


def a(x, y):
    return x * y


s = ft.reduce(a, [1, 2, 3, 4, 5, 6])
print(s)
f = lambda x, y: x * y
print(f(2, 3))
s = ft.reduce(lambda x, y: x * y, [1, 2, 3, 4])
s = ft.reduce(f, [1, 2, 3, 4, 5])
print(s)
lis = [1, 2, 3, 4, 5, 6, 7, 8]
fi = filter(lambda x: x % 3 == 0, lis)
for i in fi:
    print('fi', i)

ma = map(lambda x: x * 2 + 10, lis)
for m in ma:
    print('ma', m)

x = 0
y = 1
fblq = [x]
'''for i in range(10):
    z = x
    x = y
    y = z + y
    fblq.append(y)'''
for k in range(10):
    print(y)
    x, y = y, x + y
print(fblq)


def fblq():
    x = 0
    y = 1
    for k in range(100):
        x, y = y, x + y
        yield y


for a in fblq():
    print('fblq:', a)


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x11: x11 % n > 0


def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in prime():
    if n < 100:
        print(n)
    else:
        break


def odd():
    a = 's1'
    print(a)
    yield a + '-1'
    a = 's2'
    print(a)
    yield a + '-2'
    a = 's3'
    print(a)
    yield a + '-3'


o = odd()
print('1-', next(o))
print('2-', next(o))
print('3-', next(o))
