import pathlib as p
import fnmatch
p1 = p.Path('.')
#iterdir()似乎是一个内置的函数，不懂其由来
for x in p1.iterdir():
    # 和java的非表达不太一样
    if not fnmatch.fnmatch(x,'[abc].txt'):
        print(x)
# print(p1.iterdir())
# r = fnmatch.fnmatch(p1,'[abc].txt')
# print(r)
#测试打开文件
file = open('a.txt','r',True)
print(file.mode,file.name,file.closed,file.encoding)
file.close()

#测试读文件,读写的文件为字符
f = open('a.txt','r',1)
while True:
    ch = f.read(1)
    if not ch:break
    print(ch,end='')
f.close()

#用二进制的方式读文件,
f2 = open('a.txt','rb',1)
#文件默认是用gbk编码的
print(f2.read().decode('gbk'))
f2.close()

#用with语句自动关闭资源
with open('a.txt','r',1) as f:
    while 1:
        line = f.readline()
        if not line:break
        print(line,end="")