# -*- coding: UTF-8 -*-
import os
def ten_build_file(i):
    _path = '/Users/leonard_tia/'
    while i >=1:
        _file = _path + str(i) + '.txt'
        file = open(_file,'w')
        file.close()
        i = i - 1
ten_build_file(5)

def invest(amount,rate,time):
    year = 0
    while year <= time:
        amount = amount * (1 + rate)
        year = year + 1
        print ('year {}:${}'.format(year,amount))
invest(50000,0.0004,12)

for i in range(1,100):
    if i % 2 == 0:
        print ('{},'.format(i))