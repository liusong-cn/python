'''
用于记录逻辑判断和循环的学习
'''

def logic_decision():
    x,y = 3,4
    #使用类似java中的三目运算符
    z = x if x>y else y
    print(z)

    if x == y:
        print("=")
    elif x > y:
        print("x>y")
    elif x < y:
        print("x<y")
#logic_decision()

def loop():
    #python中创建列表较为简单，列表类似java中的数组或者list，不需要先声明再使用，可以一步到位
    # for i in [1,2,3,4]:
    #     print(i)

    """两种方式访问可迭代的数据类型，包括元组，列表"""
    x = [1,3,5,6,7]
    for i in x:
        if i > 5:
            break
        else:
            print(i)

    for i in range(x.__len__()):
        print(x[i])

loop()