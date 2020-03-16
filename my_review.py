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
if __name__ == "__main__":
    # fun_type()
    # seq_slice()
    # fun_is()
    some_origin_fun()