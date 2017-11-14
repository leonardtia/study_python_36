import random

import F_global as fg
from F_person import person


class build_nature(object):
    def nature(self, race, work, sex):
        '''
        1.雅族：智力(mp)平，体力(hp,atn)平，法力(it)平，幸运(kar)平'
        2.含族：智力(mp)平，体力(hp,atn)强，法力(it)弱，幸运(kar)高'
        3.闪族：智力(mp)高，体力(hp,atn)弱，法力(it)高，幸运(kar)弱'
        4.蛮族：智力(mp)弱，体力(hp,atn)强，法力(it)高，幸运(kar)平
        '''
        hcode = person.nature
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
        print('{},你现在是{}的{}{},你当前的生命力为{},武力为{},法力为{},法力值为{},幸运值为{}'.format(pp.name, fg.race_code[pp.race - 1],
                                                                           fg.sex_code[pp.sex - 1],
                                                                           fg.work_code[pp.work - 1], pp.nature['hp'],
                                                                           pp.nature['atn'],
                                                                           pp.nature['it'], pp.nature['mp'],
                                                                           pp.nature['kar']))
