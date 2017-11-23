class Mylist(object):
    # __mylist = []
    def __init__(self, *args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)

    def __str__(self):
        return str(self.__mylist)

    __repr__ = __str__

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


if __name__ == '__main__':
    l = Mylist(1, 2, 3, 4, 5)
    a = l + 20
    print(l)
    l - 10
    print(l)
    l * 3
    print(l)
