class Fruit:
    def info(self):
        print("水果",'这是水果')

class Food:
    def shape(self):
        print('食物',"这是食物的形状")

class Apple(Fruit,Food):
    pass

a = Apple()
a.info()
a.shape()

class Fruit2:
    def info(self):
        print("水果2",'这是水果2')

class Apple2(Fruit2,Fruit):
    pass
a2 = Apple2()
a2.info()
