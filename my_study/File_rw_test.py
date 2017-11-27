'''
请将本地一个文本文件读为一个str并打印出来：
'''
fpath = r'/Users/leonard_tia/PycharmProjects/py36/a'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

import os

print(os.name)
print(os.uname())
print(os.path.abspath('.'))  # 查看当前目录的绝对路径


# a = [x for x in os.listdir('/') ]
# print(a)
def dir1(path):
    # a = [x for x in os.listdir(path)]
    for i in os.listdir(path):
        if os.path.isfile(i) and os.path.splitext(i)[1] == '.py':
            yield i


pp = dir1('./')

for n in pp:
    print(n)

    # print(repr(pp))
