class Bird:
    def sing(self):
        print("bird sing")

class sonBird(Bird):
    def sing(self):
        print("另一种鸟sing")
    def psing(self):
        self.sing()
        Bird.sing(self)

s = sonBird()
s.sing()
s.psing()