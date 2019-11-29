a = 1
b = 2
#比较的是对象的值
print(a < b)
print(a != b)
print(a >= b)
c = a + 1
print(b == c)

#比较对象的身份,即对象的类型，类比java中class
print(b is c)
print(id(b) == id(c))

'''
id()应该是比较对象的内存地址，但是此处明显 b 和 d是两个对象，虽然内存地址一致
so 为啥比较id（）结果一致反而纳闷，是否和java一样有缓存池，
破案：python中也有缓存，对于整型和字符串会缓存，但是float不会缓存，参考下方
fuck：实际测试中发现对于float也缓存了，可能是python版本的问题
'''
d = 1 + 1
print(b is not d)
print(id(b))
print(id(d))

e = 20.1
f = 20.1
print(e is f)
print(id(e))
print(id(f))

