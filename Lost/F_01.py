'''
Lost Beta 0.1
作者：leonard
时间：2017-11-06
创建角色
初始化角色属性
初始化地图
'''
import random

race_code = ('雅族', '含族', '闪族', '蛮族')
work_code = ('战士', '法师', '牧师', '盗贼')
sex_code = ('男性', '女性', '无性')
point_code = ('w', 's', 'a', 'd')
menu = {1: '显示状态', 2: '检查装备', 3: '进入地图', 4: '存档', 5: '退出Lost'}
person = {}

map_x = [i for i in range(-12, 12)]
map_y = [j for j in range(-12, 12)]
mmap = []
for i in map_x:
    j = 0
    for j in map_y:
        mmap.append((i, j))

class welcome(object):
    def __init__(self):
        print('剑气分还合，荷珠碎复圆。万般皆是命，半点尽由天！')
        print('----------------------------------------')
        print('欢迎开始Lost迷失之旅！')
        print('leonard Beta 0.1')
        print('2017-11-06')
        print('----------------------------------------')


class build_nature(object):
    def nature(self, race, work, sex):
        hcode = {'hp': 0, 'mp': 0, 'atn': 0, 'it': 0, 'kar': 0}
        '''
        1.雅族：智力(mp)平，体力(hp,atn)平，法力(it)平，幸运(kar)平'
        2.含族：智力(mp)平，体力(hp,atn)强，法力(it)弱，幸运(kar)高'
        3.闪族：智力(mp)高，体力(hp,atn)弱，法力(it)高，幸运(kar)弱'
        4.蛮族：智力(mp)弱，体力(hp,atn)强，法力(it)高，幸运(kar)平
        '''
        if race == 1:
            hcode['hp'] = random.randint(70, 91)  # 生命力
            hcode['mp'] = random.randint(70, 91)  # 法力
            hcode['atn'] = random.randint(70, 91)  # 物理攻击力
            hcode['it'] = random.randint(70, 91)  # 法术攻击力
            hcode['kar'] = random.randint(60, 81)  # 幸运力
        elif race == 2:
            hcode['hp'] = random.randint(80, 101)  # 生命力
            hcode['mp'] = random.randint(50, 71)  # 法力
            hcode['atn'] = random.randint(70, 91)  # 物理攻击力
            hcode['it'] = random.randint(60, 81)  # 法术攻击力
            hcode['kar'] = random.randint(80, 101)  # 幸运力
        elif race == 3:
            hcode['hp'] = random.randint(70, 91)  # 生命力
            hcode['mp'] = random.randint(80, 101)  # 法力
            hcode['atn'] = random.randint(60, 81)  # 物理攻击力
            hcode['it'] = random.randint(80, 101)  # 法术攻击力
            hcode['kar'] = random.randint(50, 71)  # 幸运力
        elif race == 4:
            hcode['hp'] = random.randint(80, 101)  # 生命力
            hcode['mp'] = random.randint(70, 91)  # 法力
            hcode['atn'] = random.randint(80, 101)  # 物理攻击力
            hcode['it'] = random.randint(50, 71)  # 法术攻击力
            hcode['kar'] = random.randint(60, 81)  # 幸运力

        def wok(work, hc):
            if work == 1:
                hc['hp'] += 15
                hc['atn'] += 20
                hc['it'] -= 30
            elif work == 2:
                hc['mp'] += 15
                hc['it'] += 20
                hc['atn'] -= 30
            elif work == 3:
                hc['hp'] += 20
                hc['mp'] += 15
                hc['it'] -= 15
                hc['atn'] -= 15
            elif work == 4:
                hc['atn'] += 20
                hc['kar'] += 15
                hc['it'] -= 15
                hc['hp'] -= 15
            return hc

        def sex1(sex, hc):
            if sex == 1:
                hc['hp'] += 5
                hc['atn'] += 5
            elif sex == 2:
                hc['kar'] += 5
                hc['mp'] += 5
            elif sex == 3:
                hc['it'] += 5
                hc['hp'] += 5
            return hc

        hcode = wok(work, hcode)
        hcode = sex1(sex=sex, hc=hcode)
        return hcode

    def showuserinfo(self, pp):
        print('你现在是{}的{}{},你当前的生命力为{},武力为{},法力为{},法力值为{},幸运值为{}'.format(race_code[pp['种族'] - 1], sex_code[pp['性别'] - 1],
                                                                        work_code[pp['职业'] - 1], pp['属性']['hp'],
                                                                        pp['属性']['atn'],
                                                                        pp['属性']['it'], pp['属性']['mp'],
                                                                        pp['属性']['kar']))


class buildplayer():
    def player1(self):
        player = {}
        name = input('请输入你的角色的名字：')
        if name:
            pass
        else:
            name = '玩家' + str(random.randint(1, 9999))
        player['名字'] = name
        print('你的角色的名字是：', player['名字'])
        print('请选择你所属的种族：')
        i = 1
        for r in race_code:
            print(i, '.', r)
            i += 1
        race = input('请从（1-4）项里选择1项')
        if race:
            if eval(race) in [1, 4]:
                pass
        else:
            race = random.randint(1, 4)
        player['种族'] = race
        print('你选择的种族是：{}'.format(race_code[race - 1]))
        print('请选择你所属的职业：')
        i = 1
        for w in work_code:
            print(1, '.', w)
            i += 1
        work = input('请从（1-4）项里选择1项')
        if work:
            if eval(work) in [1, 4]:
                pass
        else:
            work = random.randint(1, 4)
        player['职业'] = work
        print('你选择的职业是：{}'.format(work_code[work - 1]))
        print('请选择你的性别：')
        i = 1
        for s in sex_code:
            print(i, '.', s)
            i += 1
        sex = input('请从（1-3）项里选择1项')
        if not sex or eval(sex) not in [1, 3]:
            sex = random.randint(1, 3)
        else:
            pass
        player['性别'] = sex
        print('你选择的性别是：{}'.format(sex_code[sex - 1]))
        bn = build_nature()
        player['属性'] = bn.nature(race=race, work=work, sex=sex)
        print('{}，欢迎你进入到Lost世界，请小心，这里处处充满着危险！'.format(player['名字']))
        return player

    def create_player(self, s='s'):
        person1 = {}
        while s is 's':
            person1 = self.player1()
            bn = build_nature()
            bn.showuserinfo(person1)
            s = input('如果要重新生成角色，请按：s 键：')
            self.create_player(s)
        return person1


class map(object):
    def getpoint(self, point, bushu, po):
        x = po[0]
        y = po[1]
        if point == 'w':
            x = x + bushu
        if point == 's':
            x = x - bushu
        if point == 'a':
            y = y - bushu
        if point == 'd':
            y = y + bushu
        po = (x, y)
        return po

    def intomap(self, po, point='s'):
        while po in mmap or point != 'q':
            point = input('请选择你要移动的方向：')
            if not point or point not in point_code:
                point = point_code[random.randint(0, 3)]
            bushu = random.randint(1, 3)
            po = self.getpoint(point, bushu, po)
        print('你当前的位置是：', po)


class main(welcome):
    def main_start(self):
        bp = buildplayer()
        person = bp.create_player('s')
        print('游戏正式开始！\n --------start---------')
        po = (0, 0)
        print('指令菜单:')
        for k, v in menu.items():
            print(k, '.', v)
        active = input()
        if not active or int(active) not in menu.keys():
            active = 3
        else:
            active = int(active)
        if menu.get(active) == '进入地图':
            print('移动方式：向北移动(w键),向南移动(s键),向西移动(a键),向东移动(d键),退出地图(q键)')
            map1 = map()
            map1.intomap(po)
        elif menu.get(active) == '显示状态':
            bn = build_nature()
            bn.showuserinfo(person)
        elif menu.get(active) == '检查装备':
            pass
        elif menu.get(active) == '存档':
            pass
        elif menu.get(active) == '退出Lost':
            pass


game = main()
game.main_start()
