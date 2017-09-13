import random
def input_game(change):
    if(playgame(change)):
        print ('You are Bingo!!!')
    else:
        print ('You are loser!!!')
        change = input('please change Big or Small or Xman:')
        input_game(change)

def playgame(change):
    list = [];
    re = False;
    for i in range(0,3):
        point1 = random.randrange(1,9)
        list.append(point1)
    count = sum(list)
    result = None
    if(count >0 and count <14):
        result = 's'
    elif (count <=27 and count >16):
        result = 'b'
    else:
        result = 'x'
    re = result is change
    return re
change = input('please change Big or Small or Xman:')
input_game(change)