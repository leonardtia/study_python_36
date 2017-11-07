import random

pname = ('小王', '小李', '小田', '小吕', '小陈', '小明')
psex = ('男', '女')
pgood = ('礼', '乐', '射', '御', '书', '数')
page = (18, 19, 20, 28, 29, 30, 38, 39, 40)
ml = []


def createUser(nl):
    i = random.randint(0, 5)
    name = input('name:')
    if name:
        pass
    else:
        name = pname[i]
    i = random.randint(0, 1)
    sex = input('sex:')
    if sex:
        pass
    else:
        sex = psex[i]
    i = random.randint(0, 5)
    good = input('good:')
    if good:
        pass
    else:
        good = pgood[i]
    i = random.randint(0, 8)
    age = input('age:')
    if age:
        age = int(age)
    else:
        age = page[i]

    nl.append(name)
    nl.append(sex)
    nl.append(good)
    nl.append(age)
    return nl


def find(ml):
    id = input('please input id:')
    if id:
        id = int(id)
    else:
        id = random.randint(0, len(ml) - 1)
    print('id=', id)
    return ml[id]


def delete(ml):
    id = input('please input delete id:')
    if id or int(id) >= random.randint(0, len(ml) - 1):
        id = int(id)
    else:
        id = random.randint(0, len(ml) - 1)
    return ml.pop(id)


def set(ml):
    l = find(ml)
    name = input('name:')
    if name:
        l[1] = name
    else:
        l[1] = pname[random.randint(0, 5)]
    return l


active = input('please input add/del/set/find:')
while active != 'end':
    nl = []
    if active == 'add':
        nl = []
        nl = createUser(nl)
        ml.append(nl)
        i = ml.index(nl)
        ml[i].insert(0, i)
        print('add:', ml[i])
    elif active == 'del':
        nl = delete(ml)
        print('del:', nl)
    elif active == 'set':
        nl = set(ml)
        print('set:', nl)
    elif active == 'find':
        nl = find(ml)
        print('find:', nl)
    active = input('please input add/del/set/find:')
print(ml)
