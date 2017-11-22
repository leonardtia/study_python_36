'''
@property学习,利用@property定义属性的可读和可写.setter,如果不定义.setter，那么这个属性只能只读
'''


class student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score muset between 0 ~ 100')
        self._score = value


if __name__ == '__main__':
    s = student()
    s.score = 60
    print(s.score)
    s.score = 600
