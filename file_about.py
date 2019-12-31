#coding=utf-8
"""学习文件相关操作"""
# 使用关键字参数避免设置其他不必要的参数
f = open('test/file_about.txt','w+',encoding='utf-8')
#多行文本
string = """ 今天是个好日子
            明天放假
            后天居然又上班了
"""
f.write(string)

import chardet #用于查看编码
#指定打开文件的编码
fin = open('test/file_about.txt','r',encoding='utf-8')
#迭代方式有几种，现在fin对象本身可迭代，因此可以直接使用下方方式，或者iter(fin)
for line in fin:
    print(line)
    #chardet接收一个bytes
    print(chardet.detect(bytes(line,encoding='utf-8')))


#去除首尾空白符空白符
str = "  ,,,hhhhmmmm    "
print(str)
print(str.strip())
