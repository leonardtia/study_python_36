import random

from F_enemy import enemy

mehord = ('正义', '邪恶', '中立')
prop_hp = {'布甲': 7, '铁盔甲': 12, '重装铠甲': 15, '符文重装铠甲': 20, '雷欧之铠': 24, '雷欧之盔': 10, '雷欧之盾': 50}
prop_mp = {'白法袍': 5, '红法袍': 7, '黑法袍': 10, '紫色法衣': 15, '符文紫色法衣': 20, '雷霆法衣': 24, '雷霆法杖': 10, '魔法之轮': 50}
prop_atn = {'铁之剑': 5, '钢之剑': 9, '光之剑': 13, '圣堂之剑': 17, '符文圣堂之剑': 21, '誓约胜利之剑': 30, '命运之矛': 50}
prop_it = {'水之戒指': 6, '火之戒指': 11, '光之戒指': 14, '圣光之戒': 16, '符文圣光之戒': 19, '无限宝石': 31, '尼伯龙根之戒': 60}
prop_kar = {'马蹄铁': 4, '四叶草': 8, '过山龙': 12, '钻地鼠': 16, '幸运石': 22, '幸运星': 35, '幸运女神': 99}
award = {'小血瓶': 6, '大血瓶': 10, '大鸡腿': 15, '无敌霸王汉堡': 25, '治疗圣药': 40, '大天使之吻': 55, '精灵女神': 99}
evil = {'哥布林': 1, '地精': 2, '大地精': 5, '巨魔': 7, '食人魔': 10, '狼骑士': 13, '狮鹫兽': 25, '九头蛇': 30, '森林女妖': 35, '沙虫': 40,
        '雷鸟': 45, '火龙': 50, '撒旦恶魔': 66, '死亡女神': 88}


class event_abc:
    def suijishijian(self, person):
        mehord1 = random.choice(mehord)
        if (mehord1 == '正义'):
            return self.event_award(person)
        elif (mehord1 == '邪恶'):
            return self.event_evil(person)
        elif (mehord1 == '中立'):
            print(mehord1)
            return True

    def event_award(self, person):
        kar = person.nature['kar']
        list = []
        for k, v in award.items():
            list.append(k)
        icount = len(list)
        bingou = random.randint(0, icount - 1)
        bingou_k = list[bingou]
        bingou_v = random.randint(award.get(bingou_k) - 5, award.get(bingou_k) + 5)
        hp = int(bingou_v * kar / 100)
        print('你得到了{},所以你增加了{}点生命值'.format(bingou_k, str(hp)))
        person.nature['hp'] += hp
        return True

    def battle(self, person):
        eh = enemy.hp
        mykar = person.nature['kar']
        myhp = person.nature['hp']
        mymp = person.nature['mp']
        myit = person.nature['it']
        myatn = person.nature['atn']
        mywork = person.work
        print('糟糕，你遇到了一头野生的{},战斗无法避免了！'.format(enemy.name))
        while eh > 0 and myhp > 0:
            atn = round(enemy.atn * enemy.kar * random.random() / mykar, 2)
            myhp -= atn
            print('{}给了你一个凶狠的惩戒攻击,你损失了{}点生命值'.format(enemy.name, str(round(atn, 2))))
            myatn = round(person.nature['atn'] * mykar / enemy.kar * random.random(), 2)
            eh -= myatn
            print('你一个漂亮的回旋踢，让{}损失了{}点生命值'.format(enemy.name, str(round(myatn, 2))))
        if eh <= 0:
            print('战斗结束了，你赢得了胜利')
            person.nature['hp'] = int(myhp)
            return True
        elif myhp <= 0:
            print('战斗失败了，你输掉了战斗，也输掉了生命！')
            return False

    def event_evil(self, person):
        kar = random.randint(person.nature['kar'] - 5, person.nature['kar'] + 5)
        hp = person.nature['hp']
        mp = person.nature['mp']
        it = person.nature['it']
        atn = person.nature['atn']
        list = []
        for k, v in evil.items():
            list.append(k)
        icount = len(list)
        bingou = random.randint(0, icount - 1)
        bingou_k = list[bingou]
        bingou_v = evil.get(bingou_k)
        enemy.name = bingou_k
        enemy.kar = round(kar * (bingou + 1) / icount, 2)
        enemy.hp = round(bingou_v / kar * enemy.kar, 2)
        enemy.mp = round(bingou_v / kar * enemy.kar, 2)
        enemy.atn = round(bingou_v * (bingou + 1) / icount / kar * enemy.kar, 2)
        enemy.it = round(bingou_v * (bingou + 1) * enemy.mp / enemy.hp, 2)

        return self.battle(person)
