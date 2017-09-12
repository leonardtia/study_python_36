for every_letter in 'Hello world':
    print (every_letter)

for num in range(1,11):
    print (str(num) + ' + 1',num + 1)

song_list = ['Holy','Thunderstruck','Rebel']
for song in song_list:
    if song == 'Holy':
        print ('Dio')
    elif song == 'Thunderstruck':
        print ('AC/CD')
    else:
        print ('David Bowie')
for i in range(1,10):
    for j in range(1,10):
        print ('{} * {} = {}'.format(i,j,i*j))

count = 0
while True:
    print (str(count))
    count = count + 1
    if count == 5:
        break

def check_password(pwd):
    bo = None
    if(pwd is '123456'):
        bo = True
    else:
        bo = False
    return bo



count1 = 0
pwd1 = input('please input pwd:')
if check_password(pwd1):
    print ('pwd is right')
else:
    while count1 < 3:
        print ('pwd is wrong:{} time'.format(str(count1)))
        pwd1 = input('please input pwd:')
        check_password(pwd1)
        count1 = count1 + 1


password_list = ['*#*#','12345']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]
        if password_correct:
            print ('Login success!')
        elif password_reset:
            new_password = input('Enter a new password:')
            password_list.append(new_password)
            print ('Password has changed successfully!')
            account_login()
        else:
            print ('Wrong password or invalid input!')
            tries = tries -1
            print (tries,'times left')
    else:
        print('Your account has been suspended')
account_login()
