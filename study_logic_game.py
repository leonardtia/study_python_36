import random
def input_game(change):
    if(playgame(change)):
        print ('You are Bingo!!!')
    else:
        print ('You are loser!!!')
        change = input('please change Big or Small or Xman:')
        input_game(change)

def roll_dice(numbers=3):
    list = [];
    for i in range(0,numbers):
        point1 = random.randrange(1, 6)
        list.append(point1)
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
input_game(change)