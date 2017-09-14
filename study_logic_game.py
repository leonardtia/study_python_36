import random

def input_game(change,money=100,total=1000):

    if(playgame(change)):
        print ('You are Bingo!!!')
        total = total + int(money)
    else:
        print ('You are loser!!!')
        total = total - int(money)
    print ('You have: ${}'.format(str(total)))
    if(total <= 0):
        print ('Game Over!!!')
    else:
        change = input('please angin:')
        money = input('please input money:')
        input_game(change, money,total)

def roll_dice(numbers=3):
    list = [];
    for i in range(0,numbers):
        point1 = random.randrange(1, 6)
        list.append(point1)
    print ('result:{},{},{}'.format(list[0],list[1],list[2]))
    return sum(list)

def playgame(change):
    count = roll_dice()
    if(count >=3 and count <=10):
        result = 's'
    elif (count <=18 and count >=11):
        result = 'b'
    else:
        result = 'x'
    re = result is change
    return re
change = input('please change Big or Small or Xman:')
money = input('please input money:')
input_game(change,money)