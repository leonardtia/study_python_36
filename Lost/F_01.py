'''
Lost Beta 0.1
作者：leonard
时间：2017-11-06
创建角色
初始化角色属性
初始化地图
'''
import random

race_code = ['雅族', '含族', '闪族', '蛮族']
work_code = ['战士', '法师', '牧师', '盗贼']


class welcome(object):
    def __init__(self):
        print('剑气分还合，荷珠碎复圆。万般皆是命，半点尽由天！')
        print('----------------------------------------')
        print('欢迎开始Lost迷失之旅！')
        print('leonard Beta 0.1')
        print('2017-11-06')
        print('----------------------------------------')


class build_nature(object):
    def nature(self, race, work):
        hcode = {'hp': 0, 'mp': 0, 'atn': 0, 'it': 0, 'kar': 0}
        '''
        1.雅族：智力(mp)平，体力(hp,atn)平，法力(it)平，幸运(kar)平'
        2.含族：智力(mp)平，体力(hp,atn)强，法力(it)弱，幸运(kar)高'
        3.闪族：智力(mp)高，体力(hp,atn)弱，法力(it)高，幸运(kar)弱'
        4.蛮族：智力(mp)弱，体力(hp,atn)强，法力(it)高，幸运(kar)平
        '''
        if race == 1:
            hcode['hp'] = random.randint(60, 101)  # 生命力
            hcode['mp'] = random.randint(70, 101)  # 法力
            hcode['atn'] = random.randint(60, 101)  # 物理攻击力
            hcode['it'] = random.randint(70, 111)  # 法术攻击力
            hcode['kar'] = random.randint(60, 101)  # 幸运力
        elif race == 2:
            hcode['hp'] = random.randint(90, 150)  # 生命力
            hcode['mp'] = random.randint(30, 91)  # 法力
            hcode['atn'] = random.randint(90, 150)  # 物理攻击力
            hcode['it'] = random.randint(60, 101)  # 法术攻击力
            hcode['kar'] = random.randint(90, 150)  # 幸运力
        elif race == 3:
            hcode['hp'] = random.randint(60, 91)  # 生命力
            hcode['mp'] = random.randint(90, 150)  # 法力
            hcode['atn'] = random.randint(60, 101)  # 物理攻击力
            hcode['it'] = random.randint(90, 150)  # 法术攻击力
            hcode['kar'] = random.randint(30, 91)  # 幸运力
        elif race == 4:
            hcode['hp'] = random.randint(90, 150)  # 生命力
            hcode['mp'] = random.randint(90, 150)  # 法力
            hcode['atn'] = random.randint(90, 150)  # 物理攻击力
            hcode['it'] = random.randint(30, 91)  # 法术攻击力
            hcode['kar'] = random.randint(60, 101)  # 幸运力

        def wok(self, work, hc):
            if work == 1:
                hc['hp'] += 10
                hc['atn'] += 15
                hc['it'] -= 25
            elif work == 2:
                hc['mp'] += 10
                hc['it'] += 15
                hc['atn'] -= 25
            elif work == 3:
                hc['hp'] += 10
                hc['mp'] += 10
                hc['it'] -= 10
                hc['atn'] -= 10
            elif work == 4:
                hc['atn'] += 10
                hc['kar'] += 10
                hc['it'] -= 10
                hc['hp'] -= 10
            return hc

        hcode1 = wok(self, work, hcode)
        return hcode1


class buildplayer(welcome):
    def player1(self):
        player = []
        name = input('请输入你的角色名字：')
        if name:
            pass
        else:
            name = '玩家' + str(random.randint(1, 9999))
        player.append(name)
        print('请选择你所属的种族：')
        print('1.雅族')
        print('2.含族')
        print('3.闪族')
        print('4.蛮族')
        race = input('请从（1-4）项里选择1项')
        if race:
            if eval(race) in [1, 4]:
                pass
        else:
            race = random.randint(1, 4)
        player.append(race)
        print('系统帮你选择的种族是：{}'.format(race_code[race - 1]))
        print('请选择你所属的职业：')
        print('1.战士')
        print('2.法师')
        print('3.牧师')
        print('4.盗贼')
        work = input('请从（1-4）项里选择1项')
        if work:
            if eval(work) in [1, 4]:
                pass
        else:
            work = random.randint(1, 4)
        player.append(work)
        print('系统帮你选择的职业是：{}'.format(work_code[work - 1]))
        bn = build_nature()
        player.append(bn.nature(race=race, work=work))
        print('{}，欢迎你进入到Lost世界，请小心，这里处处充满着危险！'.format(player[0]))
        return player


def create_player(s='s'):
    if s is 's':
        my = buildplayer()
        pp = my.player1()
        print('你现在是{}的{},你当前的生命力为{},武力为{},法力为{},法力值为{},幸运值为{}'.format(race_code[pp[1] - 1], work_code[pp[2] - 1],
                                                                      pp[3]['hp'], pp[3]['atn'], pp[3]['it'],
                                                                      pp[3]['mp'], pp[3]['hp']))
    s = input('如果要重新生成，请按：s 键：')
    create_player(s)


create_player()
