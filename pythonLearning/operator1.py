#运算符优先级和我们理解的一致
print(-2*4+3**2)

#支持自增运算,但不支持前置后置自增运算 egg：++i,i++
x=2
x+=2
print(x)

#自增运算后不能再赋值给另一个var,但支持连续赋值
#y=x+=2
y=x=x+2
print(x,y)

#元组赋值另一种形式,多元赋值
m,n,p = 1,3,['hello','world']
print(m,n,p)
#变得好看一点的方式
(r,s,t) = (1,3,['hello'])
print(r,s,t)

#交换值,相比其他语言通过定义一个tmp变量来说更简洁
i,j = 2,3
print(i,j)
i,j = j,i
print(i,j)


