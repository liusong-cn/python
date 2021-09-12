# -*- coding:utf-8 -*-
# @auther: ls
# @date: 2021/8/26
import pandas as pd
import numpy as np


def pandas_demo():
    df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
                       'size': list('SSMMMLL'),
                       'weight': [8, 10, 11, 1, 20, 12, 12],
                       'adult': [False] * 5 + [True] * 2})
    print(df)

    # series允许不同类型的值
    s = pd.Series([1, 5, 2, 'a', np.nan])
    print(s)

    dates = pd.date_range('20130101', periods=6)
    df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df1)

    # 使用series字典生成DataFrame
    df2 = pd.DataFrame({
        'A': 1.,
        # series对象作为一列
        'B': pd.Series(1, index=list(range(4)), dtype='float32'),
        'C': np.array([3] * 4, dtype='int32'),
        'd': pd.Timestamp('20130102'),
        # 单值也会与其他列长度保持一致
        'F': 'foo',
        'E': pd.Categorical(["test", "train", "test", "train"])
    })
    print(df2)


def pandas_data_view():
    """数据查看方式"""

    df2 = pd.DataFrame({
        'A': 1.,
        # series对象作为一列
        'B': pd.Series(1, index=list(range(4)), dtype='float32'),
        'C': np.array([3] * 4, dtype='int32'),
        'd': pd.Timestamp('20130102'),
        # 单值也会与其他列长度保持一致
        'F': 'foo',
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'G': [2, 4, 6, 8]
    })

    print(df2.head())

    print(df2.tail(2))

    print(df2.index)
    print(df2.columns)

    # 数据转置
    print(df2.T)

    # 按轴排序axis=0表示按行排序 1表示按列排序
    print(df2.sort_index(axis=0, ascending=False))

    # 按值排序,理解为常规的按照某列的值进行排序
    print(df2.sort_values(by='G', ascending=False))


def pandas_data_get():
    """pandas api进行值的获取"""
    df2 = pd.DataFrame({
        'A': 1.,
        # series对象作为一列
        'B': pd.Series(1, index=list(range(4)), dtype='float32'),
        'C': np.array([3] * 4, dtype='int32'),
        'd': pd.Timestamp('20130102'),
        # 单值也会与其他列长度保持一致
        'F': 'foo',
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'G': [2, 4, 6, 8]
    })

    # 获取单列的值,此写法不如df2['A']来的直观
    print(df2.A)
    dates = pd.date_range('20210101', periods=6)
    df3 = pd.DataFrame(np.random.randn(6, 3), index=dates, columns=list('ABC'))
    # 按标签获取某行数据,通过索引列进行获取整行数据，类似关系型数据库中的按id获取
    print(df3.loc[dates[0]])

    # 用标签切片,包括行切片和列切片
    print(df3.loc['20210101':'20210102', ['A', 'B']])

    # 提取标量值
    print(df3.loc['20210101', 'A'])

    # 按位置切片，通过行索引排序值
    print(df3.iloc[3])

    # 按位置切片，通过行列的索引的排序值
    print(df3.iloc[3:5, 0:2])

    # 通过类似坐标定位获取单元格值
    print(df3.iloc[0, 0])

    # 布尔筛选，通过单列条件提取值行数据
    print(df2[df2['G'] > 4])


def pandas_data_set():
    """pandas 进行赋值"""
    dates = pd.date_range('20210820', periods=6)
    data = [1, 3, 5, 7, 9, 11]
    df = pd.Series(data, index=dates, name='A')
    # 通过标签进行赋值
    # df.at[dates[0],'A']
    print(df.name)

    # 通过位置进行获取值,由于series为一维序列，因此通过通过位置获取值时只需要传入单个维度
    # 若是dataframe则需要两个维度进行定位
    print(df.iat[1])

    df2 = pd.DataFrame({
        'A': 1.,
        # series对象作为一列
        'B': pd.Series(1, index=list(range(4)), dtype='float32'),
        'C': np.array([3] * 4, dtype='int32'),
        'd': pd.Timestamp('20130102'),
        # 单值也会与其他列长度保持一致
        'F': 'foo',
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'G': [2, 4, 6, 8]
    })
    # 对二维表格进行赋值
    print("二维表格进行赋值")
    # 按标签赋值以及按索引混合赋值
    df2.at[0, 'A'] = 2.5
    print(df2)

    # 按照numpy数组赋值
    df2.loc[:, 'F'] = np.array([5] * len(df2))
    print(df2)

    # 使用where条件进行赋值
    df3 = df.copy()
    df3[df3 > 0] = -df3
    print(df3)


def pandas_data_concat():
    """
    合并dataFrame与series
    :return:
    """
    df = pd.DataFrame(np.random.randn(10, 4))
    print(df)
    # 分组切片,切片左闭右开
    pieces = [df[:3], df[3:7], df[7:]]
    print(pieces)
    # 合并
    print(pd.concat(pieces))

    left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
    right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [3, 4]})
    # sql风格合并, 由于没有匹配的key，生成笛卡尔乘积
    print(pd.merge(left, right, on='key'))
    left1 = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [2, 3]})
    right1 = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [1, 4]})
    print(pd.merge(left1, right1, on='key'))


def pandas_data_append():
    """
    追加数据
    :return:
    """
    data = pd.DataFrame(np.random.randn(10, 4), columns=list('abcd'))
    print(data)
    r = data.iloc[3]
    print(r)
    d1 = data.append(r, ignore_index=True)
    print(d1)

def pandas_data_group():
    """
    分组->应用->组合，可包含三个中的一个或多个操作
    :return:
    """
    data = pd.DataFrame({'A':['foo','bar','foo','bar','foo','che'],
                         'B':['one','two','two','three','three','one'],
                         'C':np.random.randn(6),
                         'D': np.random.randn(6)})
    print(data)
    # 单维度分组再sum
    print(data.groupby(by='A').sum())
    # 多维度进行分组再sum
    print(data.groupby(['A','B']).sum())

def pandas_data_stack():
    """
    多层索引和重塑
    :return:
    """
    tuples = list(zip(*[['bar', 'bar', 'baz', 'baz','foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two','one', 'two', 'one', 'two']
    ]))
    print(tuples)

def test(
        name: int = 1) -> int:
    """
    参数名后跟冒号，冒号后的内容为type hint，表示建议的参数类型，也可以正常赋予默认值，如上所示
    括号外的部分用 -> 随后跟随的为返回结果的type hint,表示对结果的建议类型
    :param name:
    :return:
    """
    print(type(name))
    print(name)
    return name + 2;


if __name__ == '__main__':
    # pandas_demo()
    # pandas_data_view()
    # pandas_data_get()
    # pandas_data_set()
    # pandas_data_concat()
    # pandas_data_append()
    # pandas_data_group()
    pandas_data_stack()