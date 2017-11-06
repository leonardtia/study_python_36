mm = 1
ss = 60 * mm
hh = 60 * ss
dd = 24 * hh
for i in range(1, 8):
    # print('{0} day is {1} m,is {2} ss,is {3} hh hh'.format(i,i*dd,i*dd/60,i*dd/60/60))
    pass
k = input('please input qj:')
c = 0.0041859 * eval(k)
print(c)


def abc():
    sp = input('car speed(km/h):')
    long = input('how long:')
    time = round(eval(long) / eval(sp), 2)
    print('will {} hours arealy'.format(time))
    abc()


abc()
