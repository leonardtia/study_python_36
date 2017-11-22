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

    def show(self):
        print(self.__mylist)


l = Mylist(1, 2, 3, 4, 5)
l.show()

a = l + 20
l.show()

l - 10
l.show()

l * 3
l.show()

l / 3
l.show()
