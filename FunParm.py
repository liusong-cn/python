def test(weight,height):
    print('重量是：'+str(weight),"高度是：" + str(height))

#通用的位置参数
test(3,4)
#关键字参数，允许交换形参的位置，但是要求关键字参数必须在形参之后
test(height=6,weight=5)
#在代码编写阶段工具就会提示关键字参数必须位于形参之后
#test(height=8,3)
test(8,height=4)

def test1(age=10,sex='male'):
    #使用默认参数，调用时如果不传入参数就使用该默认值
    print('年龄是：'+ str(age),'性别是：' + sex)
    #测试使用格式化字符串
    print("年龄是：%s,性别是:%s"%(age,sex))
test1()

#支持个数可变的参数，java中args...类似。要求一个函数最多只有一个个数可变的普通参数
#不要求该参数收集处于形参列表的最后，但是在使用上会有区别
def test2(*books,name):
    for b in books:
        print(b)
    print(name)

#如果普通形参位于定义的最后，那么要求使用关键字参数
test2('java','python','c','c++',name='book')

def test3(name,*books):
    for b in books:
        print(b)
    print(name)
#从此例子中看出如果普通参数位于函数定义的开始，则不用通过关键字参数来使用
test3('book2','java','python','c')

#对关键字参数的收集，收集之后其实是一个dict
def test4(**books):
    print(type(books))
    #对dict的遍历是用items(),keys(),values()方法来遍历
    #如何通过下标来遍历？
    for k,v in books.items():
        print(v)

test4(book5='java2',book6='python2')

#通过下标索引来访问list
a_list = [1,2,3,4,5,7,11]
#取list的长度的函数和java调用的方式不一样，python中 len(0),java中 o.length
for i in range(0,len(a_list)):
    #%d占位符表示将替换成十进制的数字
    print('第%d个元素是：%s'%(i,a_list[i]))