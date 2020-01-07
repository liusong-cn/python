#元组的元素类型任意
a = ('hello',1,2,[1,4])
print(a)
#支持索引访问
print(a[1])
#支持切片访问，默认step为1可以不指定
print(a[1:3:1])
#使用元祖推导式创建元组
b = (int(x*3) for x in range(10))
print(b)
#元组的下一个元素，快捷键ctrl+d和idea中不同，此处为复制当前行
print(b.__next__())
print(b.__next__())
#和元组推导式不同，列表推导式产生的是列表，而元组推导式产生的是元组生成器对象
c = [int(x*3) for x in range(10)]
d = [int(x*3) for x in range(10) if x < 3]
print(d)
print(c)
#使用内置help方法查看帮助
#help(range)
#查看方法声明的另一种方式，光标定位需要查看的方法上，点击view，选择quick documention或官方文档 ctrl+q

#判断是否包含
s = "hello"
print( 'h' in s,'m' not in s)

#去掉最后一个字符
s = 'hellomyworld'
i = -1
for i in range(-1,-len(s),-1):
    print(s[:i])

#三引号支持跨行书写
h = '''hello
 today'''
print(h)

#
s = str('好')
print(s)

#测试re正则
import re

def re_test():
    pattern = '(\w+\.)|(\d+)'
    result = re.findall(pattern, 'www.baidu.com/1245.news/13')
    print('测试成功')
    print(type(result))
    print(len(result))
    for i in range(len(result)):
        print(result[i])
        print("下面是列表元素的元素，re返回的结果叫匹配对象，是列表，列表的元素为元祖，下方为元祖内的元素")
        for j in result[i]:
            print(j)

def re_test1():
    pattern = '(\d{1})abc\(d{1})'
    #findall在无子组时返回整个匹配的子串，有子组时返回匹配的子组
    result = re.findall(pattern, '1abc23abc4')
    for i in result:
        print(i)
if __name__ == '__main__':
    print('----')
    re_test1()
    print('~~~~~')