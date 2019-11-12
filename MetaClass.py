class ItemClass(type):
    def __new__(cls, name, bases,attrs):
        attrs['call_prices'] = lambda self:self.price * self._discount
        return type.__new__(cls,name,bases,attrs)

class Book(metaclass=ItemClass):
    __slots__ = ('name','price','_discount')
    def __init__(self,name,_discount):
        self.name = name
        self._discount = _discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self,discount):
        self._discount = discount

a = Book('zhangsan',20)
a.price = 10
print(a.call_prices())