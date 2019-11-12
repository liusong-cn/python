#使用import时，要是要导入后的包中的类需要加包名，类似表空间.类名
#import pathlib
# p = pathlib.PurePath('aaa')
# print(type(p))
from pathlib import *

p1 = PurePath('aaa')
#支持用/作为连接符
print(p1/'bbb')
#windows平台上不能使用unix风格的路径
# p2 = PosixPath('aa1')
# print(p2/'bb1')

p3 = Path('.')
for x in p3.iterdir():
    print(x)

#读写文件
p4 = Path('a.txt')
result = p4.write_text('这是一个测试文件',encoding='gbk')
print(result)

x = p4.read_text(encoding='gbk')
print(x)