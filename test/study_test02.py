a = ['adam', 'LISA', 'basT']
t = 'abcdefghijklmnopqrstuvwxyz'
T = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 生成小写字母的集合tlist
tlist = []
for i, ct in enumerate(t):
    tlist.append(ord(ct))
# 生成大写字母的集合Tlist
Tlist = []
for i, cT in enumerate(T):
    Tlist.append(ord(cT))
print(tlist)
print(Tlist)
print(tlist[0] - Tlist[0])


def tolowerchar(c):
    x = ''
    for i, c in enumerate(c):
        n = ord(c)
        if n > 90:
            pass
        else:
            n += 32
        x += chr(n)
    return x.capitalize()


def firstchar(c):
    return c.replace(c[0], chr(ord(c[0]) - 32))


m = map(tolowerchar, a)
for _m in m:
    print(_m)
