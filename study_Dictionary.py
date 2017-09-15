NASDAQ_code = {
    'Bidu':'Baidu',
    'SINA':'Sina',
    'YOKU':'YouKu'
}
print (NASDAQ_code)

NASDAQ_code['YOKU'] = 'You'
print (NASDAQ_code)

NASDAQ_code.update({'FB':'Facebook','TSLA':'tesla','Bidu':'bb'})
del NASDAQ_code['YOKU']
print (NASDAQ_code)

letters = ('c','b','a','b','c','d','e','f')
print (letters[3])
print (sorted(letters))#倒排序
a_set = {1,2,3,4,5,6,7}
a_set.add(8)
a_set.discard(1)
print (sorted(a_set,reverse=True))

