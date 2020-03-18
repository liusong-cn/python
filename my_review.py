# _*_ coding:utf-8 _*_
# author:ls
# time:2020/3/16 0016
def fun_type():
    #int属于基本类型
    print(type(32))
    #python内荐类型之一
    print(type(type(32)))

def seq_slice():
    a = [1,2,3,4]
    # 左闭右开,0到1
    print(a[0:2])
    #倒数第二个
    print(a[-2])
    #步长-1，从倒数第二到倒数第四
    print(a[-2:-4:-1])
    #取全部
    print(a[::])

def fun_is():
    a = b = 3
    #判断对象内存地址是否一致
    print(a is b)
    print(a is not b)
    #其内存地址
    print(id(a))
    #此处还是创建3.1这个float对象，给c d两个引用
    c = d = 3.1
    print(c is d)
    #由于缓存，任然是同一个对象
    e=3.2
    f=3.2
    print(e is f)

def some_origin_fun():
    a = 1
    b = 3
    #返回obj的string形式 == ``,但3.7已废弃
    print(repr(1))
    print(type(repr(3)))
    #判断对象是否为类的实例
    print(isinstance(1,int))
    #生成iter的序号和值的tuple组成的enum
    x = enumerate(['w','o','s','h','i'])
    print(x)
    for i in iter(x):
        print(i)
    #可直接定义list
    for i in [2,3,4,5]:
        print(i)
    y = [3,5,6,7]
    #iter对所有可迭代的对象都适用
    for i in iter(y):
        print(i)
    #dict use, dict是关键字
    dicts = dict(one='wes',second='hello',third=3)
    #这是一个map
    dicts1 =dict((['x',1],['y',2]))
    print(dicts,dicts1)
    for key in dicts.keys():
        value = dicts[key]
def format_print():
    # %f 浮点数 %e 科学计数法 %d 有符号十进制 %o 八进制 %x 16进制 %s string %u 无符号十进制
    print("we are %d" %18)
    print("we are %x" %14)
    print("we are %e" %123)
    #原始字符串，r后面的字符串保持原样输出
    print(r"\n")

def use_for():
    #common use
    a = [1,2,5,4]
    for i in a:
        print(i)
    # for循环会在循环可迭代对象时，自动调用其next()方法，比java的方便 while i.hasNext(),i是迭代器
    b = iter(a)
    for i in b:
        print(i)
    # 复杂列表推导式
    c = [x*3 for x in range(10) if x <3]
    for i in c:
        print(i)

def file_rw():
    # access_mode: a append ;w write ;+ write and read ;b byte; U 支持通用换行符
    # f = open("test/trywrite_file.txt",'a')
    # f.write('\nappend something')
    # f.close(
    #逐行读取
    b = open('test/trywrite_file.txt','r')
    for line in b:
        print(line)
    b.close()
    print('--------')
    #当某个文件被读取完之后，其指针已经到末尾因此想再次获取该文件只有重新打开，和tuple的generator一样
    #返回的list
    m = open('test/trywrite_file.txt','r')
    print(m.readlines())
    m.close()



if __name__ == "__main__":
    # fun_type()
    # seq_slice()
    # fun_is()
    # some_origin_fun()
    # format_print()
    # use_for()
    file_rw()