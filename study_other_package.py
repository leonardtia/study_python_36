import sys

print(sys.path[3])

x = [1, 2, 3]
y = [2, 4]
print(x is not y)
del x[2]
y[1] = 1
print(y)
y.reverse()  # 反向队列
print(x == y)
print(x is y)

for number in range(1, 101):
    print(number)

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
zip(names, ages)
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
for aa in zip(names, ages):
    print(aa)

i = 0
strings = ['aaaa1', 'xxx', 'bbbb1', 'xxx', 'cccc1', 'xxx', 'dddd1']
for string in strings:
    if 'xxx' in string:
        strings[i] = '0'
    i += 1
print(strings)

for i, string in enumerate(strings):  # 枚举化
    if '0' in string:
        strings[i] = 'xxx'
print(strings)

print(sorted([4, 5, 3, 4, 2, 6]))  # 列表排序
print(sorted('leonard_tia'))
print(list(reversed('leonard_tia')))  # 倒排序，并生成列表
print(''.join(reversed('leonard_tia')))

a = [x for x in range(1, 100) if x % 2 == 0]
print(a)
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)  # 取girls里的单词的首字母作为键值，单词作为值插入到字典里
print(letterGirls)
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])
exec("print('aaa')")

eval("raw_input('Enter an arithmetic expression:')")
