import math
g = input('please input :')
def g2kg(arg1):
    arg2 = int(arg1)/2
    return arg2
kg = '{}kg'.format(g2kg(g))
print (kg)

def zjsjx(l1,l2):
    l1 = l1 ** 2
    l2 = l2 ** 2
    l3 = l1 + l2
    l3 = math.sqrt(l3)
    return l3

print ('The right triangle third side''s length is {}'.format(zjsjx(7,9)))

def trapezoid_area(base_up,base_down,height=3):
    return 1/2 * (base_up + base_down) * height

print (trapezoid_area(base_up=1,base_down=2,height=3))
print (trapezoid_area(base_up=3,base_down=2,height=1))
print (trapezoid_area(1,2))

def file_m(file_name,words):
    file = open(file_name,'a')
    file.write(words)
    file.close()
    file = open(file_name,'r')
    for line in file.readlines():
        print (line.strip())
    file.close()
    return 'success'
file_name = '/Users/leonard_tia/1.txt'
words = '\nhello my friend'
print (file_m(file_name,words))


def file_max(file_name):
    file = open(file_name,'a')
    file.write(words)
    file.close()
    count = 0
    file = open(file_name,'r')
    for line in file:
        if count == 3:
            print ('---------分割---------')
            count +=1
            continue
        print (line)
    file.close()
    return 'finished'
file_name = '/Users/leonard_tia/1.txt'
print (file_max(file_name))