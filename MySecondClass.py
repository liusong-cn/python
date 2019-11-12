class SecondClass:
    @classmethod
    def clsFunction(self):
        print(self,"类方法")

    @staticmethod
    def staticFunction(self):
        print(self,"静态方法")

SecondClass.clsFunction()
SecondClass.staticFunction("hello,假的调用对象")