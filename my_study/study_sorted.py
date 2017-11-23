'''
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def sort(x):
    return x[0].lower()


L = sorted(l, key=sort)

for ll in L:
    print(ll)
