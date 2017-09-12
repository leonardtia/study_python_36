def text_create(name,msg):
    desktop_path = '/Users/leonard_tia/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print ('text_create Done')


def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
    print ('text_filter Done')
    return word.replace(censored_word,changed_word)

def text_read(name):
    desktop_path = '/Users/leonard_tia/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'r')
    for line in file.readlines():
        print (line.strip())
    file.close()

def censored_text_create(n,msg1):
    msg2 = text_filter(msg1,censored_word='tian yuan',changed_word='leonard')
    text_create(name=n,msg=msg2)
    text_read(n)
w = 'my name is tian yuan!'
n = 'test'
censored_text_create(n,w)