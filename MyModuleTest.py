'''
此模块用于测试python的模块引用
'''
a = "这是一个测试变量"
def sayhi(name):
    print('sayhi的人是:'+name)

class User:
    name= 'zhang'
    age = 10
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def simple_test(self):
        print("这是一个简单的python模块")

