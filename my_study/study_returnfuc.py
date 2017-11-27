'''
利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''
def createCounter():
    def ccc(j):
        def fff():
            return j + 1
        return fff
    fs = []
    for i in range(0, 4):
        fs.append(ccc(i))
    return fs

c1, c2, c3, c4 = createCounter()
print(c1(), c2(), c3(), c4())

def generate_counter():
    CNT = [0]
    def add_one():
        CNT[0] = CNT[0] + 1
        return CNT[0]
    return add_one

counter = generate_counter()
print(counter())
print(counter())
print(counter())
print(counter())

def abc():
    i = 0
    def add_one():
        nonlocal i
        i = i + 1
        return i

    return add_one

coun = abc()
print(coun(), coun(), coun(), coun())


def createcounter02():
    def _odd_iter():
        n = 0
        while True:
            n = n + 1
            yield n

    y = _odd_iter()

    def counter():
        return next(y)

    return counter


coo = createcounter02()
print(coo(), coo(), coo())
