#定义并创建字典dict
a = {'first':'hello','second': 2}
print(a)
print(a['first'])
#dict也是key任意，值任意，一般key为数字或字符串
a['third'] = [3,5]
print(a)
#使用for循环遍历
for key in a.keys():
    print(key,a[key])
#使用enumerate生成的为index和key
for i,key in enumerate(a):
    print(i,key)
    print(i,a[key])
    #借助替换符实现替换
    print(i,'这是%i' %i)