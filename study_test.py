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

t = set(1, 2, 3, 4, 5)
print(t)
