import sys
sys.stdout.write('hello world\n')
sys.stdout.write(sys.version)

#引用模块并使用aliase
import random as r

print(r.random)
#运算符优先级和我们理解的一致
print(-2*4+3**2)