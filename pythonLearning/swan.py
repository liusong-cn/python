# code=utf-8
# 测试类私有属性的访问
class Swan:
    """
    类的私有属性通过双下划线表示
    """
    __neck_swan = '天鹅脖子长'

    def __init__(self):
        print("__init__():", Swan.__neck_swan)


swan = Swan()
# 访问类的私有属性要么在类中访问，要么通过实例._类名__xxx
print("加入类名访问：", swan._Swan__neck_swan)
# print("不加类名访问：", swan.__neck_swan)
