import time
all_in_list = [1,1.0,'a word',True,[1,2],(1,2),{'key':'value'}]
print (all_in_list)

fruit = ['pineaple','pear']
fruit.insert(1,'grape')
print (fruit)

fruit[0:0] = ['orange']
print (fruit[0:0])
print (fruit[0:1])
print (fruit[1:0])
print (fruit[1:3])
print (fruit)
del fruit[0:1]
print (fruit)

periodic_table = ['H','He','Li','Be','B',"C",'N','O','F','Ne']
print (periodic_table[0])#H
print (periodic_table[-2])#F
print (periodic_table[0:3])#H,He,Li
print (periodic_table[-10:-7])#H,He,Li
print (periodic_table[-10:])#H,He,Li,Be,B,C,N,O,F,Ne
print (periodic_table[:9])#H,He,Li,Be,B,C,N,O,F
periodic_table.extend(fruit)
print (periodic_table)

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)
print (zipped)
print (zip(*zipped))

a = [i for i in range(1,10)]
print (a)

a = []
t0 = time.clock()
for i in  range(1,20000):
    a.append(i)
print(time.clock() - t0,'seconds process time')
t0 = time.clock()
b = [i for i in range(1,20000)]
print (time.clock() - t0,'seconds process time')

a = [i**2 for i in range(1,10)]
print (a)
c = [j+1 for j in range(1,10)]
print (c)
k = [n for n in range(1,10) if n % 2 == 0]
print (k)
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
print (z)

for num,letter in enumerate(z):
    print (letter,'is',num+1)