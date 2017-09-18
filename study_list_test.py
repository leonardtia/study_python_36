def count_walden(word):
    path = '/Users/leonard_tia/downloads/Walden.txt'
    file = open(path,'r')
    i = 0
    for line in file.readlines():
        ws = [w for w in line.split() if w is word]
        i = i + 1
    return i
word = input('plese input check word:')
j = count_walden(word)
print (' \'{}\' in Walden.txt is {} word '.format(word,str(j)))

path = '/Users/leonard_tia/downloads/Walden.txt'
with open(path,'r') as text:
    words = text.read().split()
    print (words)
    for word in words:
        print ('{} - {} times '.format(word,words.count(word)))

import string
path = '/Users/leonard_tia/downloads/Walden.txt'
with open(path,'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}
    for word in sorted(counts_dict,key=lambda x :counts_dict[x],reverse=True):
        print ('{} -- {} times'.format(word,counts_dict[word]))