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