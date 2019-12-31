"""尝试使用@装饰器"""
class myclass(object):

    #普通的方法即实例方法，需要参数self，表示对实例的引用
    #类方法不需要实例，用staticmethod修饰
    @staticmethod
    def first_func():
        print(111)

myclass.first_func()

#自定义装饰器，装饰器最内部的函数包含对目标函数的调用，以及与目标函数无关的额外操作，最内部的函数需要返回对目标函数的调用
#而装饰器需要返回对最内部函数的引用
def log(func):
    def wrapper(*tuple,**dict):
        print('%s called'%func.__name__)
        return func(*tuple,**dict)
    return wrapper

@log
def now(str):
    print('2019-12-31%s' %str)

#now('年')

#若装饰器本身需要传递参数，那么就在原本的装饰器基础上再次封装一层装饰器，如下所示
def log1(text):
    def decorator(func):
        def wrapper(*tuple,**dict):
            print('%s,%s' %(text,func.__name__))
            return func(*tuple,**dict)
        return wrapper
    return decorator
@log1('hello')
def now1(str='默认参数'):
    print(str)

now1()