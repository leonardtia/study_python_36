# -*- coding: utf-8 -*-
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self,how_much):
        if how_much == 'a sip':
            print ('Cool-')
        elif how_much == 'Whole bottle':
            print ('Headache!')
ice_coke = CocaCola()
ice_coke.drink('a sip')
coke = CocaCola()
if(coke.drink('s') == CocaCola.drink(coke,'s')):
    print ('1')
else:
    print ('0')
coke_for_me = CocaCola()
coke_for_you = CocaCola()
print (coke_for_me.formula)
print (coke_for_you.formula)
print (CocaCola.formula)

for element in coke_for_you.formula:
    print (element)

coke_for_china = CocaCola()
coke_for_china.local_logo = '可口可乐'
print (coke_for_china.local_logo)

class persin():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):#初始化
        self.local_logo = '百事可乐'
    def drink(self):
        print ('Energy')
coke = persin()
print (coke.local_logo)

class CocaCola1:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self,logo_name):
        for element in self.formula:
            print ('{} has {}!'.format(logo_name,element))
        self.local_logo = logo_name
    def drink(self):
        print ('###')
coke = CocaCola1('百事')
print (coke.local_logo)

class CocaCola_new:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print ('You got {} cal energy!'.format(self.caffeine))

#CaffeineFree继承自CocaCola_new类
class CaffeineFree(CocaCola_new):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color']
coke_a = CaffeineFree('Cocacola-FREE')
coke_a.drink()
print (coke_a.local_logo)

class TestA:
    attr = 1
obj_a = TestA()
TestA.attr = 42
print (obj_a.attr)#42

class TestB:
    attr = 1
obj_a = TestB()
obj_b = TestB()
obj_a.attr = 42
print (obj_b.attr)#1

class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42
obj_a = TestA()
print (obj_a.attr)#42
print (TestA.__dict__)
print (obj_a.__dict__)

obj1 = 1
obj2 = 'String!'
obj3 = []
obj4 = {}
print(type(obj1),type(obj2),type(obj3),type(obj4))


