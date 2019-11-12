class Encapsulation:
    def __hide(self):
        print("示例的隐藏方法")
    def getname(self):
        return self.__name
    def setname(self,name):
        if len(name)<3 or len(name)>8:
            raise ValueError("长度不在范围内")
        self.__name = name
    name=property(getname,setname)

e = Encapsulation()
#e.name = "ha"
#print(e.name)
e._Encapsulation__hide()
