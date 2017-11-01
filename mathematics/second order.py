import numpy as np


def mybuild(equation):
    return np.array([int(x) for x in equation.split(',')])


one = input("please input equation one:")
onea = mybuild(one)
two = input("please input equation two:")
twoa = mybuild(two)
zz = zip(onea, twoa)
i = 0
for z in zz:
    if (i == 0):
        a = z
    elif (i == 1):
        b = z
    else:
        c = z
    i += 1
    print(z)
x = np.dot(c, b)
y = np.dot(a, c)
z = np.dot(a, b)
print(x, y, z)
