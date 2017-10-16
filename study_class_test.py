# -*- coding: utf-8 -*-
import random
class FakeUser:
    def __init__(self):
        _path = '/Users/leonard_tia/PycharmProjects/py36/'
        with open(_path + 'family_name.txt','r') as text:
            self.family_name = text.read().split()
        text.close
        with open(_path + 'secound_name.txt','r') as text:
            self.secound_name = text.read().split()
        text.close
    def getName(self,state):
        #familyname = self.family_name[random.randrange(0, self.family_name.__len__())]
        familyname = random.choice(self.family_name)
        secound1 = []
        secound2 = []
        for word in self.secound_name:
            if(word.__len__() == 1):
                secound1.append(word)
            else:
                secound2.append(word)
        if(state == 1):
            #all_name = "{}{}".format(familyname,secound1[random.randrange(0,secound1.__len__())])
            all_name = "{}{}".format(familyname, random.choice(secound1))
        elif(state == 2):
            #all_name = "{}{}".format(familyname,secound2[random.randrange(0,secound2.__len__())])
            all_name = "{}{}".format(familyname, random.choice(secound2))
        else:#all_name = "{}{}".format(familyname,self.secound_name[random.randrange(0,self.secound_name.__len__())])
            all_name = "{}{}".format(familyname, random.choice(secound1+secound2))
        return all_name
    def getSex(self):
        sex_list = ['男', '女', '未知']
        #i = random.randrange(0,2)
        #sex = sex_list[i]
        sex = random.choice(sex_list)
        return sex

class SnsUser(FakeUser):
    def buildman(self, i, s=1):
        #men = []
        for j in range(1, i):
            _user = user()
            _user.name = self.getName(s)
            _user.sex = self.getSex()
            #men.append(_user)
            yield _user

    def get_nick_name(self, i):
        for h in range(1, i):
            nick_name = self.getName(2)
            yield nick_name


class user():
    name=''
    sex = ''

fake = SnsUser()
for man in fake.buildman(10):
    print('{}:{}'.format(man.name, man.sex))
for nickname in fake.get_nick_name(10):
    print('nick:{}'.format(nickname))
