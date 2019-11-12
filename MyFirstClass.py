class MyClass:
    '这是第一次用python定义类'
    #类变量
    hair = 'blue'
    def __init__(self,name="zhang",age=10):
        #创建的实例变量
        self.name=name
        self.age=age
    def say(self,count):
        print('有这么多钱'+count)

p=MyClass()
print(p.name,p.age)

m=MyClass("wang",12)
print(m.name,m.age)
m.skills = ['chaocai','zhufan']
print(m.skills)
def info_show(self,content):
    print(content)
m.infos=info_show
m.infos(m,'can')

def info_show1(self,con):
    print(con)
from types import MethodType
m.infos1=MethodType(info_show1,m)
m.infos1('不用调用self')

#print函数用法，中间用逗号隔开各个输出，end参数默认为\n 换行，此处不换行故重新设定end参数
print(40,'\t',end='')
print(40,'\t',end='')
print(40,'\t',end='')
#这是复数
complex = 3 + 2j
print(type(complex))
print(complex)
#测试变量替换,%替换符相当于占位符
price = 100
print("这件产品的价格是：%s"%price)
count = 20
print("这批产品的单价是：%s,数量是：%s"%(price,count))
