'''
Lost Beta 0.4
作者：leonard
时间：2017-11-09
创建角色
初始化角色属性
初始化地图
主菜单
地图指令
主程序
优化地图指令
打印地图及当前位置
初始化姓名，使用姓名字典文件，并且按性别自动生成姓名
人物优化
'''
import random

race_code = ('雅族', '含族', '闪族', '蛮族')
work_code = ('战士', '法师', '牧师', '盗贼')
sex_code = ('男性', '女性', '无性')
point_code = {'w': '北方死沼泽', 's': '南方幽暗林', 'a': '西方梦之丘', 'd': '东方昆仑墟'}
menu = {1: '显示状态', 2: '检查装备', 3: '进入地图', 4: '存档', 5: '退出Lost'}
po = (0, 0)
_path = ''


class person(object):
    name = ''
    race = 0
    work = 0
    sex = 0
    nature = {}

map_x = [i for i in range(-9, 10)]
map_y = [j for j in range(-9, 10)]
mmap = []
for i in map_x:
    j = 0
    for j in map_y:
        mmap.append((i, j))

class buildplayer():
    def player1(self):
        self.player = person()
        name = input('请输入你的角色的名字：')
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
        self.player.race = race
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
        self.player.work = work
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
        self.player.sex = sex
        print('你选择的性别是：{}'.format(sex_code[sex - 1]))
        if name:
            pass
        else:
            name = self.getName(sex)
        self.player.name = name
        bn = build_nature()
        self.player.nature = bn.nature(race=race, work=work, sex=sex)
        print('{}，欢迎你进入到Lost世界，请小心，这里处处充满着危险！'.format(self.player.name))
        return self.player

    def create_player(self, s='s'):
        person1 = person()
        while s is 's':
            person1 = self.player1()
            bn = build_nature()
            bn.showuserinfo(person1)
            s = input('如果要重新生成角色，请按：s 键：')
            self.create_player(s)
        return person1

    def create_username(self, sex):
        with open(_path + 'family_name.txt', 'r') as text:
            self.family_name = text.read().split()
        text.close
        if sex == 1:
            with open(_path + 'secound_name_2.txt', 'r') as text:
                self.secound_name = text.read().split()
            text.close
        elif sex == 2:
            with open(_path + 'secound_name.txt', 'r') as text:
                self.secound_name = text.read().split()
            text.close
        elif sex == 3:
            with open(_path + 'secound_name_3.txt', 'r') as text:
                self.secound_name = text.read().split()
            text.close

    def getName(self, sex):
        self.create_username(sex)
        familyname = random.choice(self.family_name)
        secountd = random.choice(self.secound_name)
        all_name = "{}{}".format(familyname, secountd)
        return all_name
class welcome(object):
    def __init__(self):
        print('剑气分还合，荷珠碎复圆。万般皆是命，半点尽由天！')
        print('----------------------------------------')
        print('欢迎开始Lost迷失之旅！')
        print('leonard Beta 0.3')
        print('2017-11-08')
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
        print('{},你现在是{}的{}{},你当前的生命力为{},武力为{},法力为{},法力值为{},幸运值为{}'.format(pp.name, race_code[pp.race - 1],
                                                                           sex_code[pp.sex - 1],
                                                                           work_code[pp.work - 1], pp.nature['hp'],
                                                                           pp.nature['atn'],
                                                                           pp.nature['it'], pp.nature['mp'],
                                                                           pp.nature['kar']))

class map(object):
    def getpoint(self, point, bushu, po):
        x = po[0]
        y = po[1]
        m = '向%s的路已经到达尽头，回头是岸'
        m1 = m % (point_code[point])
        if point == 's' or point == 'a':
            bushu = -bushu
        if point == 'w' or point == 's':
            if (abs(y + bushu) <= max(map_y)):
                y = y + bushu
            else:
                print(m1)
        elif point == 'a' or point == 'd':
            if (abs(x + bushu) <= max(map_y)):
                x = x + bushu
            else:
                print(m1)
        po = (x, y)
        return po

    def intomap(self, po, point='s'):
        while 2 != 1:
            while po in mmap:
                point = input('请选择你要移动的方向或指令：')
                if point == 'q' or point == 'i' or point == 'o':
                    break
                elif point not in point_code.keys():
                    yidong = '向%s移动(%s键),'
                    yd = ''
                    for k, v in point_code.items():
                        yd += yidong % (v, k)
                    print('移动方式：', yd, '\n显示地图(i键),显示当前坐标值(o键),退出地图(q键)')
                    continue
                po = self.getpoint(point, random.randint(1, 3), po)
            if point == 'i':
                self.showmap(po)
                self.intomap(po)
            if point == 'o':
                print('你当前的坐标值是：', po)
            elif point == 'q':
                print('退出地图')
                break
        return po

    def showmap(self, po):
        for y in map_y:
            x = '#' * len(map_x)
            if y == -po[1]:  # 因为根据循环，y轴打印从第一行开始，此时y轴是负数，但是在地图中坐标又是正数
                x = ''
                for xx in map_x:
                    if xx == po[0]:
                        x += '@'
                        continue
                    x += '#'
            print(x, '\n')



class main(welcome):
    def main_menu(self):
        print('指令菜单:')
        for k, v in menu.items():
            print(k, '.', v)

    def main_start(self, active, po, pp):
        if menu.get(active, '请输入正确的菜单项') == '进入地图':
            yidong = '向%s移动(%s键),'
            yd = ''
            for k, v in point_code.items():
                yd += yidong % (v, k)
            print('移动方式：', yd, '\n显示地图(i键),显示当前坐标值(o键),退出地图(q键)')
            map1 = map()
            po = map1.intomap(po)
        elif menu.get(active, '请输入正确的菜单项') == '显示状态':
            bn = build_nature()
            bn.showuserinfo(pp)
        elif menu.get(active, '请输入正确的菜单项') == '检查装备':
            pass
        elif menu.get(active, '请输入正确的菜单项') == '存档':
            pass
        elif menu.get(active, '请输入正确的菜单项') == '退出Lost':
            pass
        return po

game = main()
active = 0
bp = buildplayer()
person = bp.create_player('s')
print('冒险正式开始!')
while int(active) != 5:
    print('--------start---------')
    game.main_menu()
    active = input()
    if not active:
        game.main_menu()
    po = game.main_start(int(active), po, person)
