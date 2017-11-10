# 向文件a写入12345678
f = open('a', 'w')
f.write('12345678')
f.close()
f = open('a', 'r')  # 'r'打开文件，指针在开头
s = f.read()
f.close()
print(s)
# 向文件a末尾写入9000，'a'打开文件，指针在末尾
f = open('a', 'a')
f.write('9000')
f.close()
f = open('a', 'r')
s = f.read()
f.close()
print(s)
# 将'123456789'更新为987654321，指针在更新的字符串的末尾
f = open('a', 'r+')
f.write('987654321')
s = f.read()
f.close()
print(s)
# 在末尾追加@@@，指针还是在末尾
f = open('a', 'a+')
f.write('@@@')
s = f.read()
f.close()
print(s)
f = open('a', 'r')
s = f.read()
f.close()
print(s)

l = ['11\n', '22\n', '33\n', '44\n', '55\n']
f = open('a', 'r+')
f.writelines(l)
f.close()
f = open('a', 'r')
c = f.read()
print(c)
# 移动指针（偏移量，选项）
# 选项=0，表示将文件指针指向从文件头部到'偏移量'字节处
# 选项=1，表示将文件指针指向从文件当前位置，向后移动偏移量字节
# 选项=2，表示将文件指针指向从文件的尾部，向前移动偏移量字节,如果是文本类型，是无法从末尾移动，除非是用rb 二进制的形式打开
f.seek(0, 0)
b = f.readlines(10)
print(b)

f.close()
