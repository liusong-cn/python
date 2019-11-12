#python内置的三种数据结构
#list
a_list=['a',2,'ab',3]
#用元素索引的方式取数据，可以通过a:b方式取区间，但是区间为左闭右开
print(a_list[0:2])
#list元素允许修改
a_list[2]='abc'
print(a_list[2])
#在末尾添加元素
a_list.append('hhh')
print(a_list)
a_list.pop()
#将末尾元素剔出list
print(a_list)
#元素的排序 sort() reverse()，但是要求元素可以的因素一致，此处str 和int 用常规方式无法进行比较
#a_list.sort(key=len)

#tuple元组，不允许修改元素
a_tuple=(1,2,3,'abcd')
print(a_tuple[0:2])
#元祖不允许修改元素，报错
#a_tuple[1]=4
print(a_tuple[1])

#dictionary字典采用key-value的形式
a_dict={'key1':'hello','key2':'world'}
print(a_dict)
#dictionary的key-value的形式支持key是一个tuple,但是不支持list作为key，因为dict要求key
#不可变
b_dict = {(1,2):'hello','key2':'world'}
print(b_dict)
#list或者tuple都可以作为dict的key-value,但是要求list or tuple都必须只有两个元素
b_list=[(1,2),(3,4),('hello','world')]
c_dict = dict(b_list)
print(c_dict)
#dict的构造函数可以支持)直接使用key-value来定义dict
d_dict = dict(first=1,second=2,third=3)
print(d_dict)
#通过key访问dict,此处发现key必须是字符
print(d_dict['first'])
#通过get方法访问dict
print(d_dict.get('second'))
#item(),keys() values()
print(d_dict.items())
print(d_dict.keys())
print(d_dict.values())