# -*- coding: utf-8 -*-
what_he_does = ' plays '
his_name = 'Robert Johnson'
his_instrument = ' guitar '
artist_intro = his_name + what_he_does + his_instrument
print (artist_intro)

num = 1
string = '1'
num2 = int(string)
print (num2 + num)

words = 'tia' * 12
print (words)

word = 'a loooooooog word'
num3 = 12
string = 'bang!'
total = string * (len(word) - num3)
print (total)

name = 'my name is leonard'
#正向序号第0个字符
print (name[0])
#逆向序号第4个字符
print (name[-4])

print (name[11:14])
print (name[11:15])
#截取第5个字符开始直到最后一个字符
print (name[5:])
#截取第1个字符到第5个字符
print (name[:5])

word1 = 'friends'
find_the_evil_in_your_friends = word1[0] +word1[2:4] + word1[-3:-1]
print (word1[0])
print (word1[2:4])
print (word1[-3:-1])
print (find_the_evil_in_your_friends)
#fiene
word2 = 'https://www.leangoo.com/kanban/board/go/2193299'
file_name = word2[-7:]
print(file_name)

phone_number = '15107145855'
hiding_number = phone_number.replace(phone_number[3:8],'*'*5)
print (hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print (search + ' is at ' + str(num_a.find(search)) + ' to ' +str(num_a.find(search) + len(search) ) + ' of num_a')
print (search + ' is at ' + str(num_b.find(search)) + ' to ' +str(num_b.find(search) + len(search) ) + ' of num_b')

print ('{} a word she can get what she {} for'.format('With','came'))
words1 = '{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came')
print (words1)
words2 = '{0} a word she can get what she {1} for'.format('With','came')
print (words2)

city = raw_input("write down the name of city:")
print (city)
url = 'my city is {}'.format(city)
print (url)

def function(arg1,arg2):
    return 'someting'