def funA(fn):
    print('A')
    fn()
    return "success"

@funA
def funB():
    print('B')

print(funB)
a = funB
print(a)

class Category:
    cake=lambda p: print(p)
c=Category()
c.cake()