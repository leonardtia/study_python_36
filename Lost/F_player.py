import os
import random

import F_global as fg
from F_nature import build_nature
from F_person import person


class buildplayer():
    def player1(self):
        self.player = person()
        name = input('请输入你的角色的名字：')
        print('请选择你所属的种族：')
        i = 1
        for r in fg.race_code:
            print(i, '.', r)
            i += 1
        race = input('请从（1-4）项里选择1项')
        if race:
            if eval(race) in [1, 4]:
                pass
        else:
            race = random.randint(1, 4)
        self.player.race = race
        print('你选择的种族是：{}'.format(fg.race_code[race - 1]))
        print('请选择你所属的职业：')
        i = 1
        for w in fg.work_code:
            print(1, '.', w)
            i += 1
        work = input('请从（1-4）项里选择1项')
        if work:
            if eval(work) in [1, 4]:
                pass
        else:
            work = random.randint(1, 4)
        self.player.work = work
        print('你选择的职业是：{}'.format(fg.work_code[work - 1]))
        print('请选择你的性别：')
        i = 1
        for s in fg.sex_code:
            print(i, '.', s)
            i += 1
        sex = input('请从（1-3）项里选择1项')
        if not sex or eval(sex) not in [1, 3]:
            sex = random.randint(1, 3)
        else:
            pass
        self.player.sex = sex
        print('你选择的性别是：{}'.format(fg.sex_code[sex - 1]))
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
        family_name_path = fg._path + 'family_name.txt'
        secound_name_path = ''
        if os.path.isfile(family_name_path):
            with open(family_name_path, 'r') as text:
                self.family_name = text.read().split()
            text.close
            if sex == 1:
                secound_name_path = fg._path + 'secound_name_2.txt'
            elif sex == 2:
                secound_name_path = fg._path + 'secound_name.txt'
            elif sex == 3:
                secound_name_path = fg._path + 'secound_name_3.txt'
            if os.path.isfile(secound_name_path):
                with open(secound_name_path, 'r') as text:
                    self.secound_name = text.read().split()
                text.close
        else:
            self.family_name = '玩家'
            self.secound_name = str(random.randint(1, 9999))

    def getName(self, sex):
        self.create_username(sex)
        familyname = random.choice(self.family_name)
        secountd = random.choice(self.secound_name)
        all_name = "{}{}".format(familyname, secountd)
        return all_name
