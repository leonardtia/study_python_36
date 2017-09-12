album = ['a','b','c','d','e','f','g']
album.append('h')
if('h' in album and album[0] is 'a'):
    print (album[2])
else:
    print (album[album.__len__()-1])

password_list = ['*#*#*#','123456']
def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print ('Login success!')
    elif password_reset:
        new_password = input('Enter a new Password:')
        password_list.append(new_password)
        print ('Your Password has changed successfully!')
        account_login()
    else:
        print ('Wrong password or invalid in put!')
        account_login()
account_login()
