def addMe2Me(x):
    return x + x

print(addMe2Me(3))
#针对非数字类型的加法相当于*2
print(addMe2Me('hello'))

#设置默认参数
def addMe2Me2(x = 2):
    if x != 2:
        print(str(x+x))
    else:
        print('none')

addMe2Me2()

#关键字参数
def keyfun(key,value):
    print(key - value)

#此种调用方式默认按形参的位置匹配
keyfun(2,3)
#此种方式则为关键字参数，通过制定指定行参的值，可以改变参数的位置
keyfun(value=2,key=3)

#元组类型的参数
def arrayfun(*param):
    total = 0
    for i in param:
        print(i)
    print(total)
c = [i for i in range(1,5)]
d = tuple(c)
arrayfun(d)

#遍历元组
def test():
    m = {1,2,3}
    total = 0
    for i in m:
        total += i
        print(i)
    print(total)
test()