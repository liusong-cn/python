#可以继承父类，默认的父类为object，单继承
class Foo(object):
    version = 1.0
    #self是类实例的引用，类似其他语言中的this
    def __init__(self, name = 'zhang'):
        self.name = name
        print('这个方法类似构造函数，但不同于其他语言，此处是类实例在创建后自动执行的第一个方法而已')

    def show(self):
        print(self.name)

    def addMe2Me3(self, x):
        print(str(x + x))

foo = Foo();
print(foo.name)
print(foo.addMe2Me3(2))