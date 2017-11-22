class Mylist(object):
    # __mylist = []
    def __init__(self, *args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] += x

    def __sub__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] -= x

    def __mul__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] *= x

    def __mod__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / x

    def get_mylist(self):
        return self.__mylist


l = Mylist(1, 2, 3, 4, 5)
print(l.get_mylist())

a = l + 20
print(l.get_mylist())

l - 10
print(l.get_mylist())

l * 3
print(l.get_mylist())
