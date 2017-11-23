'''
继承与多态
falemale，male，child都是person的继承，但是falemale和male又分别重写了函数face
monkey不是person的继承，但是因为和person一样有face方法，所以可以当成同一种类型进行传递
'''


class person(object):
    def face(self):
        print('眼睛', '鼻子', '耳朵', '嘴', '眉毛')


class falemale(person):
    def face(self):  # 对父类的方法进行重载
        print('带眼镜', '大嘴巴')


class male(person):
    def face(self):
        print('大眼睛', '小嘴巴')


class child(person):
    pass


class monkey(object):
    def face(self):
        print('毛茸茸')


def trueface(person):
    person.face()


trueface(person())
trueface(falemale())
trueface(male())
trueface(child())
trueface(monkey())
