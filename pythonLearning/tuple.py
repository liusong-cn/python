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
#查看方法声明的另一种方式，光标定位需要查看的方法上，点击view，选择quick documention或官方文档