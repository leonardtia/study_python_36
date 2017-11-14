import random

import F_global as fg
from F_event import event_abc


class map(object):
    def __init__(self):
        for i in fg.map_x:
            j = 0
            for j in fg.map_y:
                fg.mmap.append((i, j))

    def getpoint(self, point, bushu, po):
        x = po[0]
        y = po[1]
        m = '向%s的路已经到达尽头，回头是岸'
        m1 = m % (fg.point_code[point])
        if point == 's' or point == 'a':
            bushu = -bushu
        if point == 'w' or point == 's':
            if (abs(y + bushu) <= max(fg.map_y)):
                y = y + bushu
            else:
                print(m1)
        elif point == 'a' or point == 'd':
            if (abs(x + bushu) <= max(fg.map_y)):
                x = x + bushu
            else:
                print(m1)
        po = (x, y)
        return po

    def intomap(self, po, person, point='s'):
        bo = True
        while bo:
            while po in fg.mmap:
                point = input('请选择你要移动的方向或指令：')
                if point == 'q' or point == 'i' or point == 'o':
                    break
                elif point not in fg.point_code.keys():
                    yidong = '向%s移动(%s键),'
                    yd = ''
                    for k, v in fg.point_code.items():
                        yd += yidong % (v, k)
                    print('移动方式：', yd, '\n显示地图(i键),显示当前坐标值(o键),退出地图(q键)')
                    continue
                fg.po = self.getpoint(point, random.randint(1, 3), fg.po)
                event = event_abc()
                bo = event.suijishijian(person)
                if not bo:
                    return bo
            if point == 'i':
                self.showmap(fg.po)
                self.intomap(fg.po)
            if point == 'o':
                print('你当前的坐标值是：', fg.po)
            elif point == 'q':
                print('退出地图')
                break
        return bo

    def showmap(self, po):
        for y in fg.map_y:
            x = '#' * len(fg.map_x)
            if y == -po[1]:  # 因为根据循环，y轴打印从第一行开始，此时y轴是负数，但是在地图中坐标又是正数
                x = ''
                for xx in fg.map_x:
                    if xx == po[0]:
                        x += '@'
                        continue
                    x += '#'
            print(x, '\n')
